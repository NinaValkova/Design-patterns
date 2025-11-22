from planFactory import PlanFactory


def main():
    planFactory = PlanFactory()

    typePlan = input("Enter the name of plan for which the bill will be generated: ")

    units = int(
        input("Enter the number of units for which the bill will be calculated: ")
    )

    plan = planFactory.getPlan(typePlan)

    if not plan:
        print("Invalid plan type!")
        return

    plan.getRate()
    plan.calculateBill(units)


if __name__ == "__main__":
    main()
