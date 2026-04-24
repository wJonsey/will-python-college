import pandas as pd 
import matplotlib.pyplot as plt
csv_path = '/workspaces/csv/practice_sales_data.csv'
df = pd.read_csv (csv_path)



def datetime():
    df['date'] = pd.to_datetime(df['date'])

def conversion_rate():
    df['Conversion Rate'] = df['sales'] / df['website_visits']


def get_date(start_end):

    flag = True

    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end))

        try:
            pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False

    return date


def average_sales(df, start_date, end_date):
    df["date"] = pd.to_datetime(df["date"])

    mask = (df["date"] >= pd.to_datetime(start_date)) & \
           (df["date"] <= pd.to_datetime(end_date))

    filtered_data = df.loc[mask]

    avg_sales = filtered_data["sales"].mean()

    return avg_sales


def highest_sales(df):
    sorted = df['sales'].sort
    highest = df['sales'].value_counts() 
    print(highest) 


highest_sales(df)

#def main():
    #datetime()
    #conversion_rate()
    #get_date("start")
    #get_date("end")





#main()