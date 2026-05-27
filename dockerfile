# Utilizando uma imagem leve do Python
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Instala dependências do SO (necessárias para algumas libs como SQLite/C++)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código fonte
COPY . .

# Expõe a porta 5000 para acesso web
EXPOSE 5000

# Comando padrão (roda a interface web). Para rodar o CLI, basta mudar no docker run
CMD ["python", "app.py"]