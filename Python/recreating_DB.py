"""recreating_DB

The goal of this file to enable a creation of the inventory database automatically.
"""

"""Imports"""
import mysql.connector
#import mysql.connector.plugins

"""Connecting to MySQL"""
cnx = mysql.connector.connect(user='root',
                             password='aRandomPassword',
                             host='localhost')

cursor = cnx.cursor()

def execute_scripts_from_file(filepath: str):
    """Opens an SQL script an runs every query in it. In case of an error, the function will print the error message to the terminal. 
    
    Parameters
    ----------
    filepass: str
        The full path to the sql query.
    """
    fd = open(filepath, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except IOError as msg:
            print("Command skipped: ", msg)

"""Running SQL scripts to create the database"""

execute_scripts_from_file('C:/Users/yoavw/Documents/GitHub/Portfolio/Portfolio/Inventory Project/MySql/creating_database.sql') # Creating the WAREHOUSE database
cnx.commit()

execute_scripts_from_file('C:/Users/yoavw/Documents/GitHub/Portfolio/Portfolio/Inventory Project/MySql/creating_inventory_table.sql') # Creating tables
cnx.commit()