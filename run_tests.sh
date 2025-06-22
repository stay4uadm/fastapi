#!/bin/bash

echo "🚀 Iniciando testes do FastAPI..."
echo ""

# Instalar dependências se necessário
echo "📦 Verificando dependências..."
pip install -r requirements.txt

echo ""
echo "🧪 Executando testes..."
pytest -v --tb=short

echo ""
echo "📊 Executando testes com cobertura..."
pytest --cov=main --cov-report=html --cov-report=term

echo ""
echo "🎯 Relatório de cobertura gerado em htmlcov/"
echo "✅ Testes concluídos!" 