FROM python:3.10.14-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update

WORKDIR /usr/src

COPY . .
RUN pip install -r requirements.txt

CMD ["fastapi", "run", "/usr/src/outline/Server.py"]
