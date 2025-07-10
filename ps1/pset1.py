


annual_salary = int(input("Enter your annual Salary: "))
portion_saved = float(input("Enter the percent of your salray to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream house: "))
portion_down_payment=.25*total_cost
current_savings = 0
nummonths=0
while current_savings < portion_down_payment:
    current_savings += portion_saved * annual_salary / 12 + current_savings * 0.04 /12
    nummonths +=1

print("Number of Months: " , nummonths)