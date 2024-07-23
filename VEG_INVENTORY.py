veg = ['brinjal', 'tomato', 'potato', 'onion']
quantity = [15, 20, 25, 10]
price = [45, 20, 30, 50]
itemized_bill = []
revenue = 0
invest = 1000
cart = []
users = []
itemized_profit = []  # List to store itemized profit
veg_cost = {}  # Dictionary to store the cost of vegetables

# Initialize veg_cost with the current cost of each vegetable
for v, p in zip(veg, price):
    veg_cost[v] = p

while True:
    ch = input("Welcome to the stores\nOwner/User: ").lower()
   
    if ch == "owner":
        username = input("Enter username: ")
        password = int(input("Enter password: "))

        if username == "owner" and password == 1234:
            while True:
                ch = input("Owner data: \n1. Add item\n2. Remove item\n3. Update item\n4. View inventory\n5. View users and their carts\n6. Revenue Report\n7. Exit\nChoose one option: ")
                ch = int(ch)
               
                if ch == 1:
                    add_veg = input("What type of veg do you want to add: ")
                    add_qty = int(input("How much qty do you want to add: "))
                    add_price = int(input("How much amount do you add: "))
                    veg.append(add_veg)
                    quantity.append(add_qty)
                    price.append(add_price)
                    veg_cost[add_veg] = add_price  # Update veg_cost dictionary
                    print(f"{add_veg} added successfully.")
                   
                elif ch == 2:
                    print("Current Inventory:")
                    print(f"{'Item':<10}|{'Quantity':<10}|{'Price':<10}")
                    for v, q, p in zip(veg, quantity, price):
                        print(f"{v:<10}|{q:<10}|{p:<10}")
                    remove_veg = input("What do you want to remove: ")
                    if remove_veg in veg:
                        idx = veg.index(remove_veg)
                        veg.pop(idx)
                        quantity.pop(idx)
                        price.pop(idx)
                        del veg_cost[remove_veg]  # Remove from veg_cost dictionary
                        print(f"{remove_veg} removed successfully.")
                    else:
                        print("Item not found.")
                       
                elif ch == 3:
                    idx = int(input("Enter index of the vegetable to change quantity and price: "))
                    if 0 <= idx < len(veg):
                        new_quantity = int(input("Enter the new quantity: "))
                        new_price = int(input("Enter the new price: "))
                        quantity[idx] = new_quantity
                        price[idx] = new_price
                        veg_cost[veg[idx]] = new_price  # Update veg_cost dictionary
                        print(f"{veg[idx]} quantity changed to {new_quantity} and price changed to {new_price}.")
                    else:
                        print("Invalid index.")
                       
                elif ch == 4:
                    print("Current Inventory:")
                    print(f"{'Item':<10}{'Quantity':<10}{'Price':<10}")
                    for v, q, p in zip(veg, quantity, price):
                        print(f"{v:<10}{q:<10}{p:<10}")
                       
                elif ch == 5:
                    print("Users and their carts:")
                    print(f"{'Username':<15}{'Cart':<50}")
                    for user, user_cart in users:
                        cart_items = ', '.join([f"{item}({qty} kgs)" for item, qty, price in user_cart])
                        print(f"{user:<15}{cart_items:<50}")
               
                elif ch == 6:
                    print("************ Revenue Report ************")
                    print(f"Total revenue of the day: Rs. {revenue}")
                    break
                   
                elif ch == 7:
                    break
                   
                else:
                    print("Invalid option.")
        else:
            print("Authentication failed, please enter correct details.")
           
    elif ch == "user":
        username = input("Enter username: ")
        number = int(input("Enter number: "))
        user_cart = []

        while True:
            print("Available items:")
            print(f"{'Item':<10}|{'Quantity':<10}|{'Price':<10}")
            for v, q, p in zip(veg, quantity, price):
                print(f"{v:<10}|{q:<10}|{p:<10}")
               
            item = input("What do you want: ").lower()
            if item in veg:
                qty = float(input('How many kgs do you want: '))
                idx = veg.index(item)
               
                if qty <= quantity[idx]:
                    amount = qty * price[idx]
                    print('--------------------------------------')
                    print(f'Price per kg: {price[idx]}')
                    print(f'Boss, please pay Rs. {amount}')
                    print('--------------------------------------')
                    quantity[idx] -= qty
                    itemized_bill.append((item, qty, price[idx] * qty))
                    revenue += amount
                    user_cart.append((item, qty, price[idx] * qty))
                else:
                    print(f"Sorry, we only have {quantity[idx]} kgs of {item}.")
                   
            else:
                print('--------------------------------------')
                print(f"{item} is not available.")
                print('--------------------------------------')

            cart_choice = input('Do you want to add to cart (yes/no): ').lower()
            if cart_choice == 'yes':
                cart.append(user_cart)

            option1 = input('Do you want to buy more (yes/no): ').lower()
            if option1 == 'no':
                print("************* Your Bill *************")
                total_bill = 0
                print(f"{'Item':<10}|{'Quantity':<10}|{'Price':<10}")
                for item, qty, price in itemized_bill:
                    print('--------------------------------------')
                    print(f"{item:<10}|{qty:<10}|{price:<10}")
                    print('--------------------------------------')
                    total_bill += price

                    # Calculate profit for each item
                    cost = veg_cost.get(item, 0)
                    item_profit = (price - cost) / cost * 100 if cost > 0 else 0
                    itemized_profit.append((item, item_profit))
                   
                print('--------------------------------------')
                print(f"\t\tTotal bill: Rs. {total_bill}")
                print('--------------------------------------')
                users.append((username, user_cart))
                break

        close_shop = input('Do you want to close the shop (yes/no): ').lower()
        if close_shop == 'yes':
            print("************ Report ************")
            print(f"{'Item':<10}|{'Quantity':<10}")
            for v, q in zip(veg, quantity):
                print(f"{v:<10}{q:<10}")
            print("Today's revenue is:", revenue)
            profit = revenue - invest
            print("Your break-even point is:", profit)
            print("Itemized bill:")
            for item in itemized_bill:
                print(item)
            print("Itemized profit:")
            for item, profit in itemized_profit:
                print(f"{item}: {profit:.2f}%")
            print("Users and their carts:")
            for user in users:
                print(f"User: {user[0]}, Cart: {user[1]}")
            break
    else:
        print("Invalid choice. Please enter 'owner' or 'user'.")
