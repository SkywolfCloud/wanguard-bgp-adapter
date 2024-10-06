import grpc
import sys

from api import attribute_pb2
from api.gobgp_pb2 import ListPathRequest, Family
from api.gobgp_pb2_grpc import GobgpApiStub
from config import Config


# Function to get community from GoBGP
def get_community_from_gobgp(stub, resource, name, family):
    request = ListPathRequest(table_type=resource, name=name, family=family)
    response = stub.ListPath(request)
    communities = []
    for path in response.paths:
        for attr in path.pattrs:
            if attr.WhichOneof("attr_type") == "community":
                communities.extend(attr.community.communities)
    return communities


# 假设你已经有了 gobgp 的 .proto 文件编译生成的 Python 代码：gobgp_pb2 和 gobgp_pb2_grpc


def int_to_bgp_community(value):
    assert 0 <= value < 2**32, "Value must be a 32-bit integer"
    high = value >> 16
    low = value & 0xFFFF
    return f"{high}:{low}"


def get_as_path_and_community(prefix):
    # 创建与 GoBGP 的 gRPC 连接
    channel = grpc.insecure_channel(Config.GOBGP_URI)
    stub = GobgpApiStub(channel)

    # 构造请求，查询指定前缀的 AS 路径
    family = Family(afi=Family.AFI_IP, safi=Family.SAFI_UNICAST)  # IPv4 unicast
    request = ListPathRequest(
        table_type=0, family=family, prefixes=[{"prefix": prefix}]
    )
    paths = list(stub.ListPath(request))
    if not paths:
        print(f"No path found for {prefix}")
        return ""
    else:
        path = paths[0].destination.paths[0]
        as_path = ""
        communities = extended_communities = large_communities = []
        for attr in path.pattrs:
            if attr.Is(attribute_pb2.AsPathAttribute.DESCRIPTOR):
                as_path_attr = attribute_pb2.AsPathAttribute()
                attr.Unpack(as_path_attr)
                as_path = " ".join(
                    [Config.EXABGP_ASN, *map(str, as_path_attr.segments[0].numbers[1:])]
                )
            if attr.Is(attribute_pb2.CommunitiesAttribute.DESCRIPTOR):
                communities_attr = attribute_pb2.CommunitiesAttribute()
                attr.Unpack(communities_attr)
                communities = [
                    int_to_bgp_community(i) for i in communities_attr.communities
                ]
            if attr.Is(attribute_pb2.LargeCommunitiesAttribute.DESCRIPTOR):
                large_communities_attr = attribute_pb2.LargeCommunitiesAttribute()
                attr.Unpack(large_communities_attr)
                large_communities = [
                    f"{i.global_admin}:{i.local_data1}:{i.local_data2}"
                    for i in large_communities_attr.communities
                ]

    channel.close()
    return as_path, communities, extended_communities, large_communities


def broadcast_prefix_with_community(prefix, community, large_community, as_path):
    # 配置 ExaBGP 的命名管道或输入文件的路径
    with open(Config.EXABGP_CMD, "w") as f:
        # 构造 ExaBGP 的命令
        command = (
            f"announce route {prefix} next-hop self community [{' '.join(community)}] "
            f"large-community [{' '.join(large_community)}] "
            f"as-path [{as_path}] "
        )
        f.write(command + "\n")
        print(f"Sent to ExaBGP: {command}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <prefix>")
        sys.exit(1)

    prefix = sys.argv[1]
    as_path, community, large_community = get_as_path_and_community(prefix)

    # 添加 Community
    community.append(Config.EXABGP_COMMUNITY)
    broadcast_prefix_with_community(prefix, community, large_community, as_path)


if __name__ == "__main__":
    main()
