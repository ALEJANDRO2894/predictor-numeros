#!/bin/bash
# Script para ejecutar el predictor localmente

echo "🎰 Iniciando Predictor de Lotería v2.0"
echo "========================================"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no está instalado"
    exit 1
fi

# Verificar dependencias
echo "📦 Verificando dependencias..."
python3 -m pip install -q -r requirements.txt

# Ejecutar predictor
echo ""
echo "🚀 Ejecutando predictor..."
echo ""
python3 lottery_predictor_v2.py

echo ""
echo "✅ Ejecución completada!"
echo ""
echo "📁 Archivos generados:"
echo "  - resultados.json"
echo "  - lottery_prediction_analysis.png"
