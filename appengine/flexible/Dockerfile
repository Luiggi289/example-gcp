# [START dockerfile]
FROM tiangolo/uvicorn-gunicorn:python3.9-slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY modelo.keras .

CMD gunicorn -b :$PORT main:app
# [END dockerfile]



