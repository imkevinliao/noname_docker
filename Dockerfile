FROM python:3.9-alpine

WORKDIR /app

COPY ./main.py ./requirements.txt ./

RUN apk add --no-cache git tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    pip install --no-cache-dir -r requirements.txt && \
    git clone -b master --depth=1 https://github.com/libnoname/noname.git /app/noname && \
    apk del tzdata

ENV ALLOWED_IPS=""
ENV DISABLE_UPDATE=""
ENV UPDATE_RIGHT_AWAY=""

EXPOSE 8089

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8089"]
