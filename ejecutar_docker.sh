#!/bin/bash

# Nombre del archivo python (asegúrate que sea este el nombre exacto)
PYTHON_SCRIPT="DB-Browser-SQL-Lite-app.py"
TEMP_DIR="web_temp_folder"

echo "1. Creando directorio temporal..."
mkdir -p $TEMP_DIR

echo "2. Copiando archivos al directorio temporal..."
cp $PYTHON_SCRIPT $TEMP_DIR/

echo "3. Creando el Dockerfile..."
cat << _EOF_ > $TEMP_DIR/Dockerfile
FROM python:3.10-slim
RUN pip install flask flask_sqlalchemy werkzeug
COPY . /app
WORKDIR /app
# El contenedor expone el puerto que usa Flask
EXPOSE 7890
CMD ["python", "$PYTHON_SCRIPT"]
_EOF_

echo "4. Construyendo el contenedor Docker..."
cd $TEMP_DIR
docker build --no-cache -t imagen_item4 .
echo "5. Iniciando el contenedor en el puerto 7529..."

# Mapeamos el puerto solicitado 7529 al 7890 que usa tu script
docker run -d -p 7529:7890 --name contenedor_instancia_4 imagen_item4

echo "6. Comprobando ejecución..."
sleep 2
docker ps -f name=contenedor_instancia_4