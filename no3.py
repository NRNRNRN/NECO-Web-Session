class NecobishiBank():

    balance = 0
    
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self,amount):
        print("100万円引き出せた")

    def send(self, amount):
        print("1円送金した！")

    def deposit(self, amount):
        print("1000円預けた")


shonandai_atm = NecobishiBank(100)
shonandai_atm.withdraw(10)
print(shonandai_atm.balance)

yokohama_atm = NecobishiBank(1000)
print("横浜ATM:" + str(yokohama_atm.balance))