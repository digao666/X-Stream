FROM python:3.6

EXPOSE 5000

WORKDIR /
RUN mkdir -p /videos

WORKDIR /videos
COPY *.mp4 .

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY app.py /app

CMD python app.py
