import grpc
import sys

from api import attribute_pb2
from api.gobgp_pb2 import ListPathRequest, Family
from api.gobgp_pb2_grpc import GobgpApiStub
from config import Config


# 假设你已经有了 gobgp 的 .proto 文件编译生成的 Python 代码：gobgp_pb2 和 gobgp_pb2_grpc

def get_as_path(prefix):
    # 创建与 GoBGP 的 gRPC 连接
    channel = grpc.insecure_channel(Config.GOBGP_URI)
    stub = GobgpApiStub(channel)

    # 构造请求，查询指定前缀的 AS 路径
    family = Family(afi=Family.AFI_IP, safi=Family.SAFI_UNICAST)  # IPv4 unicast
    request = ListPathRequest(table_type=0, family=family, prefixes=[{'prefix': prefix}])
    paths = list(stub.ListPath(request))
    if not paths:
        print(f"No path found for {prefix}")
        return ""
    else:
        path = paths[0].destination.paths[0]
        as_path = ""
        for attr in path.pattrs:
            if attr.Is(attribute_pb2.AsPathAttribute.DESCRIPTOR):
                as_path_attr = attribute_pb2.AsPathAttribute()
                attr.Unpack(as_path_attr)
                as_path = " ".join([Config.EXABGP_ASN, *map(str, as_path_attr.segments[0].numbers[1:])])
                break
    channel.close()
    return as_path


def broadcast_prefix_with_community(prefix, community, as_path):
    # 配置 ExaBGP 的命名管道或输入文件的路径
    with open(Config.EXABGP_CMD, 'w') as f:
        # 构造 ExaBGP 的命令
        command = f"announce route {prefix} next-hop self community [{community}] as-path [{as_path}]"
        f.write(command + '\n')
        print(f"Sent to ExaBGP: {command}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <prefix>")
        sys.exit(1)

    prefix = sys.argv[1]
    as_path = get_as_path(prefix)  # 获取 AS 路径的功能需要根据实际的 API 和返回的数据结构进行调整

    # 添加 Community
    community = Config.EXABGP_COMMUNITY
    broadcast_prefix_with_community(prefix, community, as_path)


if __name__ == "__main__":
    main()
