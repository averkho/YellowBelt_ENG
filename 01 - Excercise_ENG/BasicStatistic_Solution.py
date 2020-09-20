# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 08:43:35 2020


"""
# Importing the libraries
import pandas as pd
import numpy as np

#Download data

dat=pd.read_excel('./Basic statistics. Exercise.xlsx')

#Checking data types
print(dat.dtypes)

#Efficiency calculation
dat['Efficiency']=dat['Electricity, MW/h']/dat['Gas consumption, km3/h']

'''
The task I: BASIS STATISTIC CALCULATION
'''
#Basic Statistic calculation
#Mean

MEAN=dat.mean()
for i in range(MEAN.shape[0]):
    print('Mean of ',MEAN.index[i],' is ',np.round(MEAN[i],1))
    
# Median
MEDIAN=dat.median()
for i in range(MEDIAN.shape[0]):
    print('Median of ',MEDIAN.index[i],' is ',np.round(MEDIAN[i],1))    
    
# Minimum
MINIMUM=dat[['Electricity, MW/h', 'Gas consumption, km3/h',
       'Efficiency']].min()
for i in range(MINIMUM.shape[0]):
    print('Minimum of ',MINIMUM.index[i],' is ',np.round(MINIMUM[i],1))   
    
#Maximum
MAXIMUM=dat[['Electricity, MW/h', 'Gas consumption, km3/h',
       'Efficiency']].max()
for i in range(MINIMUM.shape[0]):
    print('Maximum of ',MAXIMUM.index[i],' is ',np.round(MAXIMUM[i],1))
    
# Range
RANGE=MAXIMUM-MINIMUM
for i in range(RANGE.shape[0]):
    print('Range of ',RANGE.index[i],' is ',np.round(RANGE[i],1))

#Standard deviation
STD=dat.std()
for i in range(STD.shape[0]):
    print('Standard deviation of ',STD.index[i],' is ',np.round(STD[i],2))

#Variance
VAR=dat.var()
for i in range(VAR.shape[0]):
    print('Standard deviation of ',VAR.index[i],' is ',np.round(VAR[i],4))

#SUM
SUM=dat[['Electricity, MW/h', 'Gas consumption, km3/h']].sum()
for i in range(SUM.shape[0]):
    print('Sum of ',SUM.index[i],' is ',np.round(SUM[i],0))

'''
The task II: The turbine performance in dynamics
'''

#  Year from timestamp
dat['year']=dat['Timestamp'].dt.year

# the list of functions to calculate
stat_list=['mean','median','sum','std','var','min','max']

#Groupped DataFrame
dat_tab=dat.groupby(['year']).agg({'Electricity, MW/h':stat_list,'Gas consumption, km3/h':stat_list,
                                   'Efficiency':stat_list})

#The names of columns for further processing
column_names=[col.split(',')[0] for col in dat.columns][1:-1]

C=list([[col+'_'+ c for c in stat_list] for col in column_names])

col_names=[]
for cols in C:
    for col in cols:
        col_names.append(col)

# Column names assignment
dat_tab.columns=col_names

# Range calculation
dat_tab['Electricity_range']=dat_tab['Electricity_max']-dat_tab['Electricity_min']
dat_tab['Gas consumption_range']=dat_tab['Gas consumption_max']-dat_tab['Gas consumption_min']
dat_tab['Efficiency_range']=dat_tab['Efficiency_max']-dat_tab['Efficiency_min']

# Transposing DataFrame
dat_tab=dat_tab.T

#Rounding DataFrame
dat_tab=np.round(dat_tab,2)

#Saving information to ExcelFile
writer=pd.ExcelWriter('./Basic statistics. Exercise_FINAL.xlsx')
dat_tab.to_excel(writer,'Data')
writer.save()




