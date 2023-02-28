FROM python:3.8.5-alpine
COPY . /app
WORKDIR /app
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev rust cargo
RUN pip install -U pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["rest.py"]