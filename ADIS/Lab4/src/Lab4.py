import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

def read_dataset(path):
    df = pd.read_csv(path, sep=';', encoding='cp1252')
    return df


def remove_typo(df):
    df.rename(columns={"Populatiion": "Population"}, inplace=True)
    return df

def clean_up(df):
    df['Area'] = df['Area'].str.replace(',', '.').astype(float)
    df["GDP per capita"] = df["GDP per capita"].str.replace(',', '.').astype(float)
    df["CO2 emission"] = df["CO2 emission"].str.replace(',', '.').astype(float)
    return df

def fix_negative(df):
    fix_gdp = df[df['GDP per capita'] < 0]
    area_gdp = df[df['Area'] < 0]
    fix_gdp['GDP per capita'] *= -1
    area_gdp['Area'] *= -1
    df[df['GDP per capita'] < 0] = fix_gdp
    df[df['Area'] < 0] = area_gdp
    return df

def fix_NaN(df):
    df = df.fillna(df.mean())
    return df


def print_exploring(df):
    print('Data frame info:')
    df.info()

    pd.set_option("display.max_columns", None)
    print('\nFirst 5 rows:')
    print(df.head())

    print('\nDescriptive statistics of the dataframe:')
    print(df.describe())


def normally_visual_test(df):
    fig, axs = plt.subplots(1, 4, figsize=(16, 4))

    fig.suptitle('Histograms', fontsize=16)

    axs[0].set_title('GDP per capita')
    axs[0].hist(df['GDP per capita'])

    axs[1].set_title('Population')
    axs[1].hist(df['Population'])

    axs[2].set_title('CO2 emission')
    axs[2].hist(df['CO2 emission'])

    axs[3].set_title('Area')
    axs[3].hist(df['Area'])
    plt.show()

def shapiro_test(df, columns=0, alpha=0.05):
    print("\nShapiro–Wilk test:")
    if columns==0:
        data = df
        columns = [1]
    for column in columns:
        if column != 1:
            data = df[column]
        stat, p = stats.shapiro(data)
        print('Statistics=%.3f, p=%.3f' % (stat, p))
        if p > alpha:
            print('The data correspond to a normal distribution')
        else:
            print('The data do not correspond to a normal distribution')

def ks_test(df, columns=0, alpha=0.05):
    print("\nKolmogorov–Smirnov test:")
    if columns==0:
        data = df
        columns = [1]
    for column in columns:
        if column != 1:
            data = df[column]
        stat, p = stats.kstest(data, 'norm')
        print('Statistics=%.3f, p=%.3f' % (stat, p))
        if p > alpha:
            print('The data correspond to a normal distribution')
        else:
            print('The data do not correspond to a normal distribution')

def dagostino_test(df, columns=0, alpha=0.05):
    print("\nD'Agostino's test:")
    if columns==0:
        data = df
        columns = [1]
    for column in columns:
        if column != 1:
            data = df[column]
        stat, p = stats.normaltest(data)
        print('Statistics=%.3f, p=%.3f' % (stat, p))
        if p > alpha:
            print('The data correspond to a normal distribution')
        else:
            print('The data do not correspond to a normal distribution')


def mean_median(df, columns):
    for column in columns:
        print(f'\n{column}:')
        mean_gdp = df[column].mean()
        median_gdp = df[column].median()
        print(f'Mean {column}', ' - ' ,mean_gdp)
        print(f'Median {column} ',  ' - ' , median_gdp, '\n')    
        if mean_gdp == median_gdp:
            print(f"The mean and median {column} are the same: {mean_gdp}")

# def mean_median(df, columns):
#     for column in columns:
#         print(f'\n{column}:')
#         for region in df['Region'].unique():
#             region_data = df[df['Region'] == region]
#             mean_gdp = region_data[column].mean()
#             median_gdp = region_data[column].median()
#             print(f'Mean {column} in', region, ' - ' ,mean_gdp)
#             print(f'Median {column} in', region, ' - ' , median_gdp, '\n')    
#             if mean_gdp == median_gdp:
#                 print(f"In the {region} region, the mean and median {column} are the same: {mean_gdp}")


def closest_co2(df):
    df['CO2 emission'].hist(by=df['Region'], layout=(4, 2), figsize=(10, 20))
    plt.show()  

    for region in df['Region'].unique():
        region_emissions = df[df['Region'] == region]['CO2 emission']

        print(f'\nCheck for the region {region}:')
        try:
            shapiro_test(region_emissions)
        except ValueError as e:
            print(str(e))
        try:
            ks_test(region_emissions)
        except ValueError as e:
            print(str(e))
        try:
            dagostino_test(region_emissions)
        except ValueError as e:
            print(str(e))

def pie_chart(df):
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.suptitle('Pie chart', fontsize=16)
    labels = pd.unique(df['Region'])
    wedges, texts, autotexts = ax.pie(df.groupby('Region').sum()['Population'], labels=labels,
                                    autopct='%1.1f%%', textprops=dict(color='w'))

    ax.set_title('Population by region')
    ax.legend(wedges, labels,
            title='Regions',
            loc='center left',
            bbox_to_anchor=(1, 0, 0, 1))

    plt.setp(autotexts, size=12, weight='bold')

    plt.show()


if __name__ == "__main__":
    #Основне завдання
    data_path = 'Data2.csv'
    #Читання файлу
    df = read_dataset(data_path)
    #Виправляємо дані
    df = remove_typo(df)
    df = clean_up(df)
    df = fix_negative(df)
    df = fix_NaN(df)
    #Проаналізуємо структуру
    print_exploring(df)
    #Перевіримо, чи є параметри, що розподілені за нормальним законом
    normally_visual_test(df)
    column = ['GDP per capita', 'Population', 'CO2 emission', 'Area']
    shapiro_test(df,column)
    ks_test(df, column)
    dagostino_test(df,column)
    #Перевіримо гіпотезу про рівність середнього і медіани для одного з параметрів
    mean_median(df, column)
    #Перевіримо, в якому регіоні розподіл викидів СО2 найбільш близький до нормального
    closest_co2(df)
    #Побудуємо кругову діаграму населення по регіонам
    pie_chart(df)


    #Додатове завдання