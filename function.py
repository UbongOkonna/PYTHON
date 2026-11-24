# def apply_discount(price, discount_percent) : 
#     discount = price * (discount_percent / 100)
#     final_price = price - discount
#     return final_price

# new_price = apply_discount(10000, 20)
# print(f"price after discount: ${new_price}")

def check_voting_eligibility(name, age):
    if age >= 18:
        print(f"{name},you are eligible to vote!")
    else:
        print(f"sorry {name}, you must be at least 18 to vote.")
check_voting_eligibility("Ngozi", 22)
check_voting_eligibility("kemi", 15) 
