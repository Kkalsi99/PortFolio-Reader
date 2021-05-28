from Models.user import User
from Models.MFModels.portfolio import Portfolio
from Models.MFModels.amc import Amc
from Models.MFModels.folio import Folio
from Models.MFModels.fund import Fund
from Models.MFModels.transaction import Transaction, Type as transactionType
from CAMSStatementParser.parser import Parser
from datetime import date

parser = Parser("/home/kghost/test.pdf", "Qwerty@99")
parser.getUserInfo()
user = parser.getAmcList()






