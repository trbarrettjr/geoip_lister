FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt /app
COPY app.py /app
COPY GeoLite2-ASN.mmdb /app

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "app.py"]
