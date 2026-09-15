#Concession Stand 
items  = {'popcorn': 150,
          'chips':120,
          'nachos': 200,
          'pepsi': 60 
        }
chart = {}
total = 0 
print("-------------------MENU-------------------")
for key, value in items.items():
    print(f'{key}: Rs {value:.2f}')
print("------------------------------------------")
while True:
    food = input("enter what you want to eat OR press 'q' to quit :").lower()
    if food == 'q':
       break
  
    elif food in items: 
           if food in chart:
                chart[food] +=1 
           else:
                chart[food] = 1
    else:
         print("Write the things that are in the menu dumbo!!")
for food, quantity in chart.items():
     price = items[food]
     total += (quantity * price)

print("---------------------BILL---------------------")
for food, quantity in chart.items():
     print(f'{food} x {chart[food]} = Rs {items[food]}/piece')

print(f'Total = Rs {total}')
print("----------------------------------------------")


