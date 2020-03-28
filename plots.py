import matplotlib.pyplot as plt
import colorsys
import pandas as pd
import numpy as np
plt.style.use('seaborn-talk')

class Plot(object):

    def age_distribution(self, df):
        df.Age.hist(bins=60) #bins = quantidade de labels que terá o histograma
        plt.xlabel("Idade")
        plt.ylabel("Número de Profissionais")
        plt.title("Distribuição de Idade")
        plt.show()

    def gender_distribution(self, df):
        # pode haver mais de um sexo disponível
        labels = df.Gender.value_counts().index
        # quantidade de areas de serviço
        num = len(df.EmploymentField.value_counts().index)
        # lista de cores
        listaHSV = [(x*1.0/num, 0.5, 0.5) for x in range(num)]
        listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

        fatias, texto = plt.pie(df.Gender.value_counts(), colors=listaRGB, startangle=90)
        plt.axes().set_aspect('equal', 'datalim')
        plt.legend(fatias, labels, bbox_to_anchor=(1.05, 1))
        plt.title("Sexo")
        plt.show()

    def interest_distribution(self, df):
        # pode haver mais de uma area de interesse
        labels = df.JobRoleInterest.value_counts().index
        # quantidade de areas de interesse
        num = len(df.JobRoleInterest.value_counts().index)
        # lista de cores
        listaHSV = [(x*1.0/num, 0.5, 0.5) for x in range(num)]
        listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

        fatias, texto = plt.pie(df.JobRoleInterest.value_counts(), colors=listaRGB, startangle=90)
        plt.axes().set_aspect('equal', 'datalim')
        plt.legend(fatias, labels, bbox_to_anchor=(1.00, 1))
        plt.title("Interesse Profissional")
        plt.show()

    def employment_field_distribution(self, df):
        # pode haver mais de uma area de serviço
        labels = df.EmploymentField.value_counts().index
        # quantidade por area de serviço
        num = len(df.EmploymentField.value_counts().index)
        # lista de cores
        listaHSV = [(x*1.0/num, 0.5, 0.5) for x in range(num)]
        listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

        fatias, texto = plt.pie(df.EmploymentField.value_counts(), colors=listaRGB, startangle=90)
        plt.axes().set_aspect('equal', 'datalim')
        plt.legend(fatias, labels, bbox_to_anchor=(1.00, 1))
        plt.title("Área de trabalho atual")
        plt.show()

    def job_preference_per_age_range(self, df):
        # definindo intervalos de idade
        bins = [0, 20, 30, 40, 50, 60, 100]

        # copiando o df para não correr o risco de realizar modificações no df original
        df_age_ranges = df.copy()

        # help(pd.cut)
        df_age_ranges['AgeRanges'] = pd.cut(df_age_ranges['Age'], bins, labels=["< 20", "20-30", "30-40", "40-50",
                                                                                "50-60", "> 60"])

        # a função lambda foi utilizada para computar a media de cada tipo de preferencia de trabalho por faixa de idade
        # cria um novo dataframe df2
        df2 = pd.crosstab(df_age_ranges.AgeRanges, df_age_ranges.JobPref).apply(lambda r: r/r.sum(), axis=1)

        num = len(df_age_ranges.AgeRanges.value_counts().index)

        # Criando a lista de cores
        listaHSV = [(x * 1.0 / num, 0.5, 0.5) for x in range(num)]
        listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

        # Gráfico de Barras (Stacked)
        ax1 = df2.plot(kind="bar", stacked=True, color=listaRGB, title="Preferência de Trabalho por Idade")
        lines, labels = ax1.get_legend_handles_labels()
        ax1.legend(lines, labels, bbox_to_anchor=(1.51, 1))
        plt.show()

    def relocation_per_age(self, df):
        bins = [0, 20, 30, 40, 50, 60, 100]

        # copiando o df para não correr o risco de realizar modificações no df original
        df_age_ranges = df.copy()

        # help(pd.cut)
        df_age_ranges['AgeRanges'] = pd.cut(df_age_ranges['Age'], bins,
                                            labels=["< 20", "20-30", "30-40", "40-50", "50-60", "> 60"])

        df2 = pd.crosstab(df_age_ranges.AgeRanges, df_age_ranges.JobRelocateYesNo).apply(lambda r: r / r.sum(), axis=1)

        num = len(df_age_ranges.AgeRanges.value_counts().index)

        # Criando a lista de cores
        listaHSV = [(x * 1.0 / num, 0.5, 0.5) for x in range(num)]
        listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

        # Gráfico de Barras (Stacked)
        ax1 = df2.plot(kind="bar", stacked=True, color=listaRGB, title="Relocação por Idade")
        lines, labels = ax1.get_legend_handles_labels()
        ax1.legend(lines, ['Não', 'Sim'], loc = 'best')
        plt.show()

    def age_capacity(self, df):
        df9 = df.copy()
        # removendo linhas que possuem hours learning como missing
        df9 = df9.dropna(subset=["HoursLearning"])
        # atualiza para que fique entre 0 e 70
        df9 = df9[df['Age'].isin(range(0, 70))]

        # Definindo os valores de x e y
        x = df9.Age
        y = df9.HoursLearning

        # Computando os valores e gerando o gráfico
        m, b = np.polyfit(x, y, 1)
        plt.plot(x, y, '.')
        plt.plot(x, m * x + b, '-', color="red")
        plt.xlabel("Idade")
        plt.ylabel("Horas de Treinamento")
        plt.title("Idade por Horas de Treinamento")
        plt.show()

    def capacity_salary_expectation(self, df):
        df5 = df.copy()
        df5 = df5.dropna(subset=["ExpectedEarning"])
        df5 = df5[df['MoneyForLearning'].isin(range(0, 60000))]

        # Definindo os valores de x e y
        x = df5.MoneyForLearning
        y = df5.ExpectedEarning

        # Computando os valores e gerando o gráfico
        m, b = np.polyfit(x, y, 1)
        plt.plot(x, y, '.')
        plt.plot(x, m * x + b, '-', color="red")
        plt.xlabel("Investimento em Treinamento")
        plt.ylabel("Expectativa Salarial")
        plt.title("Investimento em Treinamento vs Expectativa Salarial")
        plt.show()
