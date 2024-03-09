FROM python:3.12-slim


LABEL "app"="wog1312"
LABEL "role"="scoreserver"


EXPOSE 8777

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
RUN mkdir aux/ 
COPY web/* /app/
COPY aux/* /app/aux/


CMD ["python", "scoreserver.py"]
