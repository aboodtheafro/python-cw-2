my_name = input("what is your name: ")
my_age = input("what is your age: ")


print(f"my name is {my_name},and i am {my_age} years old")

first_number = int(input("first_number: "))
second_number = int(input("second_number"))

opration = input("enter an opeation(+-*/): ")

if opration == ("*"):
    print(first_number * second_number)
elif opration == ("/"):
    print(first_number / second_number)
elif opration == ("+"):
     print(first_number + second_number)
elif opration == ("-"): 
    print(first_number - second_number)

bus_capacity = 20 
people_in_bus = int(input("how many people are in the bus"))
empty_seats = bus_capacity - people_in_bus


if empty_seats > people_in_bus:
    print("there is empty space in the bus")
elif empty_seats <= people_in_bus:
    print("there is no space in the bus")