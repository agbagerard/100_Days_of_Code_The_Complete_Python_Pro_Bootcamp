print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#solution refactored
final_bill = 0
if size == "S":
    final_bill += 15
elif size == "M":
    final_bill += 20
elif size == "L":
    final_bill += 25
else:
    print("You typed in the wrong value") #Error handling

if pepperoni == "Y":
    if size == "S":
        final_bill += 2
    else:
        final_bill += 3

if extra_cheese == "Y":
    final_bill += 1

print(f"Your final bill is: ${final_bill}.")


# My first solution
# if size == "S":
#     if pepperoni == "Y":
#         if extra_cheese == "Y":
#             final_bill = 15 + 2 + 1
#             print(f"Your final bill is: ${final_bill}.")
#         else:
#             final_bill = 15 + 2
#             print(f"Your final bill is: ${final_bill}.")
#     elif pepperoni == "N":
#         if extra_cheese == "Y":
#             final_bill = 15 + 1
#             print(f"Your final bill is: ${final_bill}.")
#         else:
#             final_bill = 15
#             print(f"Your final bill is: ${final_bill}.")
# elif size == "M":
#     if pepperoni == "Y":
#         if extra_cheese == "Y":
#             final_bill = 20 + 3 + 1
#             print(f"Your final bill is: ${final_bill}.")
#         else:
#             final_bill = 20 + 3
#             print(f"Your final bill is: ${final_bill}.")
#     elif pepperoni == "N":
#         if extra_cheese == "Y":
#             final_bill = 20 + 1
#             print(f"Your final bill is: ${final_bill}.")
#         else:
#             final_bill = 20
#             print(f"Your final bill is: ${final_bill}.")
# elif size == "L":
#     if pepperoni == "Y":
#         if extra_cheese == "Y":
#             final_bill = 25 + 3 + 1
#             print(f"Your final bill is: ${final_bill}.")
#         else:
#             final_bill = 25 + 3
#             print(f"Your final bill is: ${final_bill}.")
#     elif pepperoni == "N":
#         if extra_cheese == "Y":
#             final_bill = 25 + 1
#             print(f"Your final bill is: ${final_bill}.")
#         else:
#             final_bill = 25
#             print(f"Your final bill is: ${final_bill}.")