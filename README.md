# noname_docker
# 快速部署
1. 部署 docker （已部署则忽略）
```
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
```
2. 启动容器
不限制ip，所有人都可以访问：
```
docker run -d -p 8089:8089 --name noname kevinstarry/noname
```
只允许某些 ip，或 ip 段：（请自行替换允许的 ip，ip段，以英文逗号作为分隔）
```
docker run -d -p 8089:8089 -e ALLOWED_IPS="192.168.1.1,192.168.0.0/16" --name noname kevinstarry/noname
```
3. 访问
你部署服务器的公网 IP 地址 + 端口 http://ip:8089 如果是本地则是：http://localhost:8089 或者 http://127.0.0.1:8089
4. 更新：
已经内置每日凌晨三点更新，通常无需手动更新：
```
docker exec -it noname sh -c "cd /app/noname && git pull"
```
5. 移除(一键三连）
```
docker stop noname && docker rm noname && docker rmi noname 
```

# 进阶（参数配置）
新版本更新了一些控制参数：

ALLOWED_IPS:原来就有的参数（默认 本机/容器 允许访问 不必额添加, 允许的ip只需要配置公网ip即可）

DISABLE_UPDATE:是否禁止定时更新，配置任意值都将禁止更新，不配置则默认开启定时更新任务

UPDATE_RIGHT_AWAY:是否立即更新，配置任意值都将在容器首次启动时候，立即更新一次

举例：不限制任何IP，禁止开启定时更新任务，首次启动时更新。（注，当参数无需配置时候可以不填，这里这是为了展示所有参数）
```
docker run -d -p 8089:8089 \
    -e ALLOWED_IPS="" \
    -e DISABLE_UPDATE="TRUE" \
    -e UPDATE_RIGHT_AWAY="TRUE" \
    --name noname kevinstarry/noname
```

举例：不限制任何IP，启用定时更新，首次启动容器不立即更新
```
docker run -d -p 8089:8089 --name noname kevinstarry/noname
```
# 说明
noname 的 Dockerfile 镜像太大 而且 无法限制ip

这个镜像只比 noname github 仓库大一点，一键部署完就可以直接上手玩了，免折腾。

如果服务器（野草云香港）到期失效，请自行部署体验：http://38.147.170.202:8089/

制作该镜像的目的是不希望花太多时间折腾，开箱即用，时间应该花在玩上面，快乐无需等待。

# 祝福杀友
注意保存游戏配置文件，这样随时可以导入游戏配置。（选项->选项->其他->导出游戏配置）

苟卡无道，今日起兵

三国杀，再玩十年也不腻。



