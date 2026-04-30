class BankAccount:
    def __init__(self, account_number, owner_name, balance = 0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.transactions = []

#####################################

    def get_account_number(self):
        return self.account_number

    def get_owner_name(self):
        return self.owner_name

    def set_owner_name(self, name):
        self.owner_name = name

    def get_balance(self):
        return self.balance

######################################

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append("Пополнение deposit +" + str(amount))

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append("Снятие -" + str(amount))

    def check_balance(self):
        return self.balance


    def get_transaction_history(self):
        for action in self.transactions:
            print(action)


    def get_account_info(self):
        return "Счет: " + str(self.account_number) + ", Владелец: " + self.owner_name + ", Баланс: " + str(self.balance)


    def get_transaction_count(self):
        return len(self.transactions)

    def __str__(self):
        return "Account #" + str(self.account_number) + " (" + self.owner_name + "): $" + str(self.balance)

    def __iadd__(self, amount):
        self.deposit(amount)
        return self

    def __isub__(self, amount):
        self.withdraw(amount)
        return self

    def __len__(self):
        return len(self.transactions)

############################

class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance = 0, interest_rate = 0.01):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def deposit(self, amount):
        interest = amount * self.interest_rate
        total = amount + interest 
        self.balance += total
        self.transactions.append("Пополнение +" + str(amount) + " проценты " + str(interest))

    def get_account_info(self):
        return super().get_account_info() + ", ставка: " + str(self.interest_rate)

    def get_transaction_history(self):
        i = 1
        for t in self.transactions:
            print(str(i) + ". " + t)
            i += 1










# пример
acc = BankAccount(111, "Ivan", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc)
acc.get_transaction_history()
print("Кол-во операций:", len(acc))

print("\n--- Savings ---")
sav = SavingsAccount(222, "Anna", 2000, 0.05)
sav.deposit(1000)
print(sav.get_account_info())
sav.get_transaction_history()
