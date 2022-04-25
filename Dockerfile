FROM python:3.10.4
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip

COPY ./comics_store /app/
COPY ./requirements.txt /app/
WORKDIR /app

RUN python -m pip --no-cache-dir install -r requirements.txt

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]