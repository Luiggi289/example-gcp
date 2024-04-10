# [START dockerfile]
FROM tiangolo/uvicorn-gunicorn:python3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py /app/
COPY modelo.keras /app/

CMD gunicorn -b :$PORT main:app
# [END dockerfile]



