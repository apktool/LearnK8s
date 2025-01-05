FROM python:3.14.0a3-bookworm
RUN mkdir /app
WORKDIR /app
COPY main.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["flask", "--app=main", "run", "--host=0.0.0.0", "--port=8000"]