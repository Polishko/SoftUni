from typing import List


class Account:
    def __init__(self, owner: str, amount: int = 0) -> None:
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = []

    @property
    def balance(self) -> int:
        return self.amount + sum(self._transactions)

    def handle_transaction(self, transaction_amount) -> str:
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self._transactions.append(transaction_amount)

        return f"New balance: {self.balance}"

    def add_transaction(self, amount: int) -> str or handle_transaction:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        return self.handle_transaction(amount)

    def __str__(self) -> str:
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self) -> str:
        return f"Account({self.owner}, {self.amount})"

    def __len__(self) -> int:
        return len(self._transactions)

    def __getitem__(self, index) -> int:
        return self._transactions[index]

    def __reversed__(self) -> iter:
        return reversed(self._transactions)

    def __ge__(self, other) -> bool:
        return self.balance >= other.balance

    def __gt__(self, other) -> bool:
        return self.balance > other.balance

    def __eq__(self, other) -> bool:
        return self.balance == other.balance

    def __add__(self, other) -> "Account":
        new_name = f"{self.owner}&{other.owner}"
        new_amount = self.amount + other.amount
        new_list = self._transactions + other._transactions
        new_instance = Account(new_name, new_amount)
        new_instance._transactions = new_list
        return new_instance
