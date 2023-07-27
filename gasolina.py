
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=df, x="dia", y="venda", errorbar=None)
  grafico.set(title='Price per day', xlabel='Day', ylabel='Price')
plt.savefig('gasolina.png')
