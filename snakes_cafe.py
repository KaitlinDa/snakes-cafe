def print_menu():
    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
    print("** To quit at any time, type \"quit\" **")
    print("**************************************\n")

    print("Appetizers")
    print("----------")
    print("Wings")
    print("Cookies")
    print("Spring Rolls\n")

    print("Entrees")
    print("-------")
    print("Salmon")
    print("Steak")
    print("Meat Tornado")
    print("A Literal Garden\n")

    print("Desserts")
    print("--------")
    print("Ice Cream")
    print("Cake")
    print("Pie\n")

    print("Drinks")
    print("------")
    print("Coffee")
    print("Tea")
    print("Unicorn Tears\n")

    print("***********************************")
    print("** What would you like to order? **")
    print("***********************************")


def main():
    order_counts = {}
    print_menu()

    while True:
        order = input("> ")

        if order.lower() == "quit":
            break
        elif order:
            order_counts[order] = order_counts.get(order, 0) + 1
            print(f"\n** {order_counts[order]} order of {order} has been added to your meal **\n")

if __name__ == "__main__":
    main()
