# Utiliser une image Python légère
FROM python:3.13.1-slim

# Mettre à jour les packages et installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    libnss3 \
    libatk1.0-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libxshmfence1 \
    fonts-liberation \
    libdbus-1-3 \
    libappindicator3-1 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libu2f-udev \
    && apt-get clean

# Installer Chromium et ChromeDriver
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*


# Vérifier les installations
#RUN google-chrome-stable --version
#RUN chromedriver --version



# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires, packages selenium, requests et dataframe_image
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Commande pour lancer le script
CMD ["python", "main.py"]
