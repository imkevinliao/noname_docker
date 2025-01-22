# noname_docker
无名杀 个人制作 docker 版本。三国杀，再玩十年也不腻


不限制任何ip，所有人都可以访问：
```
docker run -d -p 8089:8089 --name noname kevinstarry/noname
```

只允许某些ip，或ip段：
```
docker run -d -p 8089:8089 -e ALLOWED_IPS="192.168.1.1,192.168.0.0/16" --name noname kevinstarry/noname
```


更新（如果 noname 更新了）：
```
docker exec -it noname sh -c "cd /app/noname && git pull"
```

# 说明
之所以自己制作，是因为尝试使用 noname 推荐的 dockerfile 时候并不符合我的预期。两个缺点：镜像太大，无法限制 ip。

限制 ip 是为了避免公网被恶意刷流量等，或者其他处于安全原因。

镜像大小只比 noname github 仓库稍微大一点点，一键部署完就可以直接上手玩了，不必去折腾，省心省力。

# 体验地址
服务器应该快要到期了，如果失效，请自行部署体验： http://38.147.170.202:8000/
