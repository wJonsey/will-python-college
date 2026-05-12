# Accepts input of membership card number and validates it
def membership_card_check():
    valid = True

    while valid == True:

        card_number = input("Please enter your PawsPlus membership card number: ")

        if card_number.isdigit():
            if len(card_number) == 6:
                valid = True
                return card_number
            else:
                print("You did not enter a valid membership card number.")
                print("Membership card number must be exactly 6 digits long.")
        else:
            print("You did not enter a valid membership card number.")
            print("Membership card number must contain only digits.")
            valid = False


# Allows user to select the fulfilment method for the purchase
def get_fulfilment():
    valid = False

    while valid == False:
        print("Please select the fulfilment method for this transaction")
        print("1. In-Store")
        print("2. Home Delivery")
        selection = int(input("Enter choice here (1 or 2): "))

        if selection == 1:
            method = "In-Store"
            valid = True
        elif selection == 2:
            method = "Home Delivery"
            valid = True
        else:
            print("Sorry, you have not entered a valid option.")
            valid = False

    return method


# Allows the user to enter the value and category of each item purchased
def get_items(prices, categories):
    end_transaction = False
    item_count = 0

    while end_transaction == False:
        item_count += 1

        valid_price = False
        valid = False

        while valid_price == False:
            print("Please enter the value of item {}.".format(item_count))
            print("Enter X when finished")
            temp_price = input("Item {} : £".format(item_count))

            if temp_price.lower() == "x":
                end_transaction = True
                valid = True
                break
            else:
                try:
                    float(temp_price)
                except:
                    print("Sorry, you did not enter a valid price.")
                    end_transaction == False
                else:
                    temp_price = float(temp_price)
                    prices.append(temp_price)
                    valid_price = True

        while valid == False:
            print("Please enter the category for item {}".format(item_count))
            print("1. Premium Pet Food")
            print("2. Pet Accessories")
            print("3. Veterinary Products")
            choice = input("Category: ")

            if choice == "1":
                temp_cat = "Premium Pet Food"
                categories.append(temp_cat)
                valid = True
            elif choice == "2":
                temp_cat = "Pet Accessories"
                categories.append(temp_cat)
                valid = True
            elif choice == "3":
                temp_cat = "Veterinary Products"
                categories.append(temp_cat)
                valid = True
            else:
                print("Sorry, you have not entered a valid option.")
                valid = False


# Calculates the number of points earned for each product purchased
def calculate_points(prices, categories, points_earned):

    for i in range(len(prices)):
        value = int(prices[i])
        category = categories[i]

        if category == "Premium Pet Food":
            pts = value * 5

        elif category == "Pet Accessories":
            if value > 100:
                initial_pts = 500
                extra_pts = (value - 100) * 3
                pts = initial_pts + extra_pts
            else:
                pts = value * 5

        else:
            pts = value * 4

        points_earned.append(pts)


def main():
    prices = []
    categories = []
    points_earned = []

    card_number = membership_card_check()
    method = get_fulfilment()

    get_items(prices, categories)
    calculate_points(prices, categories,points_earned)

    total_value = sum(prices)
    points_subtotal = sum(points_earned)

    if method == "Home Delivery":
        bonus_pts = int(total_value) * 1
    else:
        bonus_pts = 0

    final_pts = points_subtotal + bonus_pts

    print("-" * 60)
    print("Transaction summary for member {}".format(card_number))
    print("-" * 60)
    print("Final total value of this transaction was £{:.2f}".format(total_value))
    print("Here is a summary of the points you have earned:")
    for i in range(len(points_earned)):
        print("Item {}. {} pts".format(i + 1, points_earned[i]))
    print("-" * 60)
    print("Points subtotal: {}".format(points_subtotal))
    print("-" * 60)
    print("Bonus points earned: {}".format(bonus_pts))
    print("-" * 60)
    print("Final points total: {}".format(final_pts))
    print("-" * 60)


main()