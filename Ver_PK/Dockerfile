FROM python:3.8-slim-buster

WORKDIR /Desktop/Library-MB/Ver_PK

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN pip install bandit && pip install pycodestyle
RUN bandit --exit-zero main.py &&  pycodestyle --ignore=E501 main.py
RUN python3 unit_tests.py

ENTRYPOINT ["bash"]
