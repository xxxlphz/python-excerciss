takeaway_menu = ["1. Pad Thai","2. Chicken Tikka Masala","3. Pepperoni Pizza","4. Veggie Burger with Fries","5. Burrito Bowl"]
takeaway_prices = [12.99, 14.50,  9.99,  15.99,  11.50]
delivery_fee = 5.00
free_delivery_price = 30.00

def total(price,order,delivery,free):
    for item in order:
        if price <= free:
            price+= delivery
    return price
    


print("Welcome to the takeaway delivery service.")
name = input('Enter your name: ')
print(f'Welcome {name} !!')
print("Here's our menu.")
for item in takeaway_menu:
    print(item)

quantity = int(input("How many items would you like to purchase?"))
order = []
for i in range(quantity):
    choice = int(input("Enter the menu number of the item you wish to add to your order: "))
    order.append(choice)
print(f"\nThank you {name}, your order is as follows")
bill = 0
for item in order:
    print(takeaway_menu[item-1])
    bill += takeaway_prices[item-1]
print('Your total is %.2f euro' %total(bill,order,delivery_fee,free_delivery_price))

#1. Read throught the program, then run it to make sure you understand what it is doing.
#2. Ask the user for their name and save it in an appropriately named variable.
#3. Include the user's given name in the print statement where they are thanked for their order.
#4. Write a loop that calculates the total value of the order and prints this number to the screen with an appropriate description.
#5. Alter the program so the delivery_fee is added to the total price of the order unless the
    #total value of the food is greater than value of free_delivery_price. Print this new value to the screen with appropriate text.
#6. Create a function called get_bill_total that combines the code added in step 4 and 5. Have the program call this function. 
