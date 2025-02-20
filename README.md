# noname_docker
# 快速部署
1. 部署 docker （已部署则忽略）
```
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
```
2. 启动容器
```
docker run -d --restart=always -p 8089:8089 --name noname kevinstarry/noname
```
只允许某些 ip，或 ip 段（限制其他人访问 请自行替换允许的 ip，ip段，以英文逗号作为分隔）
```
docker run -d --restart=always -p 8089:8089 -e ALLOWED_IPS="192.168.1.1,192.168.0.0/16" --name noname kevinstarry/noname
```
3. 自动更新
已经内置每日凌晨三点更新（如需手动更新请执行下列命令）：
```
docker exec -it noname sh -c "cd /app/noname && git pull"
```
4. 移除(一键三连）
```
docker stop noname && docker rm noname && docker rmi noname 
```

# 进阶（参数配置）
ALLOWED_IPS: 原来就有的参数（默认 本机/容器 允许访问 不必额添加, 允许的ip只需要配置公网ip即可）

DISABLE_UPDATE:是否禁止定时更新，配置任意值都将禁止更新，不配置则默认开启定时更新任务

UPDATE_RIGHT_AWAY:是否立即更新，配置任意值都将在容器首次启动时候，立即更新一次

举例：不限制任何IP，禁止开启定时更新任务，首次启动时更新。
```
docker run -d -p 8089:8089 \
    --restart=always \
    -e ALLOWED_IPS="" \
    -e DISABLE_UPDATE="TRUE" \
    -e UPDATE_RIGHT_AWAY="TRUE" \
    --name noname kevinstarry/noname
```

举例：不限制任何IP，启用定时更新，首次启动容器不立即更新
```
docker run -d --restart=always -p 8089:8089 --name noname kevinstarry/noname
```
# 说明&体验
特点：单机，可以设置访问白名单，镜像仅略大于 noname 仓库大小，自动更新（省心）。

服务器长期（请勿恶意刷流量）：http://tencent.25527123.xyz:12004/

注意保存游戏配置文件，这样随时可以导入游戏配置。（选项->选项->其他->导出游戏配置）
# 祝福杀友
苟卡无道，今日起兵

三国杀 再玩十年也不腻
