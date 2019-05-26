# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:07:50 2019

@author: AcharyaA
"""

import os
import update_emp_record

os.chdir("C:\MyFolder\Python\cx_Oracle")  
#print("Current Working Directory " , os.getcwd()) 

try:
    if update_emp_record.update_salary(8, 1111)==0:
        print('Update failed.')
    else:
        print('Update success.')
except Exception as e:
    print(e)