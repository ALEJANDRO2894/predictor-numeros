# 🎰 Predictor de Números de Lotería - Machine Learning v2.0

Predictor avanzado de números de lotería usando **Ensemble Machine Learning** con GitHub Actions para automatización.

## ✨ Características

### 🤖 Machine Learning Avanzado
- **6 Modelos Ensemble:**
  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  - Random Forest (200 árboles)
  - Gradient Boosting (200 estimadores)
  - Red Neuronal (MLP)

- **Votación Ponderada:** Combina predicciones con pesos optimizados

### 📊 Feature Engineering
- Media móvil (4, 8, 12 semanas)
- Volatilidad histórica
- Cambios vs período anterior
- Lag features (valores anteriores)
- Características temporales (mes, semana, día)

### 📈 Métricas de Calidad
- R² (Coeficiente de determinación)
- MAE (Error Medio Absoluto)
- Validación cruzada

### 🔄 Automatización GitHub Actions
- ⏰ Ejecución automática cada viernes
- 🚀 Ejecución manual bajo demanda
- 📊 Generación de gráficos
- 💾 Almacenamiento de resultados
- 📤 Commit automático de resultados

## 🚀 Instalación Local

### Requisitos
- Python 3.8+
- pip

### Setup
```bash
# Clonar repositorio
git clone https://github.com/ALEJANDRO2894/predictor-numeros.git
cd predictor-numeros

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar predictor
python lottery_predictor_v2.py
```

## 📋 Uso

### Ejecución Local
```bash
python lottery_predictor_v2.py
```

**Genera:**
- `resultados.json` - Predicciones en formato JSON
- `lottery_prediction_analysis.png` - Gráficos de análisis (4 subgráficos)

### Ejecución Automatizada (GitHub Actions)
1. Configurada para ejecutarse **cada viernes a las 10:00 UTC**
2. O manualmente desde: `Actions` → `🎰 Predictor de Lotería` → `Run workflow`
3. Resultados guardados automáticamente en artifacts

## 📊 Salida Típica

```
================================================================================
🤖 PREDICTOR DE LOTERÍA v2.0 - ENSEMBLE MACHINE LEARNING AVANZADO
================================================================================

📊 DATOS PROCESADOS: 599 registros históricos
📅 Período: 05/01/2018 a 22/05/2026
⏱️  Rango temporal: ~3034 días

📍 NÚMERO 1 (Principal 0-9999)
  📈 Media histórica: 5,097
  🎯 PREDICCIÓN: 5,236
  📊 Calidad del modelo (R²): 0.4782 (47.82%)
  📏 Error Medio Absoluto: 1,847.35

📍 NÚMERO 2 (Secundario 0-399)
  📈 Media histórica: 173
  🎯 PREDICCIÓN: 186
  📊 Calidad del modelo (R²): 0.3921 (39.21%)
  📏 Error Medio Absoluto: 84.67

🎰 RESULTADO FINAL
┌─────────────────────────────────────┐
│  🎯 NÚMERO 1: 5,236            │
│  🎯 NÚMERO 2:   186              │
└─────────────────────────────────────┘
```

## 📁 Estructura de Archivos

```
predictor-numeros/
├── .github/
│   └── workflows/
│       └── lottery-prediction.yml    # Workflow de GitHub Actions
├── lottery_predictor_v2.py          # Script principal
├── resultados.json                  # Últimas predicciones
├── lottery_prediction_analysis.png  # Últimos gráficos
├── requirements.txt                 # Dependencias
└── README.md                        # Este archivo
```

## ⚠️ Disclaimer Importante

- **Lotería = Proceso ALEATORIO** (imposible predecir 100%)
- Machine Learning busca **patrones en el pasado**
- **NO GARANTIZA RESULTADOS** en sorteos reales
- Úsalo **SOLO con fines educativos y de investigación**
- Los números de lotería **NO tienen memoria estadística**

## 📊 Gráficos Generados

1. **Número 1 - Histórico y Predicción**
   - Línea azul: datos históricos
   - Línea verde: media
   - Línea roja: predicción

2. **Número 2 - Histórico y Predicción**
   - Similar al anterior

3. **Distribución del Número 1**
   - Histograma de frecuencias
   - Muestra patrón de distribución

4. **Distribución del Número 2**
   - Histograma de frecuencias

## 🔧 Configuración de GitHub Actions

El workflow está configurado para:

```yaml
# Ejecución automática
- schedule: '0 10 * * 5'  # Viernes a las 10:00 UTC

# Ejecución manual
- workflow_dispatch

# Ejecución en push
- push: main
```

### Acceder a Resultados
1. Ir a `Actions` en el repositorio
2. Seleccionar el workflow ejecutado
3. Descargar artifacts: `predicción-resultados`

## 📈 Interpretación de Métricas

| Métrica | Significado | Rango |
|---------|------------|-------|
| **R²** | % de varianza explicada | 0-1 (mayor es mejor) |
| **MAE** | Error promedio absoluto | 0-∞ (menor es mejor) |
| **Predicción** | Estimación basada en patrones | Número resultado |

## 🎯 Próximas Mejoras

- [ ] Análisis de ciclos periódicos
- [ ] Simulaciones Monte Carlo
- [ ] Comparación histórica de predicciones
- [ ] Dashboard web interactivo
- [ ] Notificaciones por email
- [ ] API REST para consultas

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👤 Autor

**ALEJANDRO2894** - GitHub

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

**Última actualización:** 2026-05-29
**Versión:** 2.0.0
