FROM python:3.8-slim-buster

WORKDIR /Desktop/Library-MB/Ver_PK

COPY requirements.txt requirements.txt

ENV VIRTUAL_ENV=/opt/venv

RUN pip install -r requirements.txt
RUN pip install bandit && pip install pycodestyle

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . .

RUN bandit check.py 
RUN pycodestyle check.py 

CMD [ "python3", "./check.py", "host = 0.0.0.0" ]
