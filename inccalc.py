class RoiCalc:
    def __init__(self, income, cost, investment):
        self.income = income
        self.cost = cost
        self.investment = investment
      
class Income():
    def __init__(self, rent=0, laundry=0, storage=0, misc=0):
        self.rental_income = rent
        self.laundry = laundry
        self.storage = storage
        self.misc = misc
    def total_income(self):
        self.rent = int(input("How much do you make from rent per month? "))
        self.laundry = int(input("How much do you make from laundry per month? "))
        self.storage = int(input("How much do you make from storage per month? "))
        self.misc = int(input("How much do you make from miscalaneous charges per month? "))
        self.income = int(self.rent) + int(self.laundry) + int(self.storage) + int(self.misc)
        print(f"Your income from this property is ${self.income} per month.")
        return self.income

class Cost(RoiCalc):
    def __init__(self, loe):
        self.loe = loe
    def cost(self):
        self.cost = 0
        self.loe = {
            "Tax" : int(input('How much do you pay for taxes per month? ')),
            "Insurance" : int(input('How much do you pay for insurance per month? ')),
            'Utilities' : int(input('How much do you pay for utilities per month? ')), 
            'HOA': int(input('How much do you pay for HOA fees per month? ')), 
            'Lawn/Snow' : int(input('How much do you pay for lawn or snow care per month? ')), 
            'Vacancy' : int(input('How much do would you like to save for vacancy per month? ')), 
            'Repairs' : int(input('How much do you pay for repairs per month? ')), 
            'CapEx' : int(input('How much do you save for capital expendetures per month? ')), 
            'Property Management' : int(input('How much do you pay for Property Management per month? ')),
            'Mortgage' : int(input('How much do you pay for your mortgage per month? '))
            } 
        for i in self.loe.values():
            self.cost = self.cost + i
        print(f"Your expenses for this property are ${self.cost} per month.")
        return self.cost

class Investment(RoiCalc):
    def __init__(self, total_investments):
        self.total_investments = total_investments
    def investment(self):        
        self.investment = 0
        self.total_investments = {
            "Down Payment" : int(input('How much was your down payment? ')),
            'Closing Costs' : int(input('How much are the closing costs? ')), 
            'Rehab Budget': int(input('How much is your rebuild budget? '))
            }
        for i in self.total_investments.values():
            self.investment = self.investment + i
        print(f"Your investment cost for this property is ${self.investment}.")
        return self.investment

class Calculator(RoiCalc):
    def __init__(self, income, cost, investment, cash=0):
        super().__init__(income, cost, investment)
        self.cash= cash
    def  __sub__(self, other):
        return self.income - self.cost  
    def cash_flow(self):
        self.CashFlow = (int(self.income) - int(self.cost)) * 12
        print (f"Your cash flow is {self.CashFlow} a year")
        return self.CashFlow
    def roi(self):
        Roi = (int(self.CashFlow) / int(self.investment)) * 100
        print (f"Your Return on ivestment is {Roi}% a year")

t1 = Income()
t2 = Cost([])
t3 = Investment([])
t4 = Calculator(t1.total_income(), t2.cost(), t3.investment())
t4.cash_flow()
t4.roi()