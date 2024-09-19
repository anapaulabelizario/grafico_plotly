import plotly.express as px
import pandas as pd

# Criar um DataFrame com dados de exemplo
data = {
    'Receita': [5000, 1200, 800],
    'Despesas': [-150, -300, -1200],
    'Valor Total': [4850, 900, -400],
}

df = pd.DataFrame(data)

# Calcular a matriz de correlação
correlation_matrix = df.corr(method='pearson')

# Criar uma matriz de calor (heatmap) para visualizar a correlação
fig = px.imshow(correlation_matrix, 
                color_continuous_scale='Blues', 
                title='Matriz de Correlação de Pearson',
                labels=dict(x="Variáveis", y="Variáveis"))

# Mostrar o gráfico
fig.show()