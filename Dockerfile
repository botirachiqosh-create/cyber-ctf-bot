FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    openssh-client \
    netcat-traditional \
    socat \
    procps \
    xxd \
    curl \
    wget \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
RUN chmod +x /app/entrypoint.sh /app/ctf_cli.py

EXPOSE 8080 2222

CMD ["/bin/bash", "/app/entrypoint.sh"]
