# Describe the class "Bank account"

from datetime import datetime as dt
from uuid import UUID, uuid4


class BankAccount:

    def __init__(self, account_name: str, account_unique_id: UUID, balance: float, transactions: list = None):
        self.account_name = account_name
        self.account_unique_id = account_unique_id
        self.balance = balance
        self.transactions = transactions

    def deposit_funds(self, amount_of_deposit: float):
        new_transaction = []
        date = dt.now().strftime('%Y-%m-%d')
        self.balance = self.balance + amount_of_deposit - amount_of_deposit * 0.01
        new_transaction.append(f'Sum: {amount_of_deposit}. Type of transaction: deposit. Current date: {date}.')
        return new_transaction

    def withdrawal_funds(self, sum_of_funds: float):
        new_withdrawal = []
        date = dt.now().strftime('%Y-%m-%d')
        self.balance = self.balance - sum_of_funds - sum_of_funds * 0.01
        new_withdrawal.append(f'Sum: {sum_of_funds}. Type of transaction: withdrawal funds. Current date: {date}.')
        return new_withdrawal

    def get_balance(self):
        return f'Hello, {self.account_name}! Your balance is currently {self.balance}.'


if __name__ == '__main__':

    customer_account = BankAccount('Gaiane Budarieva', uuid4(), 0)
    print(customer_account.account_name, customer_account.account_unique_id)
    print(customer_account.deposit_funds(5500))
    print(customer_account.withdrawal_funds(100))
    print(customer_account.get_balance())
