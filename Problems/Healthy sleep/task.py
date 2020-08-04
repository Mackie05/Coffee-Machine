recommended_sleep = int(input())
oversleep = int(input())
current_sleep = int(input())

if current_sleep < recommended_sleep:
    print("Deficiency")
elif current_sleep > oversleep:
    print("Excess")
else:
    print("Normal")