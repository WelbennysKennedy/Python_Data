import numpy as np
import pandas as pd


shape = (12, 3)
dataset = np.random.randint(0, 100, size=shape)


df = pd.DataFrame(dataset, columns=['A', 'B', 'C'])


data_inicial = '2026-01-01'
datas = pd.date_range(start=data_inicial, periods=12, freq='M')
df['Data'] = datas
df.set_index('Data', inplace=True)
print(df)