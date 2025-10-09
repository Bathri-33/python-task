item = float(input("Enter the cost of one item: "))

quantity = int(input("Enter the quantity: "))

totalcost = item * quantity

if totalcost > 1000:
    discount = totalcost * 0.10
    totalcost -= discount
    print("Discount applied:",discount)
else:
    print("No discount applied.")

print("Total cost to pay: ", totalcost)
