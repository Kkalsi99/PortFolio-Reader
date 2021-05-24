from Models.user import User
from Models.MFModels.portfolio import Portfolio
from Models.MFModels.amc import Amc
from Models.MFModels.folio import Folio
from Models.MFModels.fund import Fund
from Models.MFModels.transaction import Transaction, Type as transactionType
from CAMSStatementParser.parser import Parser
from datetime import date

parser = Parser("/home/kghost/test.pdf", "Qwerty@992")
parser.getUserInfo()
# parser.getAmcList()

user = User("Kashish Kalsi", "PanNumber", "Email@email.com","7508081375", "AddressOfUser")
user.portfolio = Portfolio()

amc = Amc("Axis Mutual Fund")
folio = Folio("155asas")
fund = Fund("Axis Bluechip","abc123")
transaction = Transaction(transactionType.BUY, 10.001, 120, date(2020, 5, 15))

fund.transactions.append(transaction)
folio.funds.append(fund)
amc.folios.append(folio)


user.portfolio.amcs.append(amc)
