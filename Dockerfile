FROM python:3.10-slim

WORKDIR /api-task

RUN apt-get update && apt-get install -y --no-install-recommends \
libpq-dev \
netcat-openbsd \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

COPY /app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "./app/main.py"]
