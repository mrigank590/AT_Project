FROM python:3.12.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
