# 🌱 Calculadora de Emisiones de CO2 - Papel

Una aplicación web interactiva para calcular y visualizar las emisiones de CO2 asociadas con el consumo de papel.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.27%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 Contenido
- [🌱 Calculadora de Emisiones de CO2 - Papel](#-calculadora-de-emisiones-de-co2---papel)
  - [📋 Contenido](#-contenido)
  - [📝 Descripción](#-descripción)
  - [✨ Características](#-características)
    - [🔢 Cálculos](#-cálculos)
    - [📊 Visualizaciones](#-visualizaciones)
    - [💡 Recomendaciones](#-recomendaciones)
  - [🚀 Instalación](#-instalación)
  - [💻 Uso](#-uso)
  - [📁 Estructura del Proyecto](#-estructura-del-proyecto)
  - [🧮 Metodología](#-metodología)
    - [Factores de Emisión](#factores-de-emisión)
    - [Pesos Estándar](#pesos-estándar)
    - [Cálculos](#cálculos)
  - [👥 Contribuir](#-contribuir)
    - [Áreas de Mejora](#áreas-de-mejora)
  - [📄 Licencia](#-licencia)
  - [🙏 Agradecimientos](#-agradecimientos)

## 📝 Descripción

Esta aplicación permite a los usuarios calcular las emisiones de CO2 generadas por su consumo de papel, proporcionando:
- Cálculos precisos basados en factores de emisión estándar
- Visualizaciones interactivas
- Comparaciones con actividades cotidianas
- Recomendaciones para reducir emisiones

## ✨ Características

### 🔢 Cálculos
- Soporte para diferentes tipos de papel:
  - Papel nuevo (virgen)
  - Papel reciclado
  - Papel mixto

### 📊 Visualizaciones
- Gráficos de barras comparativos
- Métricas en tiempo real
- Equivalencias ambientales

### 💡 Recomendaciones
- Consejos prácticos para reducción
- Alternativas sostenibles
- Mejores prácticas

## 🚀 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/co2-paper-calculator.git
cd co2-paper-calculator
```

2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate   # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
cp .streamlit/secrets.example.toml .streamlit/secrets.toml
# Editar secrets.toml con tus configuraciones
```

## 💻 Uso

1. Iniciar la aplicación:
```bash
streamlit run app.py
```

2. Acceder a la aplicación:
- Local: http://localhost:8501
- Red: http://[YOUR-IP]:8501

3. En la interfaz:
   - Seleccionar tipo de papel
   - Especificar formato
   - Ingresar cantidad
   - Ver resultados y recomendaciones

## 📁 Estructura del Proyecto

```
co2-paper-calculator/
├── .streamlit/
│   ├── config.toml       # Configuración de Streamlit
│   └── secrets.toml      # Variables secretas
├── app.py                # Aplicación principal
├── requirements.txt      # Dependencias
├── .gitignore           # Exclusiones de Git
└── README.md            # Documentación
```

## 🧮 Metodología

### Factores de Emisión
- Papel nuevo: 3.0 kg CO2/kg
- Papel reciclado: 1.8 kg CO2/kg
- Papel mixto: 2.4 kg CO2/kg

### Pesos Estándar
- A4: 5g (80g/m²)
- A3: 10g
- Otros formatos: Calculados proporcionalmente

### Cálculos
```python
emisiones = peso_papel * factor_emisión * factor_tiempo
```

## 👥 Contribuir

1. Fork el proyecto
2. Crear una rama (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

### Áreas de Mejora
- Más tipos de papel
- Factores de emisión por país
- Exportación de reportes
- Integración con sistemas de gestión

## 📄 Licencia

Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.

## 🙏 Agradecimientos

- [Streamlit](https://streamlit.io/) por su increíble framework
- [Environmental Paper Network](https://environmentalpaper.org/) por los datos de emisiones
- Todos los contribuidores que han ayudado a mejorar esta herramienta
