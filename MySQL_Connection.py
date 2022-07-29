#Import the 'pymysql' library that allow us work with DDL, DQL, DML, DLC and TLC commands of SQL
import pymysql

#Define the 'Database' class to work with all operations required to connect with the database
#and querys to retrieve and modify data

class Database:
    def __init__(self):
        #Connect to MySQL database
        self.connection = pymysql.connect(
              host = 'localhost',        #IP adress
              user = 'root',              #Name of the user
              password = '',   #Password
              database = 'empresa_hielo' #The database to connect
            )
        
        self.cursor = self.connection.cursor()
        print('Database connection has been done succesfully\n')
    

#==========================================================================================================
#SELECT Implementation to retrieve data from a table using the following values:
#table : The name of the table you do the query
#column : The attribute you want access, by default is None, this means that all columns will retrieved
#id : The ID of the row, by default is None, this means that all rows will be retrieved
#===========================================================================================================
    def select(self,table, column = None, id = None):
        
        #Select all the columns and rows of the table
        if column is None and id is None:
            sql_statement = 'SELECT * FROM {}'.format(table)
        
        #Select all rows from the 'column' of the table
        elif column is not None and id is None:
            sql_statement = 'SELECT {} FROM {}'.format(column,table)  
        
        #Select all column where ID = 'id' of the table
        elif column is None and id is not None:
            sql_statement = 'SELECT * FROM {} WHERE id = {}'.format(table,id)
        
        
        else:
            sql_statement = 'SELECT {} FROM {} WHERE id = {}'.format(column, table, id)
        
        try:
            self.cursor.execute(sql_statement)
            DQL_SELECT = self.cursor.fetchall()
            
            print('Table: {}\n'.format(table))
            for item in DQL_SELECT:
                print('|',*item)
                print('|________________\n')
            
        except Exception as e:
            raise

#=========================================================================================================
#UPDATE Implementation
#=========================================================================================================
    def update(self,table,column,id,value):
         
         sql_statement = 'UPDATE {} SET {} = {} WHERE ID = {}'.format(table,column,value,id)
         
         try:
             
             self.cursor.execute(sql_statement)
             self.connection.commit()
             
         except Exception as e:
            raise

#========================================================================================================       
#Close the connection from the MySQL server
#=========================================================================================================
    def close(self):
        self.connection.close
        print('Connection has closed')
        
                
        
#Start Connection
database = Database()

#Select the product with the ID = id and the TABLE = table
id = 3
table ='productos'
column = 'cantidad'
value = 13

#Update the database
database.update(table,column,id,value)
#View the table in the database
database.select(table)
#Close connection
database.close()

