print("Welcome to the shop")
print("Here's our menu")
menu = ['chips', 'chocolate', 'drinks', 'biscuits', 'jellies']
for i in menu:
    print(i)
print("Enter what you want to buy press 'c' to checkout")
count = 0
price = 0
item = 0
while item != 'c':
    item = input("What do you want to buy").lower()
    if item == 'chips':
        print('Price = 50$')
        price = price + 50
        count = count + 1
    elif item == 'chocolates':
        print('Price = 150$')
        price = price + 150
        count = count + 1
    elif item == 'drinks':
        print('Price = 70$')
        price = price + 70
        count = count + 1
    elif item == 'biscuits':
        print('Price = 30$')
        price = price + 30
        count = count + 1
    elif item == 'jellies':
        print('Price = 20$')
        price = price + 20
        count = count + 1
    if item == 'c':
        break

print(f"Checkout = {price}$")
print(f"You bought {count} items")














