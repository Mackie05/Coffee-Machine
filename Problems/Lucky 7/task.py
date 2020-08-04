number = int(input())
number_list = []
for i in range(0, number):
    number = int(input())
    if number % 7 == 0:
        number_list.append(int(number))
for i in number_list:
    print(i * i)
