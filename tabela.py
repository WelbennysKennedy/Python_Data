import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


shape = (12, 4)
dataset = np.random.randint(0, 100, size=shape)


df = pd.DataFrame(dataset, columns=['A', 'B', 'C' , 'D'])


data_inicial = '2026-01-01'
datas = pd.date_range(start=data_inicial, periods=12, freq='M')
df['Data'] = datas
df.set_index('Data', inplace=True)
print(df)



linhas = ['-', '--', ':', '-.']
marcadores = ['o', 's', '^', 'D']
plt.figure(figsize=(10, 6))

for i, coluna in enumerate(df.columns):
    plt.plot(df.index, df[coluna], df[coluna], label=coluna,
             linestyle=linhas[i], color='k', marker=marcadores[i])
    

plt.title('Grafico de Linhas', fontname='calibre', fontsize=16)
plt.xlabel('Data', fontname='calibre', fontsize=14)
plt.ylabel('Valores', fontname='calibre', fontsize=14)
plt.legend(fontsize=12)
plt.savefig('grafico_vetorial.svg', format='svg')
plt.show()    