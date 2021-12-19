import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('anos_vida.csv', delimiter=',')

#column separed life expectancy

life_exp = data['Life Expectancy']

#maximum data for life expectancy for country
max_life_exp = np.amax(life_exp)
print('max data is ')
print(max_life_exp)

#minimum data for life expectancy for country
min_exp_life = np.amin(life_exp)
print('minimum data is')
print(min_exp_life)

#range for data for life expectancy for countries
range_exp_life = max_life_exp - min_exp_life
print('range for data is')
print(range_exp_life)

#mean for life expectancy for country
life_exp_mean = life_exp.mean()
print('mean for data is')
print(life_exp_mean)

#median
life_exp_median = life_exp.median()
print('median for this data is')
print(life_exp_median)

#quartiles for life expectancy
life_exp_q1 = np.quantile(life_exp, 0.25)
life_exp_q2 = np.quantile(life_exp, 0.5)
life_exp_q3 = np.quantile(life_exp, 0.75)
print(f'Q1 for life exp is {life_exp_q1}')
print(f'Q2 for this data is {life_exp_q2}')
print(f'Q3 for this data is {life_exp_q3}')


#create a variable for gdp data
gdp_data = data['GDP']

#minimum for GDP
min_gdp = np.amin(gdp_data)
print('minimum data is')
print(min_gdp)

#maximum for GDP
max_gdp = np.amax(gdp_data)
print('maximum data for gdp is')
print(max_gdp)

#range for GDP
range_gdp = max_gdp - min_gdp
print('range for gdp is')
print(range_gdp)

#mean for gdp
gdp_mean = gdp_data.mean()
print('mean for GDP is')
print(gdp_mean)

#median for GDP
gdp_median = gdp_data.median()
print('a median for GDP is')
print(gdp_median)

#quartiles for gdp
gdp_q1 = np.quantile(gdp_data, 0.25)
gdp_q2 = np.quantile(gdp_data, 0.5)
gdp_q3 = np.quantile(gdp_data, 0.75)
print(f'Q1 for life exp is {gdp_q1}')
print(f'Q2 for this data is {gdp_q2}')
print(f'Q3 for this data is {gdp_q3}')

