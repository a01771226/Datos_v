import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('multiTimeline.csv')
print(df.head)

df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)

plt.figure(figsize=(10, 6))
plt.plot(df, color='skyblue', linewidth=2)
plt.title('Gráfico de Línea')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.grid(True)
plt.show()