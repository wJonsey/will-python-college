import pandas as pd
import matplotlib.pyplot as plt
 
def menu():
    while True:
        print("######################################################")
        print("Welcome to RBSX Group Ltd\n")
        print("Select one of the available options:")
        print("1.Which conversion would you like to make today? ")
        print("2. Compare GBP with other currencies")
        print("3. Select the currency for performance check")
        choice = input()
        if choice.isdigit() and int(choice) == 1:
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
            print(" comparison matrix")
            df = pd.read_csv("Task_4a_RBSX_data.csv")
            df.drop_duplicates(inplace = True)
            df['Date'] = pd.to_datetime(df['Date'], format='mixed')
            abc={}
            for c in df.columns:
                if(c.startswith("GBP")):
                    # abc[c]=float(df[c].max())
                    abc.update({"the value of 1"+c[:3]+"in"+c[-3:]:float(df[c].max())})
            print("min value for GBP over 12 week period = ")
            print(abc)
            se=pd.Series(abc)
            se.plot()
            plt.show()
            for c in df.columns:
                if(c.startswith("GBP")):
                    # abc[c]=float(df[c].max())
                    abc.update({"the value of 1"+c[:3]+"in"+c[-3:]:float(df[c].min())})
            print("max value for GBP over 12 week period = ")
            print(abc)
            se=pd.Series(abc)
            se.plot()
            plt.show()
            
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
    a=input("Do you wish to continue (Y/N) : ")
    return a
 
while True:
    menu_choice = menu()
    currency = get_currency(menu_choice)
    rate = get_conversion_rate(currency)
    amount = get_amount_to_convert()
    ab=perform_conversion(amount, rate, currency)
    if ab=='N':
        print("Thank you for using the services of RBSX Group Ltd")
        break