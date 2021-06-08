from database.database import Database
from util.amcList import amclist
import requests


def sendData():
    r = requests.get("https://www.amfiindia.com/spages/NAVAll.txt")
    db = Database("test")
    data = r.text.split('\n')

    amc = ""

    for row in data:
        row = row.replace('\r', '')
        if row in amclist:
            amc = row

        elif amc:
            if row != "":
                # db.insert_data(row+';'+amc)
                db.update_data(row + ';' + amc)
    db.commit()


pass
