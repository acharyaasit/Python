# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:14:49 2019

@author: AcharyaA
"""

###### create this object in oracle table , insert data to it, procedure 

# create table emp (empno number, comm number , sal float)

# insert into emp (empno, comm,sal)
# values (1, 4,11)

# CREATE OR REPLACE PROCEDURE compute_sal (i_empno IN emp.empno%TYPE,
# o_total_salary OUT NUMBER)
# IS
# CURSOR c_emp (p_empno emp.empno%TYPE)
# IS
# SELECT sal, comm
# FROM emp
# WHERE empno = p_empno;

# v_sal NUMBER;
# v_comm NUMBER;
# BEGIN
# OPEN c_emp (i_empno);

# FETCH c_emp
# INTO v_sal, v_comm;

# CLOSE c_emp;

# o_total_salary := (v_sal + NVL (v_comm, 0));
# END compute_sal;


import cx_Oracle

con = cx_Oracle.connect('***/****@*****')
cur = con.cursor()
n_empno=1
n_total_salary =cur.var(cx_Oracle.NUMBER)
cur.callproc('compute_sal',[n_empno,n_total_salary])
print ("Total salary for the employee: ", n_empno, "is: ", n_total_salary.getvalue())
cur.close()
con.close()
