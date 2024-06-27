import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel completo y seleccionar las primeras 300 filas
df = pd.read_excel('data/raw/dataset.xlsx').head(300)

# Contar las veces que aparecen los valores '1' y '2' en la columna E14_V2_2
conteo_1_en_E14_V2_2 = df['E14_V2_2'].value_counts().get(1, 0)
conteo_2_en_E14_V2_2 = df['E14_V2_2'].value_counts().get(2, 0)

# Imprimir los resultados
print(f"El valor '1' aparece {conteo_1_en_E14_V2_2} veces en la columna E14_V2_2.")
print(f"El valor '2' aparece {conteo_2_en_E14_V2_2} veces en la columna E14_V2_2.")

# Crear un gráfico de barras comparativo
plt.figure(figsize=(8, 6))
sns.barplot(x=['Si uso', 'No uso'], y=[conteo_1_en_E14_V2_2, conteo_2_en_E14_V2_2], palette='viridis')
plt.title('Uso de redes sociales')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.show()
