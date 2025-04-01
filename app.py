# 1) https://pypi.org/project/streamlit/

# 2) Terminal: cd Streamlit > pip install -r requirements.txt
#                           > streamlit run app.py

# 3) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración directa de la aplicación
APP_NAME = "CO2 Rechner"
VERSION = "1.0.0"
DEVELOPER = "ECUADOR-IT"
DEV_EMAIL = "ecuador@ecuador-it.com"
GITHUB_REPO = "https://github.com/dwn10/CO2_Rechner"

# Configuración de la página
st.set_page_config(
    page_title=APP_NAME,
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título y descripción
st.title("🌱 Calculadora de Emisiones de :blue[CO2 - Papel]")
st.markdown("""
Esta aplicación te ayuda a calcular las emisiones de CO2 asociadas con el consumo de papel
y te proporciona recomendaciones para reducir tu huella de carbono.
""")

# Factores de emisión (kg CO2 por kg de papel)
EMISSION_FACTORS = {
    "Papel nuevo": 3.0,  # Papel virgen
    "Papel reciclado": 1.8,  # Papel reciclado
    "Papel mixto": 2.4,  # Mezcla de virgen y reciclado
}

# Pesos promedio (gramos)
PAPER_WEIGHTS = {
    "A4": 5,  # 80g/m² * 0.0624m² = ~5g
    "A3": 10,  # Doble de A4
    "Carta": 4.5,
    "Sobre": 8,
    "Periódico": 45,  # Por unidad
    "Revista": 150,  # Por unidad
}

# Sidebar para inputs
st.sidebar.header("📝 :blue[Ingresa tus datos]")

# Selección del tipo de papel
paper_type = st.sidebar.selectbox(
    ":blue[Tipo de papel]",
    list(EMISSION_FACTORS.keys())
)

# Selección del formato
paper_format = st.sidebar.selectbox(
    ":blue[Formato de papel]",
    list(PAPER_WEIGHTS.keys())
)

# Cantidad de unidades
units = st.sidebar.number_input(
    ":blue[Cantidad de unidades]",
    min_value=1,
    value=100
)

# Período de tiempo
time_period = st.sidebar.selectbox(
    ":blue[Período de tiempo]",
    ["Día", "Semana", "Mes", "Año"]
)

# Footer en la barra lateral
st.sidebar.markdown("---")
st.sidebar.markdown(f"""
<div style='text-align: center; color: gray; padding: 10px;'>
    <p>Desarrollado por:</p>
    <h4>{DEVELOPER}</h4>
    <p>📧 {DEV_EMAIL}</p>
    <p>🌐 <a href='{GITHUB_REPO}' target='_blank'>www.ecuador-it.com</a></p>
    <p> 2025 - v{VERSION}</p>
</div>
""", unsafe_allow_html=True)

# Cálculos
paper_weight_kg = (PAPER_WEIGHTS[paper_format] * units) / 1000  # Convertir a kg
emissions = paper_weight_kg * EMISSION_FACTORS[paper_type]

# Factores de multiplicación para diferentes períodos
time_multipliers = {
    "Día": 1,
    "Semana": 7,
    "Mes": 30,
    "Año": 365
}

total_emissions = emissions * time_multipliers[time_period]

# Mostrar resultados
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 :blue[Resultados]")
    st.metric(
        label=":blue[Emisiones de CO2]",
        value=f"{total_emissions:.2f} kg CO2",
        delta=f"{total_emissions/time_multipliers[time_period]:.2f} kg CO2/día"
    )
    
    # Comparaciones
    trees_needed = total_emissions / 22  # Un árbol absorbe aprox. 22kg CO2 al año
    car_km = total_emissions * 6  # 1kg CO2 ≈ 6km en coche
    
    st.info(f"💡 Esto equivale a:")
    st.write(f"🌳 La absorción de CO2 de :blue[{trees_needed:.1f}] árboles en un año")
    st.write(f"🚗 Conducir :blue[{car_km:.1f}] km en un coche promedio")

with col2:
    # Gráfico de comparación con otros tipos de papel
    comparison_data = pd.DataFrame({
        'Tipo': list(EMISSION_FACTORS.keys()),
        'Emisiones': [ef * paper_weight_kg * time_multipliers[time_period] 
                     for ef in EMISSION_FACTORS.values()]
    })
    
    fig = px.bar(
        comparison_data,
        x='Tipo',
        y='Emisiones',
        title='Comparación de emisiones por tipo de papel',
        labels={'Emisiones': 'kg CO2'},
        color='Tipo'
    )
    st.plotly_chart(fig)

# Recomendaciones
st.subheader("💚 :blue[Recomendaciones para reducir emisiones]")
st.markdown("""
- **:blue[Usa papel reciclado:]** Reduce las emisiones en un 40%
- **:blue[Imprime a doble cara:]** Reduce el consumo de papel a la mitad
- **:blue[Digitaliza documentos:]** Evita impresiones innecesarias
- **:blue[Reutiliza el papel:]** Usa el reverso para notas
- **:blue[Recicla siempre:]** Asegura que el papel se pueda reutilizar
""")

# Footer
st.markdown("---")
st.markdown("""
**:blue[Nota:]** Los cálculos son aproximados y basados en promedios industriales.
Los factores de emisión pueden variar según el país y el proceso de fabricación.
""")