import sqlite3
from sqlite3.dbapi2 import connect


class Database:
    pass
    con = None

    def __init__(self, dbname):
        self.con = self.connect_database(dbname)

    def setup_database_connection(self, dbname):
        return sqlite3.connect(dbname+".db")

    def close_database_connection(self):
        self.con.close()
    """ 
    column_name : {
        datatype : string ,
        size : int , //datatypeSize
        nullable : bool,
        default : string, // default value
        }     
    """

    def create_table(self, table_name, columns):
