import typing

class BankAccount:
    def __init__(self,AccountNumber : str, Balance : float) -> None:
        self.AccountNumber = AccountNumber
        self.Balance = Balance

    def __repr__(self) -> str:
        return f"BankAccount('{self.AccountNumber}',{self.Balance})"

    @classmethod
    def MinBalance(cls,AccountNumber : str , MinimumBalance : float) -> 'BankAccount':
        return cls(AccountNumber, Balance=MinimumBalance)


    def deposite(self, amount : float) -> None:
        if amount <= 0:
            print('Enter amount greater than zero')
        else:
            self.Balance = self.Balance + amount

        print(f"Current Balance : {self.Balance}")

    def withdraw(self, amount):
        if amount <=0:
            print('Enter amount greater than zero')
        if amount > self.Balance:
            print("Insufficient Funds")
        else:
            self.Balance = self.Balance - amount

        print(f"Current Balance : {self.Balance}")

    @property
    def AccountNumber(self) -> str:
        return self.AccountNumber

    @property
    def Balance(self) -> float:
        return self.Balance


class SavingsAccount(BankAccount):
    def __init__(self,AccountNumber : str, Balance : float, OverDraft : float = 10000):
        super().__init__(AccountNumber, Balance)
        self.OverDraft = OverDraft

    def __repr__(self) -> str:
        return f"SavingsAccount('{self.AccountNumber}',{self.Balance}, {self.MinimumBalance}, {self.Overdraft})"

    def BalanceCheck(self, Balance : float, MinimumBalance : float):
        if self.Balance < self.MinimumBalance:
            print("Account Balance is less than min balance")