# Import pandas with alias
import pandas as pd
import numpy as np


# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

# fix column birth_year for int
census['birth_year'] = census.birth_year.replace(['missing'], 1967)
census['birth_year'] = census['birth_year'].astype(int)

# add column 'higher tax' for new variable for machine learning in next step
census_values = pd.get_dummies(data=census, columns=['higher_tax'])

mean_income = census['income_year'].mean()
print(mean_income)
median_income = census['income_year'].median()
print(median_income)




#print(census.dtypes)
#ensus.birth_year = census.birth_year.replace(['missing'], 1967)
#print(census.birth_year.unique())

#
#print(census.head())