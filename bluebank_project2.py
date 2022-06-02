# -*- coding: utf-8 -*-
"""
Created on Sun May 29 18:44:00 2022

@author: Swapnil Nawani
"""

import json
import pandas as pd
import matplotlib.pyplot as plt


json_file= open('loan_data_json.json')
data= json.load(json_file)

loandata= pd.DataFrame(data)

import numpy as np

income= np.exp(loandata['log.annual.inc'])

loandata['annual income']= income




# if fico>=300 and fico<400:
#     ficocat='very poor'
# elif fico>=400 and fico<600:
#     ficocat='poor'
# elif fico>=600 and fico<660:
#     ficocat='fair'
# elif fico>=660 and fico<780:
#     ficocat='good'
# elif fico>=780 and fico<850:
#     ficocat='excellent'
# else:
#     ficocat='unknown'   
#     print(ficocat)
 

ficocat=[]
length=len(loandata)
for x in range(0,length):
    
    category= loandata['fico'][x]
    

    if category>=300 and category<400:
        cat='very poor'
    elif category>=400 and category <600:
        cat= 'poor'
    elif category>=600 and category<660:
        cat= 'fair'
    elif category>=660 and category <700:
         cat= 'good'
    elif category>=700:
        
        cat= ' excellent'
    else:
     cat='unknown'
             
    ficocat.append(cat)
ficocat = pd.Series(ficocat)
loandata['fico.category']= ficocat


loandata.loc[loandata['int.rate']> 0.12, 'int.rate.type']='high'
loandata.loc[loandata['int.rate']<= 0.12, 'int.rate.type']='low'




catplot=loandata.groupby(['fico.category']).size()
catplot.plot.bar()
plt.show
    
catplot=loandata.groupby(['purpose']).size()
catplot.plot.bar()
plt.show


xpoint= loandata['annual income']
ypoint =loandata['dti']
plt.scatter(xpoint,ypoint)
plt.show()

loandata.to_csv('loan_cleaned_project2.csv',index=True)