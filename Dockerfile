FROM python:3.10.0

WORKDIR /home/

RUN echo "test9"

RUN git clone https://github.com/8azelnut/Django_SNS_PJ.git

WORKDIR /home/Django_SNS_PJ/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=config.settings.deploy && python manage.py migrate --settings=config.settings.deploy && gunicorn config.wsgi --env DJANGO_SETTINGS_MODULE=config.settings.deploy --bind 0.0.0.0:8000"]