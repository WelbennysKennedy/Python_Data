import pandas as pd


data = {'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
        'Idade': [25, 30, 22, 28],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}

df = pd.DataFrame(data)

sexo = ['Masculino', 'Feminino', 'Masculino', 'Feminino']
df['Gênero'] = sexo


nova_linha = {'Nome': 'Carlos', 'Idade': 35, 'Cidade': 'Porto Alegre', 'Gênero': 'Masculino'}
df.loc[len(df)] = nova_linha


data_adicional = {'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
                  'Email': ['lucas@email.com', 'sofia@email.com', 'rafael@email.com', 'isabela@email.com'],
                    'Telefone': ['123456789', '987654321', '555555555', '111111111']
                  }
df2 = pd.DataFrame(data_adicional)
df_combinado = df.join(df2.set_index('Nome'), on='Nome')