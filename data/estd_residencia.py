import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel completo y seleccionar las primeras 300 filas
df = pd.read_excel('data/raw/dataset.xlsx').head(300)

# Contar las veces que aparecen los valores '1', '2' y '3' en la columna G25
conteo_4_en_G25 = df['G25'].value_counts().get(4, 0)
conteo_2_en_G25 = df['G25'].value_counts().get(2, 0)
conteo_3_en_G25 = df['G25'].value_counts().get(3, 0)
conteo_5_en_G25 = df['G25'].value_counts().get(5, 0)

# Imprimir los resultados
print(f"El valor '1' aparece {conteo_4_en_G25} veces en la columna G25.")
print(f"El valor '2' aparece {conteo_2_en_G25} veces en la columna G25.")
print(f"El valor '3' aparece {conteo_3_en_G25} veces en la columna G25.")

# Crear un gráfico de barras comparativo
plt.figure(figsize=(8, 6))
sns.barplot(x=['Bastante improbable', 'Bastante probable', 'Ni probable ni improbable', 'Muy improbable'], y=[conteo_4_en_G25, conteo_2_en_G25, conteo_3_en_G25, conteo_5_en_G25], palette='viridis')
plt.title('Cree que es probable que  tenga que dejar su vivienda en los próximos 6 meses porque no pueda pagarla')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.show()
