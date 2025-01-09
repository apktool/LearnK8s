FROM python:3.14.0a3-bookworm
RUN mkdir /app
WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["flask", "--app=app", "run", "--host=0.0.0.0", "--port=8080"]