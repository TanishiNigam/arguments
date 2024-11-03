#Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. 
# Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), 
# this function calculates the total amount you should pay.
def total_calc(bill_amount,tip_perc):
    total= bill_amount+tip_perc
    return total
bill_amount= float(input("Enter bill amount"))
tip_perc= float(input("Enter tip percentage"))
print("The total amount is",total_calc(bill_amount,tip_perc))