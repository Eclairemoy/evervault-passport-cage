FROM ubuntu:20.04
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    && apt-get install python3.9 -y \
    && apt-get install python3-pip -y \
    && apt-get clean \
    && apt-get autoremove

ADD . /home/App
WORKDIR /home/App

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=server.py

EXPOSE 8008

ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8008"]