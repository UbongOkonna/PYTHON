# try:
#     amount = int(input("enter total bill ($): "))
#     people = int(input("split between how many people? "))
#     share = amount / people

# except ValueError: 
#     print("error: please enter valid numbers only.")

# except ZeroDivisionError: 
#     print("error: you cannot split a bill among zero people.")
 
# else:
#     print(f"each person pays: ${share:.2f}")

# finally: 
#     print("Thank you for using the bill splitter.")



class insuficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("withdrawal amount must be greater than $0.")
    
    if amount > balance:
        raise insuficientFundsError(f"cannot withdraw ${amount}. your balance is only ${balance}.")
    return balance - amount

my_balance = 10000
try:
    my_balance = withdraw(my_balance, 15000)
except insuficientFundsError as e:
    print(f"Transaction declined: {e}")
except ValueError as e:
    print(f"invalid input: {e}")
else:
    print(f"success! new balance: ${my_balance}")