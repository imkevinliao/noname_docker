# noname_docker
部署：

1. 部署 docker （已部署则忽略）

```
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
```

2. 启动容器

不限制任何ip，所有人都可以访问：
```
docker run -d -p 8089:8089 --name noname kevinstarry/noname
```

只允许某些ip，或ip段：
```
docker run -d -p 8089:8089 -e ALLOWED_IPS="192.168.1.1,192.168.0.0/16" --name noname kevinstarry/noname
```

3. 更新（同步noname）：
```
docker exec -it noname sh -c "cd /app/noname && git pull"
```

# 说明
noname 的 Dockerfile 时候并不符合我的预期，所以自制。

两个缺点：1.镜像太大 2.无法限制ip。

镜像只比 noname github 仓库稍微大一点，一键部署完就可以直接上手玩了，免去折腾，省心省力。
# 体验地址
服务器应该快要到期了，如果失效，请自行部署体验： http://38.147.170.202:8000/

三国杀，再玩十年也不腻。



