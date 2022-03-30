import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
data=pd.read_csv("C:/Users/HP/PycharmProjects/Excelrdatascience/Cutlets.csv")
print(data.head())
unitA=pd.Series(data.iloc[:,0])
print(unitA)
unitB=pd.Series(data.iloc[:,1])
print(unitB)
# 2-sample 2-tail ttest:   stats.ttest_ind(array1,array2)     # ind -> independent samples
p_value=stats.ttest_ind(unitA,unitB)
print(p_value)
# interpret
alpha = 0.05
if  0.4722394 > alpha:
	print('Same distributions (fail to reject H0)')
else:
	print('Different distributions (reject H0)')