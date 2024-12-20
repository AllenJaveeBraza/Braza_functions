def define():
    # Item Listing ---
    total = 0
    Check = []

    Menu = {"hamburger": 89,
            "sandwich": 79,
            "hotdog": 69,
            "chicken": 99,
            "pizza": 129,
            "fries": 65,
            "nuggets": 65}

    print("-======>> MENU <<=======-")
    for food, cost in Menu.items():
        print(f"{food:12}: {cost:.2f}")
    print("-=======================-")

    def collect_user_input():
        nonlocal Check
        while True:
            item = input(f"Please select an item at the menu. (insert 'done' when completed): ").lower()
            if item.lower() == 'done':
                break
            elif Menu.get(item) is not None:
                Check.append(item)

    def calculate_total():
        nonlocal total
        for item in Check:
            total += Menu.get(item)

    def process_payment():
        nonlocal total
        while True:
            payment = input("Insert your payment here: ")
            if not payment.isdigit():
                print("Invalid Input. Please try again.")
                continue
            payment = int(payment)
            if total > payment:
                print("Insufficient Amount, please insert the right amount.")
                continue
            elif total < payment:
                change = payment - total
                print(f"Transaction completed.\n Your change is {change:.2f}.\nThank you for dining, please come again!")
                break
            elif total == payment:
                print("Transaction completed with exact amount. \nThank you for dining, please come again!")
                break

    collect_user_input()
    calculate_total()

    # Receipt ---
    print("-======>> RECEIPT <<======-")
    print(f"your total is {total:.2f}")
    print("Your items are:")
    for item in Check:
        print(item, end=" ")
    print()
    print("-=========================-")

    process_payment()

# Call the define function to run the program
define()
