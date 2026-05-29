import json
from datetime import datetime

def generar_reporte_html(resultados):
    """Genera un reporte HTML a partir de los resultados JSON"""
    
    html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎰 Predicción de Lotería - Reporte</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 20px;
            text-align: center;
        }}
        
        header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .prediction-box {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin: 20px 0;
            text-align: center;
        }}
        
        .prediction-box h2 {{
            font-size: 1.2em;
            margin-bottom: 10px;
            opacity: 0.9;
        }}
        
        .prediction-number {{
            font-size: 3.5em;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        .metrics {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 30px;
        }}
        
        .metric-card {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #667eea;
        }}
        
        .metric-card h3 {{
            color: #667eea;
            font-size: 0.9em;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}
        
        .metric-value {{
            font-size: 1.8em;
            font-weight: bold;
            color: #333;
        }}
        
        .metric-subtitle {{
            font-size: 0.85em;
            color: #666;
            margin-top: 5px;
        }}
        
        .info-section {{
            background: #f0f2f5;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }}
        
        .info-section h3 {{
            color: #333;
            margin-bottom: 15px;
            font-size: 1.2em;
        }}
        
        .info-item {{
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #ddd;
        }}
        
        .info-item:last-child {{
            border-bottom: none;
        }}
        
        .info-label {{
            color: #666;
            font-weight: 500;
        }}
        
        .info-value {{
            color: #333;
            font-weight: bold;
        }}
        
        .disclaimer {{
            background: #fff3cd;
            border: 2px solid #ffc107;
            color: #856404;
            padding: 20px;
            border-radius: 10px;
            margin-top: 30px;
        }}
        
        .disclaimer h4 {{
            margin-bottom: 10px;
            font-size: 1.1em;
        }}
        
        .disclaimer ul {{
            list-style-position: inside;
            line-height: 1.8;
        }}
        
        footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #ddd;
        }}
        
        @media (max-width: 768px) {{
            .metrics {{
                grid-template-columns: 1fr;
            }}
            
            header h1 {{
                font-size: 1.8em;
            }}
            
            .prediction-number {{
                font-size: 2.5em;
            }}
            
            .content {{
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎰 Predictor de Lotería</h1>
            <p>Machine Learning Ensemble v2.0</p>
        </header>
        
        <div class="content">
            <div class="info-section">
                <h3>📋 Información de la Predicción</h3>
                <div class="info-item">
                    <span class="info-label">Fecha de predicción:</span>
                    <span class="info-value">{resultados.get('fecha_prediccion', 'N/A')}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Fecha de generación:</span>
                    <span class="info-value">{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Registros históricos:</span>
                    <span class="info-value">599</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Período analizado:</span>
                    <span class="info-value">05/01/2018 - 22/05/2026</span>
                </div>
            </div>
            
            <h2 style="margin-top: 40px; color: #333;">🎯 Predicciones</h2>
            
            <div class="prediction-box">
                <h2>NÚMERO 1 (Principal)</h2>
                <div class="prediction-number">{resultados.get('numero_1', '????')}</div>
            </div>
            
            <div class="prediction-box">
                <h2>NÚMERO 2 (Secundario)</h2>
                <div class="prediction-number">{resultados.get('numero_2', '????')}</div>
            </div>
            
            <h2 style="margin-top: 40px; color: #333;">📊 Métricas de Calidad</h2>
            
            <div class="metrics">
                <div class="metric-card">
                    <h3>Número 1 - R² Score</h3>
                    <div class="metric-value">{resultados.get('r2_numero_1', 0)*100:.2f}%</div>
                    <div class="metric-subtitle">Calidad del ajuste del modelo</div>
                </div>
                <div class="metric-card">
                    <h3>Número 1 - MAE</h3>
                    <div class="metric-value">{resultados.get('mae_numero_1', 0):.2f}</div>
                    <div class="metric-subtitle">Error medio absoluto</div>
                </div>
                <div class="metric-card">
                    <h3>Número 2 - R² Score</h3>
                    <div class="metric-value">{resultados.get('r2_numero_2', 0)*100:.2f}%</div>
                    <div class="metric-subtitle">Calidad del ajuste del modelo</div>
                </div>
                <div class="metric-card">
                    <h3>Número 2 - MAE</h3>
                    <div class="metric-value">{resultados.get('mae_numero_2', 0):.2f}</div>
                    <div class="metric-subtitle">Error medio absoluto</div>
                </div>
            </div>
            
            <div class="info-section" style="margin-top: 30px;">
                <h3>📈 Estadísticas Históricas</h3>
                <div class="info-item">
                    <span class="info-label">Media histórica Número 1:</span>
                    <span class="info-value">{resultados.get('media_numero_1', 'N/A')}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Media histórica Número 2:</span>
                    <span class="info-value">{resultados.get('media_numero_2', 'N/A')}</span>
                </div>
            </div>
            
            <div class="disclaimer">
                <h4>⚠️ Disclaimer Importante</h4>
                <ul>
                    <li><strong>Lotería = Proceso ALEATORIO</strong> (imposible predecir 100%)</li>
                    <li>Machine Learning busca <strong>patrones en el pasado</strong></li>
                    <li><strong>NO GARANTIZA RESULTADOS</strong> en sorteos reales</li>
                    <li>Úsalo <strong>SOLO con fines educativos y de investigación</strong></li>
                    <li>Los números de lotería <strong>NO tienen memoria estadística</strong></li>
                </ul>
            </div>
        </div>
        
        <footer>
            <p>🤖 Generado automáticamente por Predictor de Lotería v2.0</p>
            <p style="margin-top: 10px; font-size: 0.9em;">
                <strong>GitHub:</strong> 
                <a href="https://github.com/ALEJANDRO2894/predictor-numeros" style="color: #667eea; text-decoration: none;">
                    ALEJANDRO2894/predictor-numeros
                </a>
            </p>
        </footer>
    </div>
</body>
</html>
"""
    
    return html_content

# Cuando se ejecuta el script principal, también genera HTML
if __name__ == "__main__":
    # Ejemplo de uso
    try:
        with open('resultados.json', 'r') as f:
            resultados = json.load(f)
        
        html = generar_reporte_html(resultados)
        
        with open('reporte.html', 'w', encoding='utf-8') as f:
            f.write(html)
        
        print("✅ Reporte HTML generado: reporte.html")
    except FileNotFoundError:
        print("❌ No se encontró resultados.json")
