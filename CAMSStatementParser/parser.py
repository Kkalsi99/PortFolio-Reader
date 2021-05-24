from typing import List

import camelot
import camelot.core as camelotTable
import re

from PyPDF2.utils import PdfReadError


class Parser:
    def __init__(self, filename, password):
        self.filename = filename
        self.password = password

    def getPdfTables(self, firstPage=False, parseTransaction=True) -> camelotTable.TableList:
            if firstPage:
                if not parseTransaction:
                    tables = camelot.read_pdf(self.filename, password=self.password, pages="1", flavor="stream",
                                              table_regions=['10,800,600,600'])
                else:
                    tables = camelot.read_pdf(self.filename, password=self.password, pages="1", flavor="stream",
                                              table_regions=['10,200,600,600'], columns=['60,350,410,470,520'])
            else:
                tables = camelot.read_pdf(self.filename, password=self.password, pages="2-end", flavor="stream",
                                          columns=['60,350,410,470,520'])

            return tables

    def getUserInfo(self) -> dict:
        try:
            tables = self.getPdfTables(True, False)
        except PdfReadError as error:
            print(str(error) + ", Please check your password!")
            return None  # if password is incorrect function will return None
        userInfo = list()  # list of tables object
        userInfoStr = list()  # list of strings in tables objects
        userInfo = tables[0].df[0]
        for info in userInfo:
            if info == "":
                continue
            else:
                userInfoStr.append(str(info).replace(";", ""))

        Len = userInfoStr.__len__()  # length of userInfoStr

        # Email
        email = re.search("\w+@+\w+\.+\w+", userInfoStr[0])
        print(email.group(0))

        # Name
        name = re.search("[a-zA-Z\s]+", userInfoStr[1])
        print(name.group(0))

        # address
        address = ""
        for i in range(2, Len - 1):
            address = "".join([address, userInfoStr[i], " "])
        print(address)

        # phone
        if re.search("\+", userInfoStr[Len - 1]):
            phone = re.search("\+\d{12}", userInfoStr[Len - 1])
        else:
            phone = re.search("\d{10}", userInfoStr[Len - 1])
        print(phone.group(0))

        userInfoDict = dict()  # user info dictionary and return value
        userInfoDict["email"] = email.group(0)
        userInfoDict["name"] = name.group(0)
        userInfoDict["address"] = address
        userInfoDict["phone"] = phone.group(0)

        return userInfoDict

    def getAmcList(self) -> list:
        try:
            tables = self.getPdfTables(True, False)
        except PdfReadError as error:
            print(str(error) + ", Please check your password!")
            return None  # if password is incorrect function will return Nonegit
        transactionInfo = tables[0].df
        print(transactionInfo[0])

        pass
