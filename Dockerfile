FROM python:3.11.9

ENV CONFIG_ENV=config.Development

RUN echo "CONFIG_ENV=${CONFIG_ENV}"

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["gunicorn","-w","4","app:create_app()","-b","0.0.0.0:8000"]    