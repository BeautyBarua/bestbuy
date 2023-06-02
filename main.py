from store import Store
import products


def start(store):
    while True:
        print("Menu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            products = store.get_all_products()
            for product in products:
                print(product)
            print()

        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print("Total amount in store:", total_quantity)
            print()

        elif choice == "3":
            product_list = store.get_all_products()
            shopping_list = []
            while True:
                print("Available products:")
                for i, product in enumerate(product_list, start=1):
                    print(f"{i}. {product.name} - ${product.price} - Quantity: {product.quantity}")
                print("0. Finish ordering")

                product_choice = input("Enter the product number (0 to finish): ")
                if product_choice == "0":
                    break
                elif product_choice.isdigit() and 1 <= int(product_choice) <= len(product_list):
                    quantity = input("Enter the quantity: ")
                    if quantity.isdigit():
                        product = product_list[int(product_choice) - 1]
                        shopping_list.append((product, int(quantity)))
                        print("Product added to shopping list.")
                        print()
                    else:
                        print("Invalid quantity. Please try again.")
                        print()
                else:
                    print("Invalid product number. Please try again.")
                    print()

            order_total = store.order(shopping_list)
            print("Order placed successfully.")
            print("Total order cost:", order_total)
            print()

        elif choice == "4":
            print("Thank you for using the store. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            print()


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)
    start(store)


if __name__ == '__main__':
    main()
