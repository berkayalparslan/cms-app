FROM python:3.12

WORKDIR /app
COPY app/requirements.txt .
COPY app .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

RUN mkdir -p staticfiles
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]