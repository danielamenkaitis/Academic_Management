FROM python:3.11-slim

WORKDIR /app

# Copiar requirements primeiro para otimizar cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da API
COPY ./app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
