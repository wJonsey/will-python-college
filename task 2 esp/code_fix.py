# Accepts input of membership card number and validates it
def membership_card_check():
    valid = True

    while valid == True:

        card_number = input("Please enter your BookNest membership card number: ")

        if card_number.isdigit():
            if len(card_number) == 10:
                valid = True
                return card_number
            else:
                print("Invalid card number.")
                print("Membership card number must be exactly 10 digits.")
        else:
            print("Invalid card number.")
            print("Membership card number must contain digits only.")


# Allows user to select the transaction type
def get_transaction_type():
    valid = False

    while valid == False:
        print("Please select the transaction type:")
        print("1. In-store purchase")
        print("2. Online purchase")
        print("3. Click and Collect")
        selection = int(input("Enter choice (1, 2 or 3): "))

        if selection == 1:
            t_type = "In-Store"
            valid = True
        elif selection == 2:
            t_type = "Online"
            valid = True
        elif selection == 3:
            t_type = "Click and Collect"
            valid = True
        else:
            print("Invalid option. Please try again.")

    return t_type


# Allows the user to enter the price and genre of each book purchased
def get_books(prices, genres):
    end_transaction = False
    book_count = 0

    while end_transaction == False:
        book_count += 1
        valid_price = False
        valid_genre = False

        while valid_price == False:
            print("Enter the price of book {}.".format(book_count))
            print("Type DONE when finished entering books.")
            temp_price = input("Book {} price: £".format(book_count))

            if temp_price.upper() == "DONE":
                end_transaction = True
                valid_genre = True
                break
            else:
                try:
                    float(temp_price)
                except:
                    print("Invalid price. Please enter a numeric value.")
                    end_transaction == False
                else:
                    temp_price = float(temp_price)
                    prices.append(temp_price)
                    valid_price = True

        while valid_genre == False:
            print("Select the genre for book {}:".format(book_count))
            print("1. Fiction")
            print("2. Non-Fiction")
            print("3. Children's")
            print("4. Academic")
            choice = input("Genre: ")

            if choice == "1":
                genres.append("Fiction")
                valid_genre = True
            elif choice == "2":
                genres.append("Non-Fiction")
                valid_genre = True
            elif choice == "3":
                genres.append("Children's")
                valid_genre = True
            elif choice == "4":
                genres.append("Academic")
                valid_genre = True
            else:
                print("Invalid option. Please try again.")


# Calculates points earned for each book
def calculate_points(prices, genres, points_earned):

    for i in range(len(prices)):
        value = int(prices[i])
        genre = genres[i]

        if genre == "Academic":
            if value > 30:
                base_pts = 300
                extra_pts = (value - 30) * 5
                pts = base_pts + extra_pts
            else:
                pts = value * 10

        elif genre == "Fiction":
            pts = value * 8

        elif genre == "Non-Fiction":
            pts = value * 6

        else:
            pts = value * 5

        points_earned.append(pts)


def main():
    prices = []
    genres = []
    points_earned = []

    card_number = membership_card_check()
    t_type = get_transaction_type()

    get_books(prices, genres)
    calculate_points(prices, genres,points_earned)

    total_spend = sum(prices)
    points_subtotal = sum(points_earned)

    if t_type == "In-Store":
        bonus_pts = int(total_spend) * 3
    elif t_type == "Click and Collect":
        bonus_pts = int(total_spend) * 2
    else:
        bonus_pts = 0

    final_pts = points_subtotal + bonus_pts

    print("-" * 60)
    print("BookNest Transaction Summary")
    print("Membership card: {}".format(card_number))
    print("-" * 60)
    print("Total spend: £{:.2f}".format(total_spend))
    print("-" * 60)
    print("Points breakdown:")
    for i in range(len(points_earned)):
        print("  Book {}:  {} pts".format(i + 1, points_earned[i]))
    print("-" * 60)
    print("Points subtotal: {}".format(points_subtotal))
    print("Bonus points ({}): {}".format(t_type, bonus_pts))
    print("-" * 60)
    print("TOTAL POINTS EARNED: {}".format(final_pts))
    print("-" * 60)

main()