FROM python:3.11.4-slim

WORKDIR /usr/src/app

COPY main.py .
COPY image.jpeg .

RUN pip3 install opencv-python-headless

CMD ["python3", "main.py"]
