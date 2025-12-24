# connection.py

import psycopg2
from configparser import ConfigParser
import os

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    base_path = os.path.dirname(__file__)
    
    # Create the full path to the .ini file
    full_path = os.path.join(base_path, filename)
    if not os.path.exists(full_path):
        raise Exception(f'File {filename} not found at {full_path}')
    
    parser.read(full_path)
    
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def connect():
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    return connection


connect()