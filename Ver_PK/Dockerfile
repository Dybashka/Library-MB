FROM python:3.8-slim-buster

WORKDIR /Desktop/Library-MB/Ver_PK

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
CMD [ "python3", "main.py", "test_lib.py" ]

