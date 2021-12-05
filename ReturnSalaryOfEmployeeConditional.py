# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 15:02:29 2021

@author: scarl
"""

import pandas as pd
import numpy as np

#Create dynamic numpy array
c= np.array([[2,3,1800],[2,4,1200],[2,5,2000],[1,13,4000],[1,2,3000],[10,1,1200]])

print("Your input data Manager,Employee,Salary\n",c)
#Get all the list of managers
x = np.unique(c[:,0])

#Convert numpy array to dataframe this is whole data
c= pd.DataFrame(c)    
        
#Get ManagerSalary       
_N_arr=[]   
for i, row in c.iterrows():
    
    if c.iloc[i][1] in x:
        _N_arr.append([c.iloc[i][1],c.iloc[i][2]])

        
print("\n\nYour Isolated Manager salary",_N_arr)

Final=[]
#Now goes our stored procedure logic
for i, row in pd.DataFrame(_N_arr).iterrows():
    #print(_N_arr[i][1])
    #Foreach of the manager check thier employees and see if salary greater
    
    for j in range(0,len(c)):
        if(c[0][j] == _N_arr[i][0] and (c[2][j] > _N_arr[i][1]) ):
            Final.append([c[1][j],c[2][j], _N_arr[i][0], _N_arr[i][1]])
            #print(c[1][j],c[2][j], _N_arr[i][0], _N_arr[i][1])
                        
print("\n\nYour Employees salary whose salary is greater than thier manager\n Employee|Salary|Manager|Salary\n",Final)          
    


