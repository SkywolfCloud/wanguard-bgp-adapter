# wanguard-bgp-adapter

一个对接代理，用来把GoBGP里的前缀导入到wanguard，同时附带接收wanguard调用的脚本

## ENV
可写在.env也可通过环境变量传入
- `GOBGP_URI`: GoBGP的API地址，默认为`localhost:50051`
- `WANGUARD_BASE_URI`: wanguard的API地址，默认为`http://localhost/wanguard-api`
- `WANGUARD_USERNAME`: wanguard的用户名，默认为`admin`
- `WANGUARD_PASSWORD`: wanguard的密码，默认为`admin`
- `WANGUARD_IP_ZONE`: wanguard的IP区域，默认为`IP Zone`
- `EXABGP_CMD`: ExaBGP的命令文件路径，默认为`/run/exabgp/exabgp.in`
- `EXABGP_ASN`: ExaBGP的ASN，默认为`65002`，用于重写AS Path
- `EXABGP_COMMUNITY`: ExaBGP发送时附带的Community
- `LOG_LEVEL`: 日志级别，默认为`INFO`

## communities.yaml
用来定义GoBGP的community和wanguard的ip group和thresholds template的对应关系
Example: 
```yaml
template:
  "7720:65535:998": "Thresholds Customer (Simple, 9G)" # Wanguard 内 Thresholds Template 的名字
  "7720:65535:9990": "Thresholds Customer (Simple, 9G)" # Wanguard 内 IP Group 的名字
ip_group:
  "7720:65535:998": "No Protection"
  "7720:65535:999": "Protection"
```
此处仅以large community为例，该项目依然支持普通community，应该不支持extended community（未测试）
## 使用方法
### GoBGP 对接
1. 安装GoBGP，并写好配置文件
2. 编写 communities.yaml
3. 编写 .env
4. 运行 `python3 gobgp.py`
5. 完成！
### Wanguard 调用脚本（假设使用exabgp）
1. 编写 .env
2. 安装 pipx，详情请看 https://pipx.pypa.io/stable/
3. 运行 `sudo -u andrisoft PIPX_HOME=/opt/pipx PIPX_BIN_DIR=/usr/local/bin pipx install poetry` 此处路径为示例，请根据自己的情况修改，不使用默认参数目的是使得wanguard的andrisoft账户也可使用。
4. 在项目目录下运行 `sudo -u andrisoft poetry install`
5. 注意更改项目权限，使得andrisoft账户可读取并运行
6. 假设项目在 `/opt/wanguard-bgp-adapter`，那么wanguard 控制台的Response自定义脚本位置为`/usr/bin/sh -c "cd /opt/wanguard-bgp-adapter/ ; /usr/local/bin/poetry run python /opt/wanguard-bgp-adapter/advertise.py {prefix}"` 和 
`/usr/bin/sh -c "cd /opt/wanguard-bgp-adapter/ ; /usr/local/bin/poetry run python /opt/wanguard-bgp-adapter/withdraw.py {prefix}"`
7. 完成！
