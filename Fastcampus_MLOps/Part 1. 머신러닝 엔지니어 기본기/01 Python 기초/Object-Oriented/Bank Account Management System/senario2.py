from account import SavingAccount, CheckingAccount
from user import BankUser

user = BankUser("Goes", 900)
user.deduct_money(800)
account = CheckingAccount(user.get_name(), 800)
user.add_account(account)

user.deduct_money(100)
account2 = SavingAccount(user.get_name(), 100, 0.06)
user.add_account(account2)

try:
    account.withdraw(800)
except ValueError:
    account.update_limit(800)
    account.withdraw(800)
finally:
    user.add_money(800)

user.get_assets()