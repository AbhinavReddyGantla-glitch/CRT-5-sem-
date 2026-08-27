class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def credit(self,amount):
        self.__balance += amount
    def debit(self,amount):
        self.__balance -= amount
    def view(self):
        print("Balance:",self.__balance)

b = Bank(1000)
b.view()
b.credit(500)
b.debit(200)
b.view()