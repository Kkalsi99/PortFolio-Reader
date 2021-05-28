from Models.user import User
from Models.MFModels.portfolio import Portfolio
from Models.MFModels.amc import Amc
from Models.MFModels.folio import Folio
from Models.MFModels.fund import Fund
from Models.MFModels.transaction import Transaction, Type as transactionType

import camelot
import camelot.core as camelotTable
import re

from PyPDF2.utils import PdfReadError


class Parser:
    def __init__(self, filename, password):
        self.filename = filename
        self.password = password
        self.user: User = None

    def getPdfTables(self, firstPage=False, parseTransaction=True) -> camelotTable.TableList:
        if firstPage:
            if not parseTransaction:
                tables = camelot.read_pdf(self.filename, password=self.password, pages="1", flavor="stream",
                                          table_regions=['10,800,600,600'])
            else:
                tables = camelot.read_pdf(self.filename, password=self.password, pages="1", flavor="stream",
                                          table_regions=['10,600,600,10'])
        else:
            tables = camelot.read_pdf(self.filename, password=self.password, pages="2", flavor="stream", )

        return tables

    def getUserInfo(self):

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

        user = User(name.group(0), "", email.group(0), phone.group(0), address)
        self.user = user

    def getAmcList(self) -> User:
        try:
            tables = self.getPdfTables(True, True)
        except PdfReadError as error:
            print(str(error) + ", Please check your password!")
            return None  # if password is incorrect function will return None

        tableLen = tables.__len__()

        transactionInfo = tables[tableLen - 1].df
        firstColumn = tables[tableLen - 1].df[0]

        allAmcs = ["axis mutual fund", "invesco mutual fund", "aditya birla sun life mutual fund", "baroda mutual fund",
                   "mirae asset mutual fund"]  # this contains all the name of amcs that are registered

        amcList = list()  # Total amc in cams file
        folioList = list()
        panNumber = ""
        fundList = list()
        amc: Amc = None
        folio: Folio = None
        fund: Fund = None
        transaction: Transaction = None
        for i in range(0, tables[tableLen - 1].shape[0]):

            for j in range(0, tables[tableLen - 1].shape[1]):
                if re.search('\w\w\wP\w\d\d\d\d\w\w', tables[tableLen - 1].df[j][i]):
                    panNumber = re.search('\w\w\wP\w\d\d\d\d\w\w', tables[tableLen - 1].df[j][i])
                    panNumber = panNumber.group(0);
                if tables[tableLen - 1].df[j][i].lower() in allAmcs:
                    amcName = tables[tableLen - 1].df[j][i]
                    if amc is None:
                        amc = Amc(amcName)
                    else:
                        amcList.append(amc)
                        amc = Amc(amcName)
                    break
                if re.search("Folio No: \d+ / \d", tables[tableLen - 1].df[j][i]):
                    if tables[tableLen - 1].df[j][i] not in folioList:
                        folioNumber = tables[tableLen - 1].df[j][i]
                        if folio is None:
                            folio = Folio(folioNumber)
                        else:
                            amc.folios.append(folio)
                            folio = Folio(folioNumber)
                    break
                if re.search("^[a-zA-Z0-9]+-[a-zA-Z ]+-[a-zA-Z -]+", tables[tableLen - 1].df[j][i]):
                    fundName = re.search("^[a-zA-Z0-9]+-[a-zA-Z ]+-[a-zA-Z -]+", tables[tableLen - 1].df[j][i])
                    fundName = fundName.group(0)
                    # -[a-zA-Z ] + -[a-zA-Z -] +
                    if fund is None:
                        fund = Fund(fundName)
                    else:
                        folio.funds.append(fund)
                        fund = Fund(fundName)

                    break
                if re.search("^\d\d-\w\w\w-\d\d\d\d$", tables[tableLen - 1].df[j][i]):
                    jt = j
                    transactionList = list()
                    while jt < tables[tableLen - 1].shape[1]:
                        cost = tables[tableLen - 1].df[jt][i]
                        if cost != "":
                            transactionList.append(cost)
                        jt = jt + 1
                        if len(transactionList) == 4:
                            transaction = Transaction(transactionList[0], transactionList[1], transactionList[2],
                                                      transactionList[3])
                        fund.transactions.append(transaction)

                    break

        portfolio = Portfolio()
        portfolio.amcs = amcList
        self.user.pan = panNumber
        self.user.mf_portfolio = portfolio
        return self.user
        pass
