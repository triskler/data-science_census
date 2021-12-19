from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data

financial_data = pd.read_csv('financial_data.csv')
print(financial_data.head())


#separado em variaveis para posterior manipulação // separated into variables for further manipulation

month = financial_data['Month']
revenue = financial_data['Revenue']
expenses = financial_data['Expenses']


#criação do primeiro visual mes x receita // creation of the first visual month x revenue

plt.plot(month,revenue)
plt.xlabel('month')
plt.ylabel('amount($)')
plt.title('revenue')
plt.show()

plt.clf()

#criação do segundo visual despesas x mes // creation of second visual expenses x month

plt.plot(month, expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()


#leitura do segundo arquivo 'despesas detalhadas' // reading the second 'detailed expenses' file

expense_overview = pd.read_csv('expenses.csv')
print(expense_overview.head(7))

#criação da variavel com os dados das despesas detalhadas // creation of the variable with detailed expense data

expense_categories = expense_overview['Expense']
proportions = expense_overview['Proportion']

#listas para agregar os dados relevantes

expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]


plt.clf()

#criação do visual em pizza demonstrando as despesas mais relevantes // creation of the pizza look demonstrating the most relevant expenses

plt.pie(proportions, labels=expense_categories)
plt.title('Expenses')
plt.axis('Equal')
plt.tight_layout()
plt.show()

expense_cut = 'salaries'


#leitura de arquivos com os dados dos funcionarios // reading files with employee data

employees = pd.read_csv('employees.csv')
print(employees.head())

#classificados os dados pela coluna produtividade // sorted data by productivity column

sorted_productivity = employees.sort_values(by=['Productivity'])
print(sorted_productivity.head(10))

#decisão!! Colocação da lista dos 100 funcionarios menos produtivos para posterior corte // Placement of the list of the 100 least productive employees for further cutting

employees_cut = sorted_productivity.head(100)
print(employees_cut)


#verificação extra! Analise do tempo de deslocamento dos funcionarios para analise de trabalho remoto pós pandemia //
#extra check! Analysis of staff travel time for post pandemic remote work analysis

commute_times = employees['Commute Time']
commute_times_log = np.log(commute_times)
print(commute_times.describe())

plt.clf()
plt.hist(commute_times_log)
plt.show()