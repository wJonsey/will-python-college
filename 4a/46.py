import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv('/workspaces/csv/random-data-1777374106762.csv')

df['Date'] = pd.to_datetime(df['Date'])

df['Amount'] = pd.to_numeric(df['Amount'])

def main_menu():
    flag = True
    while flag:
        print('1.Id')
        print('2.First Name')
        print('3.City')
        print('4.Date')
        print('5.Amount')
        choice = int(input('select an option: '))

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
        else:    
            print('Choice accepted!')
            flag = False

    return choice

def ID_data():
    ID = int(input('Enter the ID you want to select: '))
    
    filtered_Id = df[df['Id'] == ID]
    
    print(filtered_Id)

def first_name():
    first_name = input('Enter the name you want to select: ')

    filtered_name = df[df['First Name']== first_name]

    print(filtered_name)

def city():
    city_boi = input('Enter the city you want to select: ')

    filtered_city = df[df['City'] == city_boi ]

    print(filtered_city)

def date(start):
    flag = True
    
    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start))

        try:
           pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False

    filtered_date = df[df['Date'] == date]
    print(filtered_date)

def amount():
    amount = float(input('Enter amount you want to filter: '))

    filtered_amount = df[df['Amount'] == amount]

    print(filtered_amount)

main_menu_choice = main_menu()

if main_menu_choice == 1:
    ID_data()
elif main_menu_choice == 2:
    first_name()
elif main_menu_choice == 3:
    city()
elif main_menu_choice == 4:
    date('start')
elif main_menu_choice == 5:
    amount()