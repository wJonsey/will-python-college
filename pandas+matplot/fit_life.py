import pandas as pd
 
# -------------------- MAIN MENU --------------------
def main_menu():
    flag = True
 
    while flag:
        print("-"*60)
        print("------ FitLife Gym Analysis System ------")
        print("-"*60)
        print("1.  Total visits by member")
        print('2.  Membership types')
        print('3.  Monthly fees')
 
        choice = input("Enter your selection: ")
 
        if choice.isdigit():
            flag = False
        else:
            print("Invalid input")
 
    return int(choice)
 
 
# -------------------- MEMBER SELECTION --------------------
def get_member_id():
    df = pd.read_csv("/workspaces/csv/fit_life.csv")
 
    member_ids = df["Member ID"].unique().tolist()
 
    flag = True
 
    while flag:
        print("\nSelect a Member ID:")
 
        for i in range(len(member_ids)):
            print(i+1, member_ids[i])
 
        selection = input("Enter number: ")
 
        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            print("Invalid input")
 
        member_id = member_ids[selection - 1]
 
    print("You selected:", member_id)
    return member_id
#membership type selection 
def get_membership_type():
    df = pd.read_csv('/workspaces/csv/fit_life.csv')
    membership_ids = df['Membership'].unique().tolist()

    flag = True 

    while flag:
        print('\nSelect a membership')

        for i in range(len(membership_ids)):
            print(i+1,membership_ids[i])
        selection = input('enter number: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            print('invalid input')

        membership_ids = membership_ids[selection -1 ]

        print('you slected: ',membership_ids)

        return membership_ids
 
# -------------------- DATE INPUT --------------------
def get_date(start_end):
    flag = True
 
    while flag:
        date = input(f"Enter {start_end} date (DD/MM/YYYY): ")
 
        try:
            pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Invalid date")
            flag = True
        else:
            flag = False
 
    return date
 
 
# -------------------- DATA FILTER --------------------
def get_data_by_member_and_date(member_id, start_date, end_date):
    df = pd.read_csv("/workspaces/csv/fit_life.csv")
 
    member_data = df.loc[df["Member ID"] == member_id].copy()
 
    member_data["Date"] = pd.to_datetime(member_data["Date"], format="%d/%m/%Y")
 
    date_filter = (
        (member_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) &
        (member_data["Date"] <= pd.to_datetime(end_date, format="%d/%m/%Y"))
    )
 
    return member_data.loc[date_filter]
 
# data filter 
def get_data_by_membership_and_date(membership_id, start_date, end_date):
    df = pd.read_csv("/workspaces/csv/fit_life.csv")
 
    membership_data = df.loc[df["Membership"] == membership_id].copy()
 
    membership_data["Date"] = pd.to_datetime(membership_data["Date"], format="%d/%m/%Y")
 
    date_filter = (
        (membership_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) &
        (membership_data["Date"] <= pd.to_datetime(end_date, format="%d/%m/%Y"))
    )
 
    return membership_data.loc[date_filter]
# -------------------- CALCULATION --------------------
def calculate_total_visits(data, member_id, start_date, end_date):
    total = data["Visits"].sum()
 
    print(f"\nTotal visits for {member_id} between {start_date} and {end_date}: {total}")

def calculate_total_membersip(data, Membership_type, start_date, end_date):
    total = data["Visits"].sum()
 
    print(f"\nTotal visits for {Membership_type} between {start_date} and {end_date}: {total}")
 
 
# -------------------- MAIN PROGRAM --------------------
choice = main_menu()
 
if choice == 1:
    member_id = get_member_id()
    start_date = get_date("start")
    end_date = get_date("end")
 
    data = get_data_by_member_and_date(member_id, start_date, end_date)
    calculate_total_visits(data, member_id, start_date, end_date)

elif choice == 2:
    Membership_type = get_membership_type()
    start_date = get_date('start')
    end_date = get_date('end')

    data =  get_data_by_membership_and_date(Membership_type, start_date,end_date)
    calculate_total_membersip(data, Membership_type, start_date, end_date)


#elif choice == 3:
    
