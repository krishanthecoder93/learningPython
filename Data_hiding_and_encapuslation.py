class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_balance(self, entered_pin):
        if entered_pin == self.__pin:
            print(f"Your balance is ₹{self.__balance}")
        else:
            print("Incorrect PIN")

    def deposit(self, entered_pin, amount):
        if entered_pin == self.__pin:
            self.__balance += amount
            print(f"₹{amount} deposited successfully!\n Updated balance is {self.__balance}")
        else:
            print("Incorrect PIN,Please enter correct PIN")

atm = ATM(1234, 25000)
atm.check_balance(1234)

print("__-----------------____")

atm.deposit(1234, 20000)
atm.check_balance(9999)
