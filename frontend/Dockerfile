# Use official Python 3.12 slim image
FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir dash requests python-dotenv

EXPOSE 8050

CMD [ "gunicorn", "--timeout=300", "--workers=1", "--threads=1", "-b 0.0.0.0:8050", "main:server"]
