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

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "web.main_score:app"]
