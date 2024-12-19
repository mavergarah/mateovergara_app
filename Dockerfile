# Utilizamos una imagen base de Python con herramientas para Django
FROM python:3.9-slim-buster

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo requirements.txt y lo instalamos
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiamos el resto de los archivos del proyecto
COPY . .

# Establecemos la variable de entorno para las configuraciones de Django
ENV PYTHONUNBUFFERED=1

# Exponemos el puerto donde se ejecutará el servidor de desarrollo
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
