FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV FLASK_APP=app.py
EXPOSE 8080

# Use Gunicorn to serve the Flask application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]