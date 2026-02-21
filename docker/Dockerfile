FROM python:3.11-slim

WORKDIR /usr/src/app

COPY ../requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "sh","-c", "python exercises/$EXO" ]