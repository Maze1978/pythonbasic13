"""
Condition 1: Purchase more than 1000 tk
Condition 2: Customer age less than 50 years
Condition 3: if customer's gender male will get "pen" and female will get "chocolate" as free
Condition 4: Payment on cash will get 10% discount, card will get 20% discount
"""

purchase = int(input("purchase: "))
age = int(input("age: "))
Gender = input("Gender: ")
Payment = input("Payment: ")
Formula1 = purchase - purchase * 10/100
Formula2 = purchase - purchase * 20/100

if purchase > 1000 and age < 50:
    print("Eligible foe discount")
    if Gender == "male":
        print("Free pen")
    elif Gender == "female":
        print("free Chocolate")
    if Payment == "cash":
        print("After Discount 10% you have to pay")
        print("purchase - purchase * 10/100")
    elif Payment == "card":
        print("After Discount 20% you have to pay")
        print("purchase - purchase * 20/100")
else:
    print("Not eligible for discount ")