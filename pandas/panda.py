import pandas as pd
 
def menu():
    while True:
        print("######################################################")
        print("Welcome to RBSX Group Ltd\n")
        print("Select one of the available options:")
        print("1.conversions? ")
        print("2. Compare GBP with other currencies")
        print("3. Select the currency for performance check")
        choice = input()
        if choice.isdigit() and int(choice) == 1:
            print("Select one of the following currency conversion options:")
            print("1. Pound Sterling (GBP) to Euros (EUR)")
            print("2. Euros (EUR) to Pound Sterling (GBP)")
            print("3. Pound (GBP) to Australian Dollars (AUD)")
            print("4. Australian Dollars (AUD) to Pound Sterling (GBP)")
            print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
            print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
            print("7. Pound Sterling (GBP) to American Dollar (USD)")
            print("8. American Dollar(USD) to Pound Sterling (GBP)")
            print("######################################################")
            choice = input()
            return choice
        elif choice.isdigit() and int(choice) == 2:
            
       
        elif choice.isdigit() and int(choice) == 3:

        
        else:
            print("Sorry, you did not enter a valid choice")
 
def get_currency(menu_choice):
    currencies = {
        '1': 'GBP +AC0- EUR',
        '2': 'EUR +AC0- GBP',
        '3': 'GBP +AC0- AUD',
        '4': 'AUD +AC0- GBP',
        '5': 'GBP +AC0- JPY',
        '6': 'JPY +IBM- GBP',
        '7': 'GBP +AC0- USD',
        '8': 'USD +AC0- GBP',
    }
    return currencies.get(menu_choice)
 
def get_conversion_rate(currency):
    df = pd.read_csv("Task_4a_RBSX_data.csv")
    df.drop_duplicates(inplace = True)
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
    return round(df[currency].iloc[-1], 2)
 
def get_amount_to_convert():
    while True:
        amount = input("Please enter the amount you wish to convert: ")
        try:
            return float(amount)
        except ValueError:
            print("Sorry, you must enter a numerical value")
 
def perform_conversion(amount, rate, currency):
    received = round(amount * rate, 2)
    print("##################################")
    print(f"You are converting {amount} {currency[:3]}")
    print(f"You will receive {received} {currency[-3:]}")
    print()
    a = input("Do you wish to continue (Y/N) : ")
    return a
 
while True:
    menu_choice = menu()
    currency = get_currency(menu_choice)
    rate = get_conversion_rate(currency)
    amount = get_amount_to_convert()
    ab = perform_conversion(amount, rate, currency)
    if ab == 'N':
        print("Thank you for using the services of RBSX Group Ltd")
        break