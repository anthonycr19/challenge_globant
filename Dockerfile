FROM python:3.13-slim

# Crear y usar el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . .

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto para FastAPI
EXPOSE 8000

# Comando por defecto
CMD ["sh", "-c", "sleep 10 && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
