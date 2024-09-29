from python:3.12-slim-buster

run apt install awscli -y

workdir /app
copy . /app
run pip install -r requirements.txt

entrypoint ["python3", "app.py"]