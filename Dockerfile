FROM python:3.10.9-slim-buster

WORKDIR /app

COPY requirements/ /app/requirements

RUN pip install --no-cache-dir -r /app/requirements/dev.txt

COPY . .

EXPOSE 8000

CMD ["./scripts/start-dev.sh"]
