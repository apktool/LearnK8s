FROM python:3.14.0a3-bookworm
RUN mkdir /app
WORKDIR /app
COPY main.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt