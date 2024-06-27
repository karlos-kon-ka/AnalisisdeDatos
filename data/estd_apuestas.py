import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel completo y seleccionar las primeras 300 filas
df = pd.read_excel('data/raw/dataset.xlsx').head(300)

# Contar las veces que aparecen los valores '1', '2' y '3' en la columna E11
conteo_4_en_E11 = df['E11'].value_counts().get(4, 0)
conteo_2_en_E11 = df['E11'].value_counts().get(2, 0)
conteo_3_en_E11 = df['E11'].value_counts().get(3, 0)

# Imprimir los resultados
print(f"El valor '1' aparece {conteo_4_en_E11} veces en la columna E11.")
print(f"El valor '2' aparece {conteo_2_en_E11} veces en la columna E11.")
print(f"El valor '3' aparece {conteo_3_en_E11} veces en la columna E11.")

# Crear un gráfico de barras comparativo
plt.figure(figsize=(8, 6))
sns.barplot(x=['Salamanca', 'Arganzuela', 'Retiro'], y=[conteo_4_en_E11, conteo_2_en_E11, conteo_3_en_E11], palette='viridis')
plt.title('Partacipación en juegos de apuestas')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.show()
