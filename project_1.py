# Income Tax Calculator
flat_rate = float(0.20)  # Assigned variable flat_rate to represent value 0.20
standard_deduction = float(10000)  # Assigned variable Standard_deduction to 10,000 deduction
gross_income = float(input('Enter the gross income: '))
# Assigned gross_income to input number after 'Enter the gross income:
dependents = float(input('Enter the number of dependents: '))
# Assigned Dependents to input number after 'Enter the number of dependents:
dependent_calculation = dependents * 3000
# assigned dependent_calculation to multiply dependents by 3000

total= (gross_income - standard_deduction - dependent_calculation) * flat_rate
# assigned totals to subtract gross_income, standard_deduction, and dependent_calculation and then multiply it by
# flat_rate
print("The income tax is $",total)
 # print "the income tax is $" and variable total.























