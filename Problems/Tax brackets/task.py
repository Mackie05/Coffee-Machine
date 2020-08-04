income = abs(int(input()))
if income <= 15527:
    tax_rate = 0
elif income <= 42707:
    tax_rate = 15
elif income <= 132406:
    tax_rate = 25
else:
    tax_rate = 28

calculated_tax = int(round(income * tax_rate / 100))

print(f"The tax for {income} is {tax_rate}%. That is {calculated_tax} dollars!")

