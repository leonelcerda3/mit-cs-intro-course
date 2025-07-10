starting_salary = int(input("Enter your starting Salary: "))

total_cost=1000000
semi_annual_raise = 0.07 
portion_down_pay = 0.25 * total_cost
annual = 0.04 
months = 36

bi_steps=0
epsilon = 100



low = 0
high = 10000


portion_saved = (high + low) / 2
found = False
while abs(low - high) > 1:
    bi_steps += 1
    annual_salary = starting_salary
    monthly_save = (annual_salary /12 ) * (portion_down_pay/10000)
    current_saving = 0.0

    for i in range (1,months+1):
    




    
    
print("Best savings rate: " , savings_rate)

print("Steps in bisection search: " , bi_steps)
