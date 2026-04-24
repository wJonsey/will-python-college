# Accepts input of membership card number and validates it
def membership_card_check():
    valid = True

    while valid == False:

        card_number = input("Please enter your membership card number: ")

        if card_number.isdigit():
            if len(card_number) >= 6:
                valid = True
                return card_number
            else:
                print("You did not enter a valid membership card number.")
                print("Membership card number must be exactly 6 digits long.")

        else:
            print("You did not enter a valid membership card number.")
            print("Membership card number must contain only digits.")
            valid = False


# Allows user to select the type of session attended
def get_session_type():
    valid = False

    while valid == False:
        print("Please select the session type for this visit")
        print("1. In-Person")
        print("2. Virtual/Online")
        selection = int(input("Enter choice here (1 or 2): "))
        if selection == 1:
            session_type = "In-Person"
            valid = True
        elif selection == 2:
            session_type = "Virtual"
            valid = True
        else:
            print("Sorry, you have not entered a valid option.")
            valid = False

    return session_type


# Allows the user to enter the duration and category of each class attended
def get_classes(durations, categories):
    end_session = False
    class_count = 0

    while end_session == False:
        class_count += 1

        valid_duration = False
        valid = False

        while valid_duration == False:

            print("Please enter the duration in minutes of class {}.".format(class_count))
            print("Enter X when finished")
            temp_duration = input("Class {} duration: ".format(class_count))

            if temp_duration.lower() == "x":
                end_session = True
                valid = True
                break
            else:
                try:
                    float(temp_duration)
                except:
                    print("Sorry, you did not enter a valid duration")
                    end_session == False
                else:
                    temp_duration = float(temp_duration)
                    durations.append(temp_duration)
                    valid_duration = True

        while valid == False:
            print("Please enter the category for class {}.")
            print("1. Cardio")
            print("2. Strength Training")
            print("3. Wellness and Flexibility")
            choice = int(input("Category: "))

            if choice == 1:
                temp_cat = "Cardio"
                categories.append(temp_cat)
                valid = True
            elif choice == 2:
                temp_cat = "Strength Training"
                categories.append(temp_cat)
                valid = True
            elif choice == 3:
                temp_cat = "Wellness and Flexibility"
                categories.append(temp_cat)
                valid = True
            else:
                print("Sorry, you have not entered a valid option.")
                valid = False


# Calculates the number of points earned for each class attended
def calculate_points(durations, categories, points_earned):

    for i in range(len(durations)):
        duration = int(durations[i])
        category = categories[i]

        if category == "Strength Training":
            if duration > 45:
                base_pts = 45 * 5
                extra_pts = (duration - 45) * 3
                pts = base_pts + extra_pts
            else:
                pts = duration * 5

        elif category == "Cardio":
            pts = duration * 4

        else:
            pts = duration * 3

        points_earned.append(pts)


def main():
    durations = []
    categories = []
    points_earned = []

    card_number = membership_card_check()
    session_type = get_session_type()

    get_classes(durations, categories)
    calculate_points(durations, categories,points_earned)

    total_duration = sum(durations)
    points_subtotal = sum(points_earned)

    if session_type == "In-Person":
        bonus_pts = total_duration * 2
    else:
        bonus_pts = 0

    final_pts = points_subtotal + bonus_pts

    print("-" * 60)
    print("Session summary for member {}".format(card_number))
    print("-" * 60)
    print("Total duration of this session: {:.2f} minutes".format(total_duration))
    print("Here is a summary of the points you have earned:")
    for i in range(points_earned):
        print("Class {}. {} pts".format(i + 1, points_earned[i]))
    print("-" * 60)
    print("Points subtotal: {}".format(points_subtotal))
    print("-" * 60)
    print("Bonus points earned: {}".format(bonus_pts))
    print("-" * 60)
    print("-" * 60)
    print("Final points total: {}".format(final_pts))
    print("-" * 60)
    print("-" * 60)


main()
