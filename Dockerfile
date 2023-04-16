FROM python:3.10.9-slim-buster

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt clean && \
    rm -rf /var/cache/apt/*

WORKDIR /app

COPY requirements/ /app/requirements

RUN pip install --no-cache-dir -r /app/requirements/dev.txt

COPY . .
ENV PATH "$PATH:/scripts"

# RUN chmod +x ./scripts/*

EXPOSE 8000

CMD ["./scripts/start-dev.sh"]
