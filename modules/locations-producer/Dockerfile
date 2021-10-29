FROM python:3.7-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache gcc g++ musl-dev linux-headers geos libc-dev postgresql-dev
RUN pip3 install --upgrade pip && \
        pip3 install -r requirements.txt

EXPOSE 5005/tcp

CMD ["python3", "main.py"]