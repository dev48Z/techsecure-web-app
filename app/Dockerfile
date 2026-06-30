FROM python:3.10-slim

WORKDIR /app

# Sécurité système : On met à jour les paquets pour éviter les vulnérabilités courantes
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 5000

CMD ["python", "app.py"]
