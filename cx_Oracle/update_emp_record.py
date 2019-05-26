# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:59:55 2019

@author: AcharyaA
"""

import cx_Oracle

con = cx_Oracle.connect('***/****@*****')

def update_salary(n_empno, n_salary):
    cur = con.cursor()
    #cur.execute("Update emp set sal = :n_salary where empno = :n_empno",{'n_empno': (n_empno), 'n_salary': (n_salary)})
    statement = 'Update emp set sal = :n_salary where empno = :n_empno'
    cur.execute(statement, {'n_empno':n_empno, 'n_salary':n_salary})
    n_count = cur.rowcount
    con.commit()
    cur.close()
    con.close()
    return n_count
    
########## DPI 1010: Database not connected error while call from another piece of code
try:
    if update_salary(8, 9999)==0:
        print('Update failed.')
    else:
        print('Update success.')
except Exception as e:
    print(e)
    
    
    
