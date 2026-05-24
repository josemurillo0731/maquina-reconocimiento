import streamlit as st

st.title("Máquina de Reconocimiento de Patrones - Letra T")

st.markdown("""
### ¿Cómo funciona?

En esta aplicación vemos la simulacion  de una máquina capaz de reconocer patrones simples.

Cada píxel de la imagen se multiplica por un peso ajustable.
Luego todos los resultados se suman para generar un puntaje.

Si el puntaje supera el threshold, la imagen será clasificada como una posible letra T.
""")

# Imágenes
T1 = [
    [1,1,1],
    [0,1,0],
    [0,1,0]
]

T2 = [
    [1,1,1],
    [0,1,0],
    [0,1,0]
]

T3 = [
    [1,1,1],
    [0,1,0],
    [0,1,0]
]

N1 = [
    [0,1,0],
    [1,1,1],
    [0,1,0]
]

N2 = [
    [1,0,1],
    [1,1,1],
    [0,1,0]
]

N3 = [
    [1,1,0],
    [0,1,1],
    [0,1,0]
]

imagenes = {
    "T1": T1,
    "T2": T2,
    "T3": T3,
    "No T 1": N1,
    "No T 2": N2,
    "No T 3": N3
}

st.subheader("Ajuste de pesos")

pesos = []

for i in range(3):
    fila = []
    columnas = st.columns(3)

    for j in range(3):
        peso = columnas[j].slider(
            f"W{i}{j}",
            min_value=-5,
            max_value=5,
            value=1
        )
        fila.append(peso)

    pesos.append(fila)

threshold = st.slider(
    "Threshold",
    min_value=-20,
    max_value=20,
    value=5
)

st.subheader("Fórmula utilizada")

st.latex(r"y=\sum w_i x_i")

st.subheader("Resultados")

for nombre, imagen in imagenes.items():

    total = 0

    for i in range(3):
        for j in range(3):
            total += imagen[i][j] * pesos[i][j]

    st.write(f"### {nombre}")

    st.table(imagen)

    st.write(f"Puntaje: {total}")

    if total >= threshold:
        st.success("Parece una T")
    else:
        st.error("No parece una T")