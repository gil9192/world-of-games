FROM python:3.9.19-bookworm

WORKDIR /app

COPY entrypoint.sh /usr/local/bin/
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8777

ENTRYPOINT ["entrypoint.sh"]
