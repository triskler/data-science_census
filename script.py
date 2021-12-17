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

print('-------Column Income_year data-------')
print('' * 20)
# mean data for income for year
mean_income = round(census['income_year'].mean(), 2)
print(f' *  The average annual income is {mean_income}')
# median
median_income = round(census['income_year'].median(), 2)
print(f' *  The median plotted for the annual income is {median_income}')
# variance
variance_income = round(census['income_year'].var(), 2)
print(f' *  The variance for the annual income is in {variance_income}')
# standard deviation
std_income = round(census['income_year'].std(), 2)
print(f' *  The standard deviation of annual income is {std_income}')

print('' * 20)
print('' * 20)

print('-------Column birth_year data --------')
print('' * 20)

mean_birth = int(census['birth_year'].mean())
print(f' *  The average of the year of birth is {mean_birth}')

median_birth = int(census['birth_year'].median())
print(f' *  The median of the year of birth is {median_birth}')

variance_birth = int(census['birth_year'].var())
print(f' *  The variance of the year of birth is {variance_birth}')

std_birth = int(census['birth_year'].std())
print(f' *  The standard deviation of the year of birth is {std_birth}')
