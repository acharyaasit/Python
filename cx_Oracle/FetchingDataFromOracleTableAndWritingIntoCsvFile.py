# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:42:46 2019

@author: AcharyaA
"""

########## FetchingDataFromOracleTableAndWritingIntoCsvFile 

#connect schema 
con = cx_Oracle.connect('***/****@***')
cursor = con.cursor()

csv_file = open("C:\MyFolder\Python\cx_Oracle\client.csv", "w")

writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
r = cursor.execute("select * from scw.d_client  where rownum<=10")

for row in cursor:
    writer.writerow(row)

cursor.close()
con.close()
csv_file.close()