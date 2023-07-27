
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=df, x="dia", y="venda", errorbar=None)
  grafico.set(title='Valor de venda por dia', xlabel='Dias', ylabel='Valor')
plt.savefig('gasolina.png')
