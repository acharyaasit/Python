# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:21:30 2019

@author: AcharyaA
"""
######## Create this function in oracle
# CREATE OR REPLACE FUNCTION calc_percentage (p_1 IN NUMBER, p_2 IN NUMBER)
# RETURN NUMBER
# IS
# n_pct NUMBER := 0;
# BEGIN
# IF p_1 IS NOT NULL
# THEN
# n_pct := (p_1 * p_2) / 100;
# END IF;

# RETURN n_pct;
# END calc_percentage;


import cx_Oracle 
con = cx_Oracle.connect('***/****@*****')
cur =con.cursor()
n_pct = cur.var(cx_Oracle.NUMBER)

n_1=80
n_2=20

cur.callfunc('calc_percentage',n_pct,[n_1,n_2])


print (str(n_2)+"%","  Percent of ", n_1, " is: ", n_pct.getvalue())

cur.close()
con.close()
