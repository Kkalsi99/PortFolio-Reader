import sqlite3
from sqlite3 import Error


class Database:
    con = None

    def __init__(self, dbname):
        self.setup_database_connection(dbname)

    def setup_database_connection(self, dbname):
        try:
            self.con = sqlite3.connect(dbname + ".db")

        except Error as e:
            print(e)

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

    def create_table(self, tableName, columns):
        if self.con:
            cur = self.con.cursor()
            # properties = ""
            # for columnName,columnProperties in columns:
            #     properties = properties + columnProperties + ","
            sql = 'CREATE TABLE mutual_fund_NAV (scheme_code text, isin_div_payout text ,isin_div_reinvestment ' \
                  'text,scheme_name text,net_asset_value text,date text,amc_name text)'
            cur.execute(sql)
            self.con.commit()
            pass
        else:
            print("please setup database connection")

    def insert_data(self, data):
        if self.con:
            rowData = data.split(";")
            cur = self.con.cursor()
            if len(rowData) == 7:
                sql = """INSERT INTO mutual_fund_NAV(scheme_code,isin_div_payout,isin_div_reinvestment,scheme_name,
                net_asset_value,date,amc_name) values (?,?,?,?,?,?,?)"""
                cur.execute(sql, rowData)

    def commit(self):
        self.con.commit()

    def select_data(self):
        if self.con:
            cur = self.con.cursor()
            cur.execute("select * from mutual_fund_NAV")
            print(cur.fetchall())

    def update_data(self, data):
        rowData = data.split(";")
        if self.con:
            cur = self.con.cursor()
            if len(rowData) == 7:
                sql = 'UPDATE mutual_fund_NAV set net_asset_value = ?,date=? where scheme_code = rowData[0]'
                updateData = [rowData[-3], rowData[-2]]
                cur.execute(sql, updateData)


pass
