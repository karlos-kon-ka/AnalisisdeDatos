import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel completo
df = pd.read_excel('data/raw/dataset.xlsx')

# Verificar las columnas disponibles en el DataFrame
print("Columnas disponibles en el DataFrame:")
print(df.columns)

# Columnas de interés y sus etiquetas personalizadas
columns_of_interest = {
    'C1_10': 'depresión',
    'C1_11': 'Ansiedad crónica',
    'C1_12': 'Migraña',
    'C1_13': 'Cataratas',
    'C1_14': 'Tiroides',
    'C1_15': 'Problemas crónicos de piel',
    'C1_16': 'Colesterol alto'
}

# Verificar y ajustar las columnas de interés para asegurarse de que están en el DataFrame
columns_to_use = [col for col in columns_of_interest.keys() if col in df.columns]

# Contar la frecuencia de valores "1" en cada columna de interés
counts = df[columns_to_use].apply(pd.Series.value_counts).loc[1]

# Crear la gráfica de barras solo si hay datos disponibles
if not counts.empty:
    # Crear la gráfica de barras
    plt.figure(figsize=(12, 8))
    bars = plt.bar([columns_of_interest[col] for col in columns_to_use], counts.values, color=['blue', 'green', 'orange', 'red', 'purple', 'brown', 'pink'])

    # Añadir etiquetas y título
    plt.title('Frecuencia de valores "1" en columnas específicas')
    plt.xlabel('Columnas')
    plt.ylabel('Frecuencia')
    plt.ylim(0, max(counts.values) * 1.1)  # ajuste del límite y para mejor visualización

    # Añadir etiquetas con los valores numéricos en las barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 2), ha='center', va='bottom')

    plt.xticks(rotation=45)  # rotar las etiquetas del eje x para mejor visualización
    plt.tight_layout()  # ajustar el diseño de la gráfica para evitar superposiciones
    plt.show()
else:
    print("No se encontraron valores '1' en las columnas especificadas.")
