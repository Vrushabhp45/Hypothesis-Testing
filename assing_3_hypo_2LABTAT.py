import pandas as pd
import numpy as np
from numpy.random import randn
from scipy.stats import f_oneway
data = pd.read_csv("LabTAT.csv")
print(data.head())

# Anova ftest statistics: stats.f_oneway(column-1,column-2,column-3,column-4)
stat, p= f_oneway(data.iloc[:,0],data.iloc[:,1],data.iloc[:,2],data.iloc[:,3])
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Same distributions (fail to reject H0)')
else:
	print('Different distributions (reject H0)')