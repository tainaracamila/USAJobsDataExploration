"""

Neste projeto usaremos uma pesquisa recente nos EUA sobre o mercado de trabalho para programadores de software.
Nosso objetivo é fazer uma investigação inicial dos dados a fim de detectar problemas com os dados,
necessidade de mais variáveis, falhas na organização e necessidades de transformação.

Pesquisa Salarial realizada pelo site https://www.freecodecamp.com/ com programadores de software
nos EUA que frequentaram treinamentos Bootcamp.

"""

import pandas as pd


import warnings
warnings.filterwarnings("ignore")
from plots import Plot

if __name__ == '__main__':

    pt = Plot()
    df = pd.read_csv("Dados-Pesquisa.csv", low_memory=False)
    #print(df.describe())
    #print(list(df))

    # análises exploratória

    # 1) Distribuição de idade
    pt.age_distribution(df)
    # 2) Sexo dos programadores
    pt.gender_distribution(df)
    # 3) Interesse profissional dos programadores
    pt.interest_distribution(df)
    # 4) Distribuição de empregabilidade
    pt.employment_field_distribution(df)
    # 5) Preferencia de emprego por idade
    pt.job_preference_per_age_range(df)
    # 6) Relocação por idade
    pt.relocation_per_age(df)
    # 7) Horas de capacitação por idade
    pt.age_capacity(df)
    # 8) Capacitação e expectativa salarial
    pt.capacity_salary_expectation(df)