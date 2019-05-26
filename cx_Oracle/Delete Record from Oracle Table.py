# -*- coding: utf-8 -*-  
"""Created on Wed May 15 17:40:26 2019
@author: AcharyaA
"""

########### insert into oracle table 
import cx_Oracle

con = cx_Oracle.connect('***/****@*****')

def insert_dept(n_dept, s_dname,s_loc):
    cur= con.cursor()
    cur.execute("insert into dept(deptno, dname, loc) values(:1,:2,:3)",(n_dept,s_dname,s_loc))
    cur.close()
    con.commit()
    con.close()
# call the insert_dept function
try:
    insert_dept(7,'testdept', 'testloc')
except Exception as e:
    print(e)

