from scripts.graficas import cargar_datos, generar_graficas

if __name__ == "__main__":
    datos = cargar_datos("data/clases.json")
    generar_graficas(datos)