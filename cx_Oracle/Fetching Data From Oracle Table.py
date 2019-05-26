# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:49:43 2019

@author: AcharyaA
"""

########## fetching data from oracle table 
import cx_Oracle
import csv

#connect schema 
con = cx_Oracle.connect('***/****@*****')
cursor = con.cursor()


#fetching data from oracle table 
cursor.execute("""select client_nm from ***.d_client  where rownum<=10 """)
for client_nm in cursor:
    print("Values:", client_nm)
    
cursor.close()
con.close()
