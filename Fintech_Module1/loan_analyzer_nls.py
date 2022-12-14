# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# Determine the amount of loans in loan_costs list
number_of_loans = len(loan_costs)
# Print the number of loans from the list
print(f"Number of loans: {number_of_loans:.2f}")

# Sum total of all loans
total_of_loans = sum(loan_costs)
# Print the total value of the loans
print(f"Total sum of loans: {total_of_loans:.2f}")

# Determine average amount of loans price
average_of_loans = total_of_loans / number_of_loans
# Print the average loan amount
print(f"Average amount per loan: {average_of_loans:.2f}")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Extract Future Value from loan dictionary Remaining Months on the loan.
future_value = loan.get("future_value")
# Print future value of loan
print(f"FutureValue of loan is: {future_value:.2f}")
# Extract Remaining Months on the loan from loan dictionary .
months_remain = loan.get("remaining_months")
# Print Months Remaining of loan
print(f"Months Remaining: {months_remain:.2f}")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# Create discount rate (minimum required return) variable of 20%
discount_rate = 0.20
# Calculate fair value using discount rate variable
fair_value = future_value/(1 + discount_rate/12)**months_remain
# print Fair Value
print(f"Fair Value of loan at discount 20%: {fair_value:.2f}")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

# create counter to be able to understand in the print which loan is worth buying
loan_index = -1

# Use for loop to loop through loan_costs list 
for loan in loan_costs:
    # Determine/count which loan gives which result
    loan_index = loan_index + 1
    
    # Determine if current loan cost is lower or equal to fair_value calculation
    if fair_value >= loan:
        # If fair value greater than or equal to the cost, print Loan_number / PV of loan / Fair Value of the Loan 
        print(f"Loan with index {loan_index},  PV is {loan:.2f} FV is {fair_value:.2f} and is worth at least the cost to buy it")
    
    # if fair value is lower than the cost of the loan, print Loan_number / PV of loan / Fair Value of the Loan 
    else:
        print(f"Loan with index {loan_index},  PV is {loan:.2f} FV is {fair_value:.2f} and is too expensive and not worth the price")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.

# Define function to calculate present value with parameters `future_value`, `remaining_months`, and the `annual_discount_rate`
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    # Define present_value calculation
    present_value = future_value/(1 + annual_discount_rate/12)**remaining_months
    # Print present value of new loan
    print(f"The present value of the new loan is: {present_value:.2f}")
    # Return present value to be able to use present value as output of the function. 
    return present_value

# Calculate the present value of the new loan given below.
#  Use an `annual_discount_rate` of 0.2 for this new loan calculation.
discount_rate = 0.2
calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], discount_rate)

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""
# Loans dictionary (Given)
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create empty list called `inexpensive_loans`
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)
    else:
        pass

# Print the `inexpensive_loans` list
print(inexpensive_loans)


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Create a new empty file using variable name 'output_path' to make a file that include all 'inexpensive loans'
with open(output_path,'w',newline='') as csvfile:
    # Return a writer object responsible for converting the user???s data into delimited strings
    csvwriter = csv.writer(csvfile,delimiter=',')
    # write header to first row
    csvwriter.writerow(header)
    # write each row of `loan.values()` from the `inexpensive_loans` list.
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())