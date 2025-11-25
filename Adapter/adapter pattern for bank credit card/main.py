from bank_customer import BankCustomer
from bank_details import BankDetails

if __name__ == "__main__":
    bank_details = BankDetails()
    credit_card_adapter = BankCustomer(bank_details)

    credit_card_adapter.give_bank_details()
    print(credit_card_adapter.get_credit_card())
