FROM python:3.11

WORKDIR /app

# Copia los archivos de tu proyecto
COPY . .

# Crea el entorno virtual
ENV VIRTUAL_ENV=/app/.venv_docker
RUN python3.11 -m venv $VIRTUAL_ENV

# Ajusta el PATH para usar el entorno virtual
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Actualiza pip e instala las dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar tu aplicación
CMD ["reflex", "run", "--env", "prod", "--backend-only"]
