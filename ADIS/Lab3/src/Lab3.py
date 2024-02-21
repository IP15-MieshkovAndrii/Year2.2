import pandas as pd
import matplotlib.pyplot as plt


def read_dataset(path):
    df = pd.read_csv(path, sep=';', encoding='cp1252')
    return df


def print_exploring(df):
    print('Data frame info:')
    df.info()
    print('\nFirst 5 rows:')
    print(df.head())


def remove_typo(df):
    df.rename(columns={"Populatiion": "Population"}, inplace=True)
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


def clean_up(df):
    df['Area'] = df['Area'].str.replace(',', '.').astype(float)
    df["GDP per capita"] = df["GDP per capita"].str.replace(',', '.').astype(float)
    df["CO2 emission"] = df["CO2 emission"].str.replace(',', '.').astype(float)
    return df


def add_population_density(df):
    df["Population_density"] = df["Population"] / df["Area"]
    print(df.head())
    return df

def create_boxplot(df):
    fig, axs = plt.subplots(1, 4, figsize=(16, 4))

    fig.suptitle('Діаграми розмаху', fontsize=16)

    axs[0].set_title('GDP per capita')
    axs[0].boxplot(df['GDP per capita'])

    axs[1].set_title('Population')
    axs[1].boxplot(df['Population'])

    axs[2].set_title('CO2 emission')
    axs[2].boxplot(df['CO2 emission'])

    axs[3].set_title('Area')
    axs[3].boxplot(df['Area'])



def create_hist(df):
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

def number_two(df):
    highest_gdp_per_capita = df.loc[df['GDP per capita'].idxmax()]
    print("Country with the highest GDP per capita:", highest_gdp_per_capita['Country Name'])
    smallest_area = df.loc[df['Area'].idxmin()]
    print("Country with the smallest area:", smallest_area['Country Name'])


def number_three(df):
    mean_area_by_region = df.groupby('Region')['Area'].mean()
    region_with_highest_mean_area = mean_area_by_region.idxmax()
    print("Region with the highest average area per country:", region_with_highest_mean_area)

def number_four(df):
    highest_pop_density = df.loc[df['Population_density'].idxmax()]
    print("Country with the highest population density in the world:", highest_pop_density['Country Name'])
    europe_and_central_asia = df[df['Region'].isin(['Europe & Central Asia'])]
    highest_pop_density_in_europe_and_central_asia = europe_and_central_asia.loc[europe_and_central_asia['Population_density'].idxmax()]
    print("Country with the highest population density in Europe and Central Asia:", highest_pop_density_in_europe_and_central_asia['Country Name'])

def number_five(df):
    for region in df['Region'].unique():
        region_data = df[df['Region'] == region]
        mean_gdp = region_data['GDP per capita'].mean()
        median_gdp = region_data['GDP per capita'].median()
        print('\nMean GDP per capita in', region, ' - ' ,mean_gdp)
        print('Median GDP per capita in', region, ' - ' , median_gdp)    
        if mean_gdp == median_gdp:
            print(f"In the {region} region, the mean and median GDP per capita are the same: {mean_gdp}")


def number_six(df):
    df_sorted_gdp = df.sort_values(by='GDP per capita',  ascending=False)
    top5_gdp = df_sorted_gdp.head(5)
    bottom5_gdp = df_sorted_gdp.tail(5)
    print("\nTop 5 countries by GDP per capita:")
    print(top5_gdp)
    print("\nBottom 5 countries by GDP per capita:")
    print(bottom5_gdp)

    pd.set_option("display.max_columns", None)
    df['CO2 emission per citizen'] = df['CO2 emission'] / df['Population']
    df_sorted_co2 = df.sort_values(by='CO2 emission per citizen',  ascending=False)
    top5_co2 = df_sorted_co2.head(5)
    bottom5_co2 = df_sorted_co2.tail(5)
    print("\n\nTop 5 countries by CO2 emissions per citizen:")
    print(top5_co2)
    print("\nBottom 5 countries by CO2 emissions per citizen:")
    print(bottom5_co2)



if __name__ == "__main__":
    data_path = 'Data2.csv'
    df = read_dataset(data_path)

    print_exploring(df)

    df = remove_typo(df)

    df = clean_up(df)

    df = fix_negative(df)

    df = fix_NaN(df)

    create_boxplot(df)

    create_hist(df)

    plt.show()

    df = add_population_density(df)

    number_two(df)
    number_three(df)
    number_four(df)
    number_five(df)
    number_six(df)

    
