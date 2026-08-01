cents = [25, 10, 5]

amount_due = 50
amount_paid = 0

while amount_paid < 50:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in cents:
        amount_due -= coin
        amount_paid += coin

if amount_paid > 50:
    print(f"Change Owed: {amount_paid-50}")
else:
    print(f"Change Owed: 0")

