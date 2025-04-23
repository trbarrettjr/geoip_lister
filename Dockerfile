FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt /app
COPY app.py /app

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "app.py"]
