from factory_creator import FactoryCreator

def main():
    bankName = input("Enter the name of Bank from where you want to take loan amount: ")
    loanName = input("Enter the type of loan you want: ")

    bankFactory = FactoryCreator.getFactory("Bank")

    if bankFactory is None:
        return
    bank = bankFactory.getBank(bankName)

    if bank is None:
        return

    rate = float(input(f"Enter the interest rate for {bank.getBankName()}: "))
    loanAmount = float(input("Enter the loan amount you want to take: "))
    years = int(input("Enter the number of years to pay your loan: "))

    print(f"\nYou are taking the loan from {bank.getBankName()}")

    loanFactory = FactoryCreator.getFactory("Loan")
    if loanFactory is None:
        return

    loan = loanFactory.getLoan(loanName)

    if loan is None:
        return

    loan.getInterestRate(rate)
    loan.calculateLoanPayment(loanAmount, years)

if __name__ == "__main__":
    main()
