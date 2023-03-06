FROM python:3.8-slim-buster

COPY . /Desktop/Library-MB/Ver_PK
WORKDIR /Desktop/Library-MB/Ver_PK

#COPY requirements.txt requirements.txt

ENV VIRTUAL_ENV=/opt/venv

RUN pip install -r requirements.txt
#RUN pip install bandit && pip install pycodestyle

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#COPY . .

RUN python3 test_lib.py

CMD [ "python3", "main.py", "host = 0.0.0.0" ]

