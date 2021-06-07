from database.database import Database
from util.amcList import amclist
import requests


def sendData():
    r = requests.get("https://www.amfiindia.com/spages/NAVAll.txt")
    db = Database("test")
    data = r.text.split('\n')

    amc = ""
    i = 0

    for row in data:
        row = row.replace('\r','')
        if row in amclist:
            amc = row

        elif amc:
            print(amc)
            if row != "":
                db.update_data(row+';'+amc)
                db.commit()



pass
