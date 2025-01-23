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

只允许某些 ip，或 ip 段：（请勿直接使用该命令，自行替换允许的 ip，ip段，以英文逗号作为分隔）
```
docker run -d -p 8089:8089 -e ALLOWED_IPS="192.168.1.1,192.168.0.0/16" --name noname kevinstarry/noname
```

3. 更新：
已经内置了 UTC 时间每日凌晨三点更新定时任务，当然也可以选择手动更新：
```
docker exec -it noname sh -c "cd /app/noname && git pull"
```

4. 移除(一键三连）
```
docker stop noname && docker rm noname && docker rmi noname 
```

# 说明
noname 的 Dockerfile

1.镜像太大 2.无法限制ip。

自制的镜像只比 noname github 仓库稍微大一点，一键部署完就可以直接上手玩了，免折腾。

如果服务器到期失效，请自行部署体验。

三国杀，再玩十年也不腻。



