import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
from scipy.stats import chi2_contingency
data = pd.read_csv("C:/Users/HP/PycharmProjects/Excelrdatascience/Costomer+OrderForm.csv")
data.head()
print(data['Phillippines'].value_counts(),data['Indonesia'].value_counts(),data['Malta'].value_counts(),data['India'].value_counts)
# Make a contingency table
obs=np.array([[271,267,269,280],[29,33,31,20]])
obs
stat, p, dof, expected = chi2_contingency(obs)
stat
p
print('dof=%d' % dof)
print(expected)
from scipy.stats import chi2
alpha = 0.05
prob=1-alpha
critical = chi2.ppf(prob, dof)
print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
if abs(stat) >= critical:
	print('Dependent (reject H0),variables are related')
else:
	print('Independent (fail to reject H0), variables are not related')
print('significance=%.3f, p=%.3f' % (alpha, p))
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')