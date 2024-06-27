import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo Excel completo y seleccionar las primeras 300 filas
df = pd.read_excel('data/raw/dataset.xlsx').head(300)

# Cuento las veces que aparece el valor en las columnas C12_V1_1 y C12_V1_2
conteo_1_en_C12_V1_1 = df['C12_V1_1'].value_counts().get(1, 0)
conteo_1_en_C12_V1_2 = df['C12_V1_2'].value_counts().get(1, 0)

# Imprimo los resultados
print(f"El valor '1' aparece {conteo_1_en_C12_V1_1} veces en la columna C12_V1_1.")
print(f"El valor '1' aparece {conteo_1_en_C12_V1_2} veces en la columna C12_V1_2.")

# Comparo los conteos y determinar cuál columna tiene más veces el valor '1'
if conteo_1_en_C12_V1_1 > conteo_1_en_C12_V1_2:
    columna_mas_grande = 'C12_V1_1'
    frecuencia_mas_grande = conteo_1_en_C12_V1_1
elif conteo_1_en_C12_V1_2 > conteo_1_en_C12_V1_1:
    columna_mas_grande = 'C12_V1_2'
    frecuencia_mas_grande = conteo_1_en_C12_V1_2
else:
    columna_mas_grande = 'Ambas columnas tienen la misma frecuencia de valor 1'
    frecuencia_mas_grande = conteo_1_en_C12_V1_1  # o conteo_1_en_C12_V1_2, ya que son iguales

print(f"La columna con más veces el valor '1' es '{columna_mas_grande}' con {frecuencia_mas_grande} ocurrencias.")

# Crear un gráfico de barras comparativo
plt.figure(figsize=(8, 6))
sns.barplot(x=['MAL FUNCIONAMIENTO PÚBLICO', 'COMODIDAD'], y=[conteo_1_en_C12_V1_1, conteo_1_en_C12_V1_2], palette='viridis')
plt.title('Motivo de contratación: Seguro de sanidad')
plt.xlabel('Columna')
plt.ylabel('Frecuencia')
plt.show()
