FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
COPY .env .
RUN pip install --no-cache-dir --timeout=100 -r requirements.txt

COPY src/ .

CMD ["python", "qrbot.py"]