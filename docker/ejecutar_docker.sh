#!/bin/bash

#!/bin/bash

# Variables
TEMP_DIR="../web_temp_folder"
APP_SCRIPT="../scripts/DB-Browser-SQL-Lite-app.py"
DB_FILE="../scripts/usuarios.db"

echo "1. Creando directorio temporal..."
mkdir -p $TEMP_DIR

echo "2. Copiando archivos al directorio temporal..."
cp "$APP_SCRIPT" "$TEMP_DIR/"
cp "$DB_FILE" "$TEMP_DIR/"

echo "3. Creando el Dockerfile..."
# Usamos el nombre directo del archivo para evitar fallos de variables de bash
cat <<EOF > $TEMP_DIR/Dockerfile
FROM python:3.10-slim
WORKDIR /app
RUN pip install flask flask_sqlalchemy werkzeug
COPY . .
# El puerto interno de tu app según el Ítem 2 es 7890
EXPOSE 7890
CMD ["python", "DB-Browser-SQL-Lite-app.py"]
EOF

echo "4. Construyendo el contenedor Docker..."
# Entramos a la carpeta para que el contexto de build sea el correcto
cd $TEMP_DIR
docker build --no-cache -t imagen_item4 .

echo "5. Iniciando el contenedor en el puerto 7529..."
# Borramos cualquier intento fallido anterior para evitar errores de nombre en uso
docker rm -f contenedor_instancia_4 2>/dev/null || true

# IMPORTANTE: Mapeamos el puerto solicitado 7529 al 7890 de la app
docker run -d -p 7529:7890 --name contenedor_instancia_4 imagen_item4

echo "6. Comprobando ejecución..."
sleep 2
docker ps -f name=contenedor_instancia_4