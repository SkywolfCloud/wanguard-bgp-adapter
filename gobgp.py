# read prefix from gobgp and write it to wanguard
import base64
import logging
from logging import error, info, debug

import grpc
import requests
import yaml

from api import gobgp_pb2_grpc, gobgp_pb2, attribute_pb2
from config import Config

logging.basicConfig(level=Config.LOG_LEVEL)
templates = {}
ip_groups = {}
header = {"Content-Type": "application/json",
          "Authorization": f"Basic {base64.b64encode((Config.WANGUARD_USERNAME + ':' + Config.WANGUARD_PASSWORD).encode('utf-8')).decode('utf-8')}"}


def ip_zone_id():
    r = requests.get(Config.WANGUARD_BASE_URI + "/v1/ip_zones",
                     params={"ip_zone_name": Config.WANGUARD_IP_ZONE}, headers=header)
    if r.status_code == 200:
        return r.json()[0]["ip_zone_id"]
    else:
        error(f"get ip zone failed: {r.status_code} {r.text}")
        return None


IP_ZONE_ID = ip_zone_id()
debug(f"IP_ZONE_ID: {IP_ZONE_ID}")


def communities_init():
    with open("communities.yaml") as f:
        communities = yaml.load(f, Loader=yaml.CLoader)
        for i, j in communities["template"].items():
            r = requests.get(Config.WANGUARD_BASE_URI + "/v1/threshold_templates",
                             params={"threshold_template_name": j}, headers=header)
            if r.status_code == 200:
                templates[i] = r.json()[0]["threshold_template_id"]
            else:
                error(f"get threshold template failed: {r.status_code} {r.text}")
        for i, j in communities["ip_group"].items():
            ip_groups[i] = j
    debug(f"templates: {templates}, ip_groups: {ip_groups}")


def add_prefix(prefix, ip_group, template):
    r = requests.get(Config.WANGUARD_BASE_URI + "/v1/ip_zones/" + str(IP_ZONE_ID) + "/prefixes",
                     params={"prefix": prefix}, headers=header)
    if r.status_code == 200:
        prefix_id = r.json()[0]["prefix_id"]
        r = requests.put(Config.WANGUARD_BASE_URI + "/v1/ip_zones/" + str(IP_ZONE_ID) + "/prefixes/" + str(prefix_id),
                         json={"ip_group": ip_group, "thresholds_template_id": template,
                               "comments": "auto added by bgp-adapter"},
                         headers=header)
    if r.status_code != 200:
        r = requests.post(Config.WANGUARD_BASE_URI + "/v1/ip_zones/" + str(IP_ZONE_ID) + "/prefixes",
                      json={"prefix": prefix, "ip_group": ip_group,
                            "thresholds_template_id": template,
                            "comments": "auto added by bgp-adapter"},
                      headers=header)
        if r.status_code != 201:
            error(f"add prefix failed: {r.status_code} {r.text}")


def del_prefix(prefix):
    # only delete <prefix>
    r = requests.get(Config.WANGUARD_BASE_URI + "/v1/ip_zones/" + str(IP_ZONE_ID) + "/prefixes",
                     params={"prefix": prefix}, headers=header)
    if r.status_code == 200:
        r = requests.delete(
            Config.WANGUARD_BASE_URI + "/v1/ip_zones/" + str(IP_ZONE_ID) + "/prefixes/" + str(r.json()[0]["prefix_id"]),
            headers=header)


def int_to_bgp_community(value):
    assert 0 <= value < 2 ** 32, "Value must be a 32-bit integer"
    high = value >> 16
    low = value & 0xFFFF
    return f"{high}:{low}"


def handle_route_added(route):
    prefix = attribute_pb2.IPAddressPrefix()
    route.nlri.Unpack(prefix)
    prefix = prefix.prefix + "/" + str(prefix.prefix_len)
    communities = []
    for attr in route.pattrs:
        if attr.Is(attribute_pb2.CommunitiesAttribute.DESCRIPTOR):
            com = attribute_pb2.CommunitiesAttribute()
            attr.Unpack(com)
            communities.extend([int_to_bgp_community(i) for i in com.communities])
        elif attr.Is(attribute_pb2.LargeCommunitiesAttribute.DESCRIPTOR):
            com = attribute_pb2.LargeCommunitiesAttribute()
            attr.Unpack(com)
            communities.extend([f"{i.global_admin}:{i.local_data1}:{i.local_data2}" for i in com.communities])

    ip_group = ""
    template = ""
    for com in communities:
        if com in templates:
            template = templates[com]
        if com in ip_groups:
            ip_group = ip_groups[com]
    if ip_group and template:
        add_prefix(prefix, ip_group, template)
        info(f"Route added: {prefix} {communities} {ip_group} {template}")
    else:
        error(f"No ip_group or template found: {prefix} {communities}")


def handle_route_deleted(route):
    prefix = attribute_pb2.IPAddressPrefix()
    route.nlri.Unpack(prefix)
    route = prefix.prefix + "/" + str(prefix.prefix_len)
    info(f"Route deleted: {route}")
    del_prefix(route)


def main():
    channel = grpc.insecure_channel(Config.GOBGP_URI)
    stub = gobgp_pb2_grpc.GobgpApiStub(channel)

    watch_request = gobgp_pb2.WatchEventRequest(table=gobgp_pb2.WatchEventRequest.Table(filters=[
        gobgp_pb2.WatchEventRequest.Table.Filter(init=True)]))
    # 订阅表格事件
    # watch_request.table.filters.add(type=gobgp_pb2.WatchEventRequest.Table.Filter.ADJIN, init=True)
    debug(watch_request)
    try:
        for event in stub.WatchEvent(watch_request):
            debug(f"Event: {event}")
            if event.HasField("peer"):
                debug(f"Peer: {event.peer}")
            if event.HasField("table"):
                for path in event.table.paths:
                    if path.is_withdraw:
                        handle_route_deleted(path)
                    else:
                        handle_route_added(path)
    except grpc.RpcError as e:
        error(f"An RPC error occurred: {e.code()} {e.details()}")


if __name__ == '__main__':
    communities_init()
    main()
