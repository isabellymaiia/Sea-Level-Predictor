import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Ler dados do arquivo
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Criar gráfico de dispersão
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Dados')

    # 3. Criar a primeira linha de melhor ajuste
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))  # Estender os anos até 2050
    sea_level_fit = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_fit, color='red', label='Linha de Melhor Ajuste (1880-2050)')

    # 4. Criar a segunda linha de melhor ajuste (apenas a partir de 2000)
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    
    # Limitar anos para a linha de ajuste de 2000
    years_2000_extended = pd.Series(range(2000, 2051))  # Estender anos apenas a partir de 2000
    sea_level_fit_2000 = slope_2000 * years_2000_extended + intercept_2000
    plt.plot(years_2000_extended, sea_level_fit_2000, color='green', label='Linha de Melhor Ajuste (2000-2050)')

    # 5. Adicionar rótulos e título
    plt.xlabel('Year')  # Rótulo do eixo X
    plt.ylabel('Sea Level (inches)')  # Rótulo do eixo Y
    plt.title('Rise in Sea Level')  # Título do gráfico
    plt.legend()

    # Salvar o gráfico e retornar dados para testes (NÃO MODIFICAR)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
