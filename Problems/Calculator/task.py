first_number = float(input())
second_number = float(input())
operator = input()

if operator == '+':
    print(first_number + second_number)
elif operator == '-':
    print(first_number - second_number)
elif operator == '*':
    print(first_number * second_number)
elif operator == 'pow':
    print(first_number ** second_number)
elif operator == '/' and second_number != 0:
    print(first_number / second_number)
elif operator == 'mod' and second_number != 0:
    print(first_number % second_number)
elif operator == 'div' and second_number != 0:
    print(first_number // int(second_number))
else:
    print("Division by 0!")
