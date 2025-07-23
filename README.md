# 🚗 Análisis interactivo de autos usados (Streamlit + Plotly)

Este proyecto consiste en una aplicación web interactiva construida con **Streamlit**, que permite explorar un conjunto de datos de autos usados vendidos en EE. UU.

La app forma parte de un sprint del bootcamp de Data Analytics, y fue desplegada en la nube con Render.

## 🧰 Herramientas utilizadas

- Python
- Pandas
- Plotly Express
- Streamlit
- Git & GitHub
- Render (para despliegue en la nube)

## 📊 Funcionalidades

- Ver el dataset completo
- Histograma del kilometraje (`odometer`)
- Gráfico de dispersión entre `price` y `odometer` por condición
- Histograma apilado por tipo de auto y modelo
- Interfaz con botones y visualización dinámica

🔗 [Ver aplicación desplegada en Render](https://analisis-autos-usados.onrender.com)


## 🖥️ Cómo ejecutar localmente

```bash
git clone https://github.com/MrSprintALot/analisis-autos-usados.git
cd analisis-autos-usados
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
