# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:19:06 2019

@author: AcharyaA
"""

import csv
import cx_Oracle
con = cx_Oracle.connect('***/****@*****')
cursor = con.cursor()

csv.register_dialect('myDialect',
delimiter = '|',
lineterminator="\n",
quoting=csv.QUOTE_NONE,
skipinitialspace=True)

csv_file = open("info.csv", "w")
writer = csv.writer(csv_file, dialect='myDialect')
r = cursor.execute("SELECT * FROM db_info")

cols = []
for col in r.description:
    cols.append(col[0])
writer.writerow(cols)

for row in cursor:
    writer.writerow(row)

cursor.close()
con.close()
csv_file.close()