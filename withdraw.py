import sys

from config import Config

if len(sys.argv) != 2:
    print("Usage: python withdraw.py <prefix>")
    sys.exit(1)
prefix = sys.argv[1]
with open(Config.EXABGP_CMD, 'w') as f:
    # 构造 ExaBGP 的命令
    command = f"withdraw route {prefix}"
    f.write(command + '\n')
    print(f"Sent to ExaBGP: {command}")
