# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 01:17:13 2015

@author: Kruthika
"""

import pandas as pd
#import numpy as np 
import matplotlib.pyplot as plt
import statsmodels.api

df = pd.read_csv('LoanStats3d.csv', header=1, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

#Plot the loan data
plt.plot(loan_count_summary)
plt.show()

#Plot out the ACF
statsmodels.api.graphics.tsa.plot_acf(loan_count_summary)
plt.show()
statsmodels.api.graphics.tsa.plot_pacf(loan_count_summary)
plt.show()