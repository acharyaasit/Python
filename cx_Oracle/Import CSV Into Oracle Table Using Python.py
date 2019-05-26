# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:40:54 2019

@author: AcharyaA
"""

### Create table in orcle 
# create table new_locations (
#    LOCATION_ID varchar2(100), 
#    STREET_ADDRESS varchar2(100), 
#    POSTAL_CODE varchar2(100), 
#    CITY varchar2(100), 
#    STATE_PROVINCE varchar2(100), 
#    COUNTRY_ID varchar2(100))
#select * from new_locations
#
#truncate table new_locations

import cx_Oracle
import csv

import os

os.chdir("C:\MyFolder\Python\cx_Oracle")  
print("Current Working Directory " , os.getcwd()) 


con = cx_Oracle.connect('***/****@*****')
cur = con.cursor()

with open ("locations.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter ='|')
    # skip first line if header row
    # next(csv_reader)
    for lines in csv_reader:
        cur.execute(
            "insert into new_locations (LOCATION_ID, STREET_ADDRESS, POSTAL_CODE, CITY, STATE_PROVINCE, COUNTRY_ID) values (:1, :2, :3, :4, :5, :6)",
              (lines[0], lines[1], lines[2], lines[3], lines[4], lines[5]))
cur.close()
con.commit()
con.close()


############ Import CSV Using csv.DictReader method


import cx_Oracle
import csv

import os

os.chdir("C:\MyFolder\Python\cx_Oracle")  
print("Current Working Directory " , os.getcwd()) 


con = cx_Oracle.connect('***/****@*****')
cur = con.cursor()

with open("locations.csv", "r") as csv_file:
    fields = ['F_LOCATION_ID', 'F_STREET_ADDRESS', 'F_POSTAL_CODE', 'F_CITY', 'F_STATE_PROVINCE', 'F_COUNTRY_ID']
    csv_reader = csv.DictReader(csv_file, fieldnames=fields, delimiter='|')
    for lines in csv_reader:
        cur.execute(
            "insert into new_locations (LOCATION_ID, STREET_ADDRESS, POSTAL_CODE,"
            " CITY, STATE_PROVINCE, COUNTRY_ID) values (:1, :2, :3, :4, :5, :6)",
            (lines['F_LOCATION_ID'], lines['F_STREET_ADDRESS'], lines['F_POSTAL_CODE'],
             lines['F_CITY'], lines['F_STATE_PROVINCE'], lines['F_COUNTRY_ID']))

cur.close()
con.commit()
con.close()



############## Import CSV With Header Row Using csv.DictReader Method Example
#########  we no need to skip the first header; it will automatically skip the row

import cx_Oracle
import csv

import os

os.chdir("C:\MyFolder\Python\cx_Oracle")  
print("Current Working Directory " , os.getcwd()) 


con = cx_Oracle.connect('***/****@*****')
cur = con.cursor()

with open("locations_wheader.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='|')
    for lines in csv_reader:
        cur.execute(
            "insert into new_locations (LOCATION_ID, STREET_ADDRESS, POSTAL_CODE,"
            " CITY, STATE_PROVINCE, COUNTRY_ID) values (:1, :2, :3, :4, :5, :6)",
            (lines['LOCATION_ID'], lines['STREET_ADDRESS'], lines['POSTAL_CODE'],
             lines['CITY'], lines['STATE_PROVINCE'], lines['COUNTRY_ID']))

cur.close()
con.commit()
con.close()


