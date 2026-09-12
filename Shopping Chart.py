#Shopping Cart 
items = []
prices = []
total = 0
while True:
    item = input("Enter the item (press q for quit): ")
    if item.lower()== "q":
        break
    else:
        price = float(input(f'Enter the price for {item}: '))
        items.append(item)
        prices.append(price)

print("----Total Chart is: ")
for item in items:
    print(item, end = " ")
for price in prices:
    total += price 

print()

print(f'Total is {total}')

   
