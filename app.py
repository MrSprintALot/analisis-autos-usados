import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar dataset
df = pd.read_csv('vehicles_us.csv')

st.title('Análisis interactivo de autos usados')

# Mostrar datos
if st.checkbox('Mostrar tabla de datos'):
    st.write(df)

# Histograma
if st.button('Mostrar histograma de kilometraje'):
    st.write('Histograma de odómetro')
    fig = px.histogram(df, x='odometer', title='Distribución de kilometraje')
    st.plotly_chart(fig)

# Gráfico de dispersión
if st.button('Mostrar dispersión precio vs kilometraje'):
    st.write('Gráfico de dispersión: precio vs odómetro')
    fig = px.scatter(df, x='odometer', y='price', color='condition', title='Precio vs Kilometraje')
    st.plotly_chart(fig)

# Histograma de modelos por tipo
if st.button('Mostrar tipos de vehículo por modelo'):
    st.write('Histograma de modelos por tipo de auto')
    fig = px.histogram(df, x='model', color='type', barmode='stack', title='Tipos de vehículo por modelo')
    st.plotly_chart(fig)
