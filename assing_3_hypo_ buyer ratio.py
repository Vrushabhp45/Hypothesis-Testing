import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
data=pd.read_csv("C:/Users/HP/PycharmProjects/Excelrdatascience/BuyerRatio.csv")
print(data.head())
df_table=data.iloc[:,1:]
df_table
df_table.values
val=stats.chi2_contingency(df_table)
val
type(val)
tuple
no_of_rows=len(df_table.iloc[0:2,0])
no_of_columns=len(df_table.iloc[0,0:4])
degree_of_f=(no_of_rows-1)*(no_of_columns-1)
print('Degree of Freedom=',degree_of_f)
Expected_value=val[3]
Expected_value
from scipy.stats import chi2
chi_square=sum([(o-e)**2/e for o,e in zip(df_table.values,Expected_value)])
chi_square_statestic=chi_square[0]+chi_square[1]
chi_square_statestic
critical_value=chi2.ppf(0.95,3)
critical_value
if chi_square_statestic >= critical_value:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')
pvalue = 1 - chi2.cdf(chi_square_statestic, 3)
pvalue
if pvalue <= 0.05:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')