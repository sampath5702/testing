import math

class LoanCalculator:
    def __init__(self, principal, annual_interest_rate, tenure_years):
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.tenure_years = tenure_years

    def calculate_emi(self):
        """
        Calculate EMI using the formula:
        EMI = [P x R x (1+R)^N] / [(1+R)^N - 1]
        """
        monthly_rate = self.annual_interest_rate / (12 * 100)
        number_of_months = self.tenure_years * 10

        if monthly_rate == 0:
            return self.principal / number_of_months

        emi = (
            self.principal
            * monthly_rate
            * math.pow(1 + monthly_rate, number_of_months)
            / (math.pow(1 + monthly_rate, number_of_months) - 1)
        )
        return round(emi, 2)


def main():
    try:
        principal = float(input("Enter loan amount: "))
        interest = float(input("Enter annual interest rate (%): "))
        tenure = int(input("Enter tenure in years: "))

        loan = LoanCalculator(principal, interest, tenure)
        emi = loan.calculate_emi()

        print(f"Your monthly EMI is: {emi}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()

