import logging
import os
import subprocess
from datetime import datetime, timedelta
from ipaddress import ip_address, ip_network
from logging.handlers import RotatingFileHandler

from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

# 挂载静态文件目录
app.mount("/", StaticFiles(directory="/app/noname", html=True), name="static")


# 路由直接返回 index.html
@app.get("/")
async def root():
    return FileResponse("/app/noname/index.html")

# 默认定时更新
disable_update = os.getenv('DISABLE_UPDATE')
if not disable_update:
    cron_job = "0 3 * * * cd /app/noname && git pull >> /app/git_pull.log 2>&1\n"
    try:
        with open("/etc/crontabs/root", "a") as cron_file:
            cron_file.write(cron_job)
        print("Cron job added for git pull.")
    except Exception as e:
        print(f"Error adding cron job: {e}")
else:
    print("No update needed, skipping cron job setup.")

# 立即更新
update_now = os.getenv('UPDATE_RIGHT_AWAY')
if update_now:
    try:
        subprocess.run(['git', 'pull'], cwd='/app/noname', check=True)
        print("Code updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during git pull: {e}")
else:
    print("No update needed.")
    
# 访问ip记录与限制
ALLOWED_IPS = os.getenv("ALLOWED_IPS")
ALLOWED_ALL = False
if not ALLOWED_IPS:  # 不填的情况下默认是空，即允许所有
    ALLOWED_ALL = True

ALLOWED_IPS = ALLOWED_IPS.split(",") + ["localhost", "127.0.0.1", "172.17.0.0/16"]
# 设置最大日志文件大小和备份数量
log_file = "/app/log.txt"
max_log_size = 10 * 1024 * 1024  # 10MB
backup_count = 3  # 保留3个旧日志文件
# 创建一个 RotatingFileHandler
handler = RotatingFileHandler(log_file, maxBytes=max_log_size, backupCount=backup_count)
handler.setLevel(logging.DEBUG)

# 切换ip才显示，不然会频繁打印
client_ip_previous = None
client_time_previous = datetime.now()


@app.middleware("http")
async def check_ip(request: Request, call_next):
    # 获取客户端 IP 地址
    client_ip = request.headers.get("X-Forwarded-For", "").split(",")[0] or request.client.host
    user_agent = request.headers.get("User-Agent", "Unknown")
    request_method = request.method
    request_url = str(request.url)
    current_time = datetime.now().strftime("%Y%m%d %H:%M:%S")
    log_message = f"{current_time} IP: {client_ip}, User-Agent: {user_agent}, Method: {request_method}, URL: {request_url}\n"
    global client_ip_previous
    global client_time_previous
    client_time = datetime.now()
    time_diff = client_time - client_time_previous
    is_record = False
    if time_diff > timedelta(minutes=10):  # 每十分钟记录一次ip请求，或者更换ip时记录
        is_record = True
    if client_ip_previous != client_ip or is_record:
        client_ip_previous = client_ip
        client_time_previous = client_time
        with open(log_file, "a") as f:
            f.write(log_message)
        print(log_message)
    
    allowed = False
    for allowed_ip in ALLOWED_IPS:
        allowed_ip = allowed_ip.strip()
        if "/" in allowed_ip:  # 检查是否是 IP 段
            if ip_address(client_ip) in ip_network(allowed_ip):
                allowed = True
                break
        elif client_ip == allowed_ip:  # 精确匹配
            allowed = True
            break
    
    if ALLOWED_ALL:
        allowed = True
    
    if not allowed:
        raise HTTPException(status_code=403, detail="Forbidden: Access denied")
    
    response = await call_next(request)
    return response
