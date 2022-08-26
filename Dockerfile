FROM python:3.9-alpine3.13
LABEL maintainer="cherrytechnologies.io"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

ARG DEV=flase

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true"]; \
      then /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    adduser \
	  --disabled-password \
	  --no-create-home \
	  django-user

#COPY ./app /app
#
#WORKDIR /app

EXPOSE 8000

ENV PATH="/py/bin:$PATH"

USER django-user
