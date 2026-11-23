# CQ13 
class SavingsAccount:
    # This class will take the account id, current balance, previous balance, and annual interest rate for a savings account
    def __init__(self, account_id: int, balance: float, previous_balance: float, annual_interest_rate: float) -> None:
        self.account_id = account_id
        self.balance = balance
        self.previous_balance = previous_balance
        self.annual_interest_rate = annual_interest_rate
    # This function will change the interest rate of the savings account by passing the new one as an argument
    def set_interest_rate(self, new_interest_rate: float) -> None:
        self.annual_interest_rate = new_interest_rate
    # This will return the monthly interest rate by dividing the annual by 12
    def get_monthly_interest_rate(self) -> float:
        return (self.annual_interest_rate / 12)
    # This will get the total monthly interest by taking the monthly interest and multiplying it by the current balance
    def get_monthly_interest(self) -> float:
        return self.balance * (self.get_monthly_interest_rate() / 100)
    # This will take the percent change from the previous balance to the current balance
    def get_balance_change_percent(self) -> float:
        return ((self.balance - self.previous_balance) / self.previous_balance) * 100
    # This will allow the user to pass an withdrawal argument in order to reduce the amount of money in the account
    def withdraw(self, withdraw_amount: float) -> None:
        if withdraw_amount > self.balance:
            return "The current balance is insufficient"
        self.previous_balance = self.balance
        self.balance -= withdraw_amount
    # This allows the user to increase the amount of money in the account by passing the deposit as an argument
    def deposit(self, deposit_amount: float):
        self.previous_balance = self.balance
        self.balance += deposit_amount
    # This prints the current state of the bank account
    def get_state(self):
        print(f"The account id is {self.account_id}")
        print(f"The balance is {self.balance}")
        print(f"The previous balance was {self.previous_balance}")
        print(f"The annual interest rate {self.annual_interest_rate}")
        
        


# This is a handful of the possible operations that can be done using this class
def main():
    my_savings_account = SavingsAccount(1122, 20_000, 18_500, 4.5)
    my_savings_account.withdraw(2_500)
    my_savings_account.deposit(3_000)
    print(f"The id of the account is {my_savings_account.account_id}")
    print(f"The current monthly interest rate is {round(my_savings_account.get_monthly_interest_rate(), 2)}%")
    print(f"The current monthly interest is {round(my_savings_account.get_monthly_interest(), 2)}$")
    print(f"The percent change in assets is {round(my_savings_account.get_balance_change_percent(), 2)}%")




if __name__ == "__main__":
    main()