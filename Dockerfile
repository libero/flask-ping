FROM python:3.7.4-slim

WORKDIR /srv/app

COPY requirements.txt .

RUN pip install --no-cache -r requirements.txt \
    && rm -rf /tmp/*

COPY . .

RUN pip install -e .

CMD "pytest -v"
