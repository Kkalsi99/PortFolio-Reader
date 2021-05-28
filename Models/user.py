from Models.MFModels.portfolio import Portfolio


class User:

    def __init__(self,name,pan,email,phone,address):

        self.name: str = name
        self.pan = pan
        self.email = email
        self.phone = phone
        self.address = address
        self.mf_portfolio: Portfolio
        pass



    pass
