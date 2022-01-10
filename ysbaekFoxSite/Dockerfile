FROM python:3.8.5
MAINTAINER ysbaek<ysbaekFox@gmail.com>
RUN pip3 install django
RUN pip3 install gunicorn
COPY . /usr/src/app/django
WORKDIR /usr/src/app/django
CMD ["gunicorn", "--bind", "0:8000", "ysbaekFoxSite.wsgi:application"]
EXPOSE 8000
