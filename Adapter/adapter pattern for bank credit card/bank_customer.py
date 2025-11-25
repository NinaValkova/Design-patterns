from credit_card import CreditCard
from bank_details import BankDetails


# Adapter - the middle piece that lets them connect
class BankCustomer(CreditCard):

    def __init__(self, bank_details: BankDetails):
        self.bank_details = bank_details

    def give_bank_details(self):
        acc_holder_name = input("Enter the account holder name: ")
        acc_number = int(input("Enter the account number: "))
        bank_name = input("Enter the bank name: ")

        self.bank_details.set_acc_holder_name(acc_holder_name)
        self.bank_details.set_acc_number(acc_number)
        self.bank_details.set_bank_name(bank_name)

    def get_credit_card(self):
        return (
            f"The account number {self.bank_details.acc_number} "
            f"of {self.bank_details.acc_holder_name} in "
            f"{self.bank_details.bank_name} bank is valid for credit card issuing."
        )
