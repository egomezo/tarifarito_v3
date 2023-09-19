# Usamos la imagen base de Python 3.7.7
FROM python:3.7.7

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Actualizar paquetes
RUN python -m pip install --upgrade pip

# Copiamos el archivo requirements.txt al directorio de trabajo
COPY ./Backend/. .

# Instalamos las dependencias
RUN pip3 install -r requirements.txt

# Actualizar paquetes
RUN python -m pip install --upgrade pip

# Set the FLASK_ENV environment variable to "development"
ENV FLASK_APP=app
ENV FLASK_ENV=development

# Exponemos el puerto 5000 en el contenedor
EXPOSE 5063

# Command to run the Flask app
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5063"]