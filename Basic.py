# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:08:21 2020

"""


import pandas as pd 
import numpy as np

#Downloading data into python
dat=pd.read_excel('.\Basic Statistic.xlsx')

# Checking data types
dat.dtypes

# Replace text with numbers
dat=dat.replace('No Data',0)

# Calculating the central tendency: mean, median, mode
# Flow
mean=dat['Flow'].mean()
median=dat['Flow'].median()
mode=dat['Flow'].mode()

# Output 
print('The mean of the Flow is', np.round(mean,1),' m3/h' )
print('The mode of the Flow is', np.round(mode,1),' m3/h' )
print('The median of the Flow is', np.round(median,1),' m3/h' )

# Temperature
mean=dat['Temp'].mean()
median=dat['Temp'].median()
mode=dat['Temp'].mode()

# Output 
print('The mean of the Temp is', np.round(mean,1),' 0C' )
print('The mode of the Temp is', np.round(mode,1),' 0C' )
print('The median of the Temp is', np.round(median,1),' 0C' )



# Calculating dispersion: variance, standard deviation, range
# Flow
std=dat['Flow'].std()
var=dat['Flow'].var()
R=dat['Flow'].max()-dat['Flow'].min()


#Output
print('The std of the Flow is', np.round(std,2),' m3/h' )
print('The var of the Flow is', np.round(var,2),' [m3/h]*2' )
print('The Range of the Flow is', np.round(R,2),' m3/h' )

#Calculating basic statistics in dynamics
#Getting categorical variable from timestamp - months
dat['month_year']=dat['Timestamp'].dt.strftime('%m-%y')

#The statistics to be calculated in the from of a list
stat_list=['mean','sum','median','var','std','min','max']

#Creating groupped DataFrame.
dat_tab=dat.groupby('month_year').agg({'Flow':stat_list,'Temp':stat_list})

#The columns' names of the DataFrame
column_list=['Flow_'+col for col in stat_list]+['Temp_'+col for col in stat_list]

#Assigning these column names to our table (DataFrame)
dat_tab.columns=column_list

#Calculating the range of flow and temperature
dat_tab['Temp_range']=dat_tab['Temp_max']-dat_tab['Temp_min']
dat_tab['Flow_range']=dat_tab['Flow_max']-dat_tab['Flow_min']

#Rounding
dat_tab=np.round(dat_tab,1)

#Saving information to excel file
writer=pd.ExcelWriter('./Stat_final.xlsx')
dat_tab.to_excel(writer,'Data')
writer.save()



