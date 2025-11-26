#!/bin/bash
# Script para criar um venv limpo no macOS com Python 3.12+
# Uso: ./make_venv.sh nome_do_ambiente

# Nome do ambiente (default: venv)
ENV_NAME=${1:-venv}

# Remove ambiente antigo se existir
if [ -d "$ENV_NAME" ]; then
  echo "Removendo ambiente existente: $ENV_NAME"
  rm -rf "$ENV_NAME"
fi

# Cria novo ambiente sem pip
echo "Criando novo ambiente virtual: $ENV_NAME"
python3 -m venv --without-pip "$ENV_NAME"

# Ativa ambiente
source "$ENV_NAME/bin/activate"

# Instala pip manualmente
echo "Baixando instalador do pip..."
curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
rm get-pip.py

# Atualiza pacotes básicos
echo "Atualizando pip, setuptools e wheel..."
pip install --upgrade pip setuptools wheel

echo "✅ Ambiente virtual '$ENV_NAME' pronto!"
