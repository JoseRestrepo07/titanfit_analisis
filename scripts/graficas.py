import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cargar_datos(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def generar_graficas(data):
    clases_admin = pd.DataFrame(data['admin'])
    clases_cliente = pd.DataFrame(data['cliente'])

    # Unimos los dos DataFrames
    clases = pd.concat([clases_admin, clases_cliente], ignore_index=True)

    # Gráfico: clases por instructor
    plt.figure(figsize=(6, 4))
    sns.countplot(x="instructor", data=clases, palette="Blues")
    plt.title("Cantidad de clases por instructor")
    plt.xlabel("Instructor")
    plt.ylabel("Cantidad de clases")
    plt.tight_layout()
    plt.show()

    # Gráfico: clases por nombre
    plt.figure(figsize=(6, 4))
    sns.countplot(x="nombre", data=clases, palette="dark")
    plt.title("Clases ofrecidas")
    plt.xlabel("Nombre de la clase")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.show()

    # Gráfico de torta: distribución por día
    dias = clases['horario'].apply(lambda h: h.split()[0])  # extraer "Lunes", "Martes", etc.
    conteo_dias = dias.value_counts()

    plt.figure(figsize=(5, 5))
    plt.pie(conteo_dias, labels=conteo_dias.index, autopct="%1.1f%%", colors=sns.color_palette("pastel"))
    plt.title("Distribución de clases por día")
    plt.tight_layout()
    plt.show()

    # Gráfico: Clases por día de la semana (gráfico de barras)
    dias = clases["horario"].apply(lambda h: h.split()[0])  # Extraer día (Lunes, Martes, etc.)
    conteo_dias = dias.value_counts().reindex(["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])

    plt.figure(figsize=(6, 4))
    sns.barplot(x=conteo_dias.index, y=conteo_dias.values, palette="Set2")
    plt.title("Cantidad de clases por día")
    plt.xlabel("Día")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.show()

    # Gráfico: Distribución de clases por hora (línea)
    horas = clases["horario"].apply(lambda h: h.split()[1])  # Extraer "10:00", "18:00"
    conteo_horas = horas.value_counts().sort_index()

    plt.figure(figsize=(8, 4))
    sns.lineplot(x=conteo_horas.index, y=conteo_horas.values, marker="o", color="dodgerblue")
    plt.title("Distribución de clases por hora")
    plt.xlabel("Hora")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.show()