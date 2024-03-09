FROM python:3.12-slim

LABEL "app"="wog1312"
LABEL "role"="scoreserver"

EXPOSE 8777

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN mkdir aux/ 
COPY web/* /app/
COPY aux/* /app/aux/

RUN python -m pip install -r web-requirements.txt

CMD ["python", "scoreserver.py"]
