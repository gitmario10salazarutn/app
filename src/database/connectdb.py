# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:15:31 2022

@author: Mario
"""

#import pyodbc as conn
from decouple import config
import mysql.connector as c

"""
def connect_sqlserver(hostname, dbname, username, password):
    try:
        conexion = conn.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                hostname + ';DATABASE=' + dbname + ';UID=' + username + ';PWD=' + password)
        return conexion
    except Exception as ex:
        # Atrapar error
        return "Error to connect to SQL Server: {0}".format(ex)
"""

def get_points(username, password, hostname, database):
    try:
        db = c.connect(user="{0}".format(username), password="{0}".format(password),
                       host="{0}".format(hostname), database="{0}".format(database))
        return db
    except Exception as ex:
        return "Error to connect to MySQL: {0}".format(ex)


def get_connection():
    try:
        return get_points(
            config('USER_NAME'),
            config('PASSWORD'),
            config('HOSTNAME'),
            config('DATABASE')
        )
    except Exception as ex:
        raise ex


print(get_connection())

"""
print(
    config('USER_NAME'),
    config('PASSWORD'),
    config('HOSTNAME'),
    config('DATABASE')
)
print(get_connection_MySQL())
"""

"""
def get_connectionS():
    try:
        return connect_sqlserver(
            config('HOST'),
            config('DB'),
            config('USER'),
            config('PASS')
        )
    except Exception as ex:
        raise ex
"""