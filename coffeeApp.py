class Coffee:

    # initialize coffee with name and prize

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:

    #initialize order with empty list of coffees

    def __init__(self):
        self.items = []

    # add coffee to order

    def add_item(self, coffee):
        self.items. append(coffee)
        print(f"Added {coffee.name} to your order.")

    # calculate total price of order

    def total(self):
        return sum(item.price for item in self.items)
    
    # print order summary

    def show_order(self):
        if not self.items:
            print("Your order is empty.")

            return
        
        print("\nYour Order:")

        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price}")

        print(f"Total: ${self.total()}\n")

        # handle checkout process

        def checkout(self):
            if not self.items:
                print("Your order is empty. Please add items before checking out.")
                return
            
            self.show_order()
            confirm = input("Proceed to checkout? (yes/no): ").strip().lower()
            if confirm == 'yes':

                print("Order confirmed! Thank you for your purchase.")

                self.items.clear()

            else:
                print("Order cancelled. Your items are still in the cart.")

# display menu and handle user input

def main():

    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Americano", 2.0),
        Coffee("Mocha", 3.5)
    ]

    order = Order()

    #User interaction

    while True:
        print("\n--- Coffee Menu ----")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")

        print("5. View Order")

        print("6. Checkout")

        print("7. Exit")

        choice = input("Choose an option: ")

        if choice in ['1', '2', '3', '4']:
            order.add_item(menu[int(choice) - 1])

        elif choice == '5':
            order.show_order()

        elif choice == '6':
            order.checkout()

        elif choice == '7':
            print("Thank you for visiting our coffee shop!")
            break

        else:
            print("Invalid choice. Please try again.")

    if __name__ == "__main__":
        main()

