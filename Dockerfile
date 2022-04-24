FROM python 3.10.4
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# RUN mkdir /app

RUN pip install --upgrade pip
RUN python -m pip --no-cache-dir install -r requirements.txt

COPY ./comics_store /app/
COPY requirements.txt /app/
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]