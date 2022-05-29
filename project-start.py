
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('dolinha.csv')

# for aninhado com listas
profit = []
flag = 0
s = []
dif = []
listsoma = []
resultado = 0
df['diferenca'] = df.close.diff()
soma = 0
valor_diferencial_atual = 0

for i in range(len(df)):
    rv = df.real_volume[i]
    profit.append(np.nan)
    dif.append(df.diferenca[i])
    s.append(soma)
    valor_diferencial_atual = df.diferenca[i]

    if df['real_volume'][i] <= 5000.0 and flag != 1: # condição de entrada

        flag = 1
        profit.pop()
        profit.append('start')
        soma = 0
        listsoma.clear()

    soma += df.diferenca[i]
    listsoma.append(valor_diferencial_atual)
    acumuladolista = np.cumsum(listsoma)
    resultado = acumuladolista[-1]



    if resultado >= 20.0 and flag == 1: #condição de saida
        profit.pop()
        profit.append('gain')
        listsoma.clear()
        resultado = 0
        acumuladolista = 0
        flag = 0
        soma = 0
    
    if resultado <= -4.0 and flag == 1: #condição de saida
        profit.pop()
        profit.append('loss')
        listsoma.clear()
        resultado = 0
        acumuladolista = 0
        flag = 0
        soma = 0

df['profit'] = profit


profit_df = pd.DataFrame(profit)
profit_df = profit_df.dropna()
profit_df.columns = ['profit']
profit_df = profit_df[profit_df['profit'] != 'start']

fig = px.pie(profit_df, names='profit') 
fig.show()