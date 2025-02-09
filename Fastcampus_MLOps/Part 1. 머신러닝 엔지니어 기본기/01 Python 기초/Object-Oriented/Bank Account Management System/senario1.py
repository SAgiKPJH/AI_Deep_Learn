from account import SavingAccount, CheckingAccount
from user import BankUser

user = BankUser("Ami", 1000)
user.deduct_money(200)
account = CheckingAccount(user.get_name(), 200)
user.add_account(account)

user.deduct_money(800)
account2 = SavingAccount(user.get_name(), 800, 0.05)
user.add_account(account2)

account2.unlock()

account2.withdraw(400)
user.add_money(400)

user.deduct_money(400)
account.deposit(400)

user.get_assets()