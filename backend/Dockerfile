FROM python:3.9

WORKDIR /usr/src/backend

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
