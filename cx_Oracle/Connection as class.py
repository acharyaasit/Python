# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:18:53 2019

@author: AcharyaA
"""

import cx_Oracle

class Oracle(object):

    def connect(self, username, password, hostname, port, servicename):
        """ Connect to the database. """

        try:
            self.db = cx_Oracle.connect(username, password
                                , hostname + ':' + port + '/' + servicename)
        except cx_Oracle.DatabaseError as e:
            # Log error as appropriate
            raise

        # If the database connection succeeded create the cursor
        # we-re going to use.
        print('Database Connection is Succeeded !!!')
        self.cursor = self.db.cursor()

    def disconnect(self):
        """
        Disconnect from the database. If this fails, for instance
        if the connection instance doesn't exist, ignore the exception.
        """

        try:
            self.cursor.close()
            self.db.close()
        except cx_Oracle.DatabaseError:
            pass

    def execute(self, sql, bindvars=None, commit=False):
        """
        Execute whatever SQL statements are passed to the method;
        commit if specified. Do not specify fetchall() in here as
        the SQL statement may not be a select.
        bindvars is a dictionary of variables you pass to execute.
        """

        try:
        
             
            try:
                if sql[0:3].lower() in ["cre","dro","tru"]:
                    self.cursor.execute(sql)
                    lower_str = sql[0:3].lower()
                    if lower_str == 'cre':
                        print ('Table testt created')
                    elif lower_str == 'dro':
                        print ('Table testt dropped')
                    elif lower_str == 'tru':
                        print ('Table testt truncated')
            except cx_Oracle.DatabaseError as exception:
                print ('Error in DDL')
                #printException (exception)
                #exit (1)  
          
            try:
                if sql[0:3].lower() in ["ins","upd","del"]:
                    self.cursor.execute(sql, bindvars)
                    lower_str = sql[0:3].lower()
                    if lower_str == 'ins':
                        print ('Table testt inserted')
                    elif lower_str == 'upd':
                        print ('Table testt updated')
                    elif lower_str == 'del':
                        print ('Table testt deleted')
                        
            except cx_Oracle.DatabaseError as exception:
                print ('Error in DML')
                #printException (exception)
                #exit (1) 

            
        except cx_Oracle.DatabaseError as e:
            # Log error as appropriate
            raise

        # Only commit if it-s necessary.
        if commit:
            self.db.commit()


if __name__ == '__main__':
    
    oracle = Oracle()
    oracle.connect('***8','****','*****','1521','********')

    try:
        # No commit as you don-t need to commit DDL.
       
        oracle.execute("""Drop table testt""",{"arg_1":''},False)
        oracle.execute("""Create table testt (name varchar2(100))""",{"arg_1":''},False)
        
        # DML Statement example
        oracle.execute("""Insert into testt(name) values(:arg_1)""",{"arg_1":'aaa'},True)
        oracle.execute("""Update testt set name =:arg_1 where name = :arg_2""",{"arg_1":'bbb',"arg_2":'aaa'},True)
        #oracle.execute("""delete from testt where name=:arg_1""",{"arg_1":'aaa'},True)

    # Ensure that we always disconnect from the database to avoid
    # ORA-00018: Maximum number of sessions exceeded. 
    finally:
        oracle.disconnect()
        
   
#import cx_Oracle
#class Example(object):
#    def connect(self, username, password, hostname, port, servicename):
#        """ Connect to the database. """
#
#        try:
#            self.db = cx_Oracle.connect(username, password
#                                , hostname + ':' + port + '/' + servicename)
#        except cx_Oracle.DatabaseError as e:
#            # Log error as appropriate
#            raise
#
#if __name__ == '__main__':
#     e=Example()
#     e.connect('***8','****','*****','1521','********')
