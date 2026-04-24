FROM python:3.10-slim
RUN pip install flask flask_sqlalchemy werkzeug
COPY . /app
WORKDIR /app
# El contenedor expone el puerto que usa Flask
EXPOSE 7890
CMD ["python", "DB-Browser-SQL-Lite-app.py"]
