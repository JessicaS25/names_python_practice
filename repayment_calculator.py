#This programme will calculate the investment on a property and calculate home loan repayments
import math
print ("investment - to calculate the amount of interest you'll earn on your investment bond")
print ("bond - to calculate the amount you'll have to pay on a home loan")

#Selection of investment or bond calculation
user_selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
#This prints an error message if too many or too few characters are entered
if len(user_selection) <4:
    print ("Invalid selection entered, please try again")


#This will gather the information to complete the investment calculations    
if user_selection.upper() == "INVESTMENT":
    print ("You have selected Investment, please complete the following details; ")
    user_deposit = int(input("Amount of deposit: "))
    interest_rate = int(input("Interest rate: "))
    investment_years = int(input("Number of years of investment: "))
    interest_type = input ("Simple or compound interest: ")

    #This will calculate the investment amount from the information gathered for simple interest
    if interest_type.upper() == "SIMPLE":
        rate_rate = (interest_rate/100)
        simple_amount = user_deposit*(1 + rate_rate*investment_years)
        print (f"Your total investment return will be {simple_amount}.")

    #This will calculate the investment amount from the information gather for compound interest
    elif interest_type.upper() == "COMPOUND":
        rate_rate = (interest_rate/100)
        compound_amount = user_deposit * math.pow( (1 + rate_rate), investment_years)
        print (f"Your total investment return will be {compound_amount}.")

#This will gather the information to calculate home loan repayments
elif user_selection.upper() == "BOND":
    print ("You have selected Bond, please complete the following details; ")
    house_value = int(input("Enter current house value: "))
    house_interest = int(input("Interest rate: "))
    repayment_length = int(input("Number of months to repay: "))
    
    #This will calculate the bond repayments
    rate_monthly = ((house_interest/100)/12)
    bond_repayment = (rate_monthly * house_value)/(1-(1 + rate_monthly)**(-repayment_length))
    print (f"Your repayments will be {bond_repayment}")
