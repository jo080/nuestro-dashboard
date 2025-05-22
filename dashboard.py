import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Función para cargar datos desde el archivo
def cargar_datos(archivo="datos.csv"):
    return pd.read_csv(archivo)

# Identificación de alertas de asistencia baja (<70%)
def identificar_alertas(df):
    alertas = []
    i = 0
    while i < len(df):
        if df.iloc[i]["Asistencia"] < 70:
            alertas.append(df.iloc[i]["Alumno"])
        i += 1
    return alertas

# Cargar datos
df = cargar_datos()

# Configuración del dashboard en Streamlit
st.title("Dashboard de Asistencia y Rendimiento")

# Mostrar la tabla de datos
st.subheader("Datos de Asistencia")
st.dataframe(df)

# Generar gráfico de asistencia
st.subheader("Distribución de Asistencia")
fig, ax = plt.subplots()
ax.hist(df["Asistencia"], bins=10, color="skyblue", edgecolor="black")
ax.set_xlabel("Porcentaje de Asistencia")
ax.set_ylabel("Cantidad de Estudiantes")
st.pyplot(fig)

# Mostrar alertas
st.subheader("Alertas de Asistencia Baja")
alertas = identificar_alertas(df)

if alertas:
    st.warning("Estudiantes con asistencia < 75%")
    i = 0
    while i < len(alertas):
        st.write('alertas[i]')
        i += 1
else:
    st.success('No hay alertas de asistencia.')
