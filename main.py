# Importações necessárias
import pandas as pd


# Dados iniciais para o DataFrame principal
data = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Idade': [25, 30, 22, 28],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}

# Criar DataFrame principal
df = pd.DataFrame(data)

# Adicionar coluna de gênero
sexo = ['Masculino', 'Feminino', 'Masculino', 'Feminino']
df['Gênero'] = sexo

# Adicionar uma nova linha ao DataFrame
nova_linha = {
    'Nome': 'Carlos',
    'Idade': 35,
    'Cidade': 'Porto Alegre',
    'Gênero': 'Masculino'
}
df.loc[len(df)] = nova_linha

# Dados adicionais para combinar
data_adicional = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana' ],
    'Email': ['lucas@email.com', 'sofia@email.com', 'rafael@email.com', 'isabela@email.com'],
    'Telefone': ['123456789', '987654321', '555555555', '111111111']
}

# Criar DataFrame adicional
df2 = pd.DataFrame(data_adicional)

# Combinar os DataFrames usando join
df_combinado = df.join(df2.set_index('Nome'), on='Nome')





# Exibir o DataFrame combinado
print(df_combinado)

