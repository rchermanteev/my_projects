FROM python:3.7.3-alpine3.9

WORKDIR /var/www/app
ADD . /var/www/app

RUN pip3 install -r /var/www/app/requirements.txt

ENTRYPOINT ["sh", "./entrypoint.sh", "run"]
