from Models.user import User
from Models.MFModels.portfolio import Portfolio
from Models.MFModels.amc import Amc
from Models.MFModels.folio import Folio
from Models.MFModels.fund import Fund
from Models.MFModels.transaction import Transaction,Type as transaction_type
from datetime import date


user = User("Kashish Kalsi","PanNumber","Email@email.com","AddressOfUser")
user.portfolio = Portfolio()

amc = Amc("Axis Mutual Fund")
folio = Folio("155asas")
fund = Fund("Axis Bluechip")
transaction = Transaction(transaction_type.BUY,10.001,120,date(2020,5,15))

fund.transactions.append(transaction)
folio.funds.append(fund)
amc.folios.append(folio)


user.portfolio.amcs.append(amc)

