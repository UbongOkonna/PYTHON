# cart = ["sneakers", "T-shirt", "water bottle"]
# cart.append("watch")
# cart[3] = "hoodies"

# print("items in cart:", len(cart))
# print("checkout list:", cart)

# print(cart[2])


# indexed list

# queue = ["chidi", "amina", "tunde", "Ngozi", "emeka"]


# print(queue)
# print("Last person:", queue[-1])
# print("second to last", queue[-2])
# queue = "Zainab"
# print("update queue:", queue)

# tuple

# customer_record = ("chidi okonkwo", "14-05-1998", "12345678901")



# name, dob, nin = customer_record
# print(f"verifying {name} (DOB: {dob})...")
# print("customer Name:", {name})
# print("date of birth:", {dob})


# dictionary

# account = {
#     "account_name": "ngozi okafor",
#     "account_number": "0123456789",
#     "balance": 45000,
#     "is_active": True 
# }

# transfer_amount = 5000.00
# if account["is_active"] and account["balance"] >= transfer_amount:
#     account["balance"] -= transfer_amount
#     print(f"Transfer successful! new balance: ${account["balance"]}")


basket = []
basket.append("plantains")
basket.append("garri")
basket.append("palm oil")
basket.append("afang leaves")

print("current basket:", basket)

basket.sort()
print("sorted basket:", basket)

scanned_first = basket.pop(0)
print(f"cashier scanned: {scanned_first}")

scanned_last = basket.pop()
print(f"cashier scanned: {scanned_last}")

print("remaining items to scan:", basket)