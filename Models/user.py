from Models.MFModels.portfolio import Portfolio


class User:
    name: str = None
    pan: str = None
    email: str = None
    phone: str = None
    address: str = None
    mf_portfolio: Portfolio = None

    def __init__(self,name,pan,email,phone,address):
        self.name = name
        self.pan = pan
        self.email = email
        self.phone = phone
        self.address = address
        pass



    pass
