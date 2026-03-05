# 无名杀 Docker 版
无名杀：https://github.com/libnoname/noname

个人精力实在是有限，Dockerfile 留给大家借鉴了，实在是杀不动了。
# 部署
准备Docker
```
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
```

启动容器 直接启动
```
docker run -d --restart=always -p 8089:8089 --name noname kevinstarry/noname
```
启动容器 限制IP启动（自行替换允许的ip，ip段，以英文逗号作为分隔）
```
docker run -d --restart=always -p 8089:8089 -e ALLOWED_IPS="192.168.1.1,192.168.0.0/16" --name noname kevinstarry/noname
```

完全移除
```
docker stop noname && docker rm noname && docker rmi noname 
```
# 祝福杀友
苟卡无道 今日起兵 三国杀 再玩十年也不腻

注意保存游戏配置文件，这样随时可以导入游戏配置。（选项->选项->其他->导出游戏配置）
