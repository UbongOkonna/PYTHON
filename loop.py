# cities = ["uyo","lagos","abuja"]
# for city in cities:
#     print(f"welcome to {city}")


# while loop
# battery = 20
# while battery < 100:
#     print(f"charging... {battery}%")
    # battery += 20


# for i in range(5):
#     print(i)
# for i in range(0, 11, 2):
#     print(i)




# break in loop

# for num in range(1, 10):
#     if num == 6:
#         print("found 6! existing loop.")
#         break
#     print(f"checking {num}...") 

# continue in loop

# for num in range(1, 8):
#     if num % 2 == 0:
#         continue 
#     print(f"odd numbers: {num}")

correct_pin = "4231"
account_balance = 50000
is_card_active = True
for attempt in range(1, 4):
    entered_pin = input(f"attempt {attempt}/3 enter your pin: ")
    if not (entered_pin == correct_pin):
        if attempt < 3:
            print("wrong pin. try again.\n")
            continue
        else:
            print("3 failed attempts. your card is blocked")
            break
    if entered_pin == correct_pin and is_card_active:
        print("PIN accepted")

        withdrawal = int(input ("enter amount to withdraw:  "))

        if withdrawal <= account_balance:
            account_balance = withdrawal
            print(f"success! you have withdraw: #{withdrawal}")
        else:
            print("insuficient funds.")
        break
