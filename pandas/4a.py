import pandas as pd
import matplotlib.pyplot as plt

file_path = "/workspaces/codespaces-blank/Task_4a_RBSX_data.csv"

try:
    df = pd.read_csv(file_path)
    df.drop_duplicates(inplace=True)
    df["Date"] = pd.to_datetime(df["Date"], format="mixed")
    df.sort_values("Date", inplace=True)
except:
    print("Error loading file")
    exit()

while True:
    print("\nWelcome to RBSX Group Ltd")
    print("1. Currency Conversion")
    print("2. Compare GBP with other currencies")
    print("3. Check performance of a currency")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print("1. GBP to EUR")
        print("2. EUR to GBP")
        print("3. GBP to AUD")
        print("4. AUD to GBP")
        print("5. GBP to JPY")
        print("6. JPY to GBP")
        print("7. GBP to USD")
        print("8. USD to GBP")

        conversions = {
            "1": "GBP +AC0- EUR",
            "2": "EUR +AC0- GBP",
            "3": "GBP +AC0- AUD",
            "4": "AUD +AC0- GBP",
            "5": "GBP +AC0- JPY",
            "6": "JPY +AC0- GBP",
            "7": "GBP +AC0- USD",
            "8": "USD +AC0- GBP"
        }

        c = input("Choose conversion: ")

        if c in conversions:
            currency = conversions[c]
            rate = df[currency].iloc[-1]

            try:
                amount = float(input("Enter amount: "))
                result = amount * rate
                print(amount, currency[:3], "=", round(result, 2), currency[-3:])
            except:
                print("Invalid amount")
        else:
            print("Invalid option")

    elif choice == "2":
        gbp_cols = [col for col in df.columns if col.startswith("GBP")]

        for col in gbp_cols:
            print("\nCurrency:", col)
            print("Min:", df[col].min())
            print("Max:", df[col].max())

            if df[col].iloc[-1] > df[col].iloc[0]:
                print("GBP went up overall")
            elif df[col].iloc[-1] < df[col].iloc[0]:
                print("GBP went down overall")
            else:
                print("No change")

            plt.plot(df["Date"], df[col])
            plt.title(col)
            plt.xticks(rotation=45)
            plt.show()

    elif choice == "3":
        cols = [col for col in df.columns if col != "Date"]

        for i in range(len(cols)):
            print(i + 1, cols[i])

        try:
            num = int(input("Select number: "))
            selected = cols[num - 1]

            start = df[selected].iloc[0]
            end = df[selected].iloc[-1]

            change = ((end - start) / start) * 100

            print("Start:", start)
            print("End:", end)
            print("Change %:", round(change, 2))

            if change > 0:
                print("Currency increased")
            elif change < 0:
                print("Currency decreased")
            else:
                print("No change")

            plt.plot(df["Date"], df[selected])
            plt.title(selected)
            plt.xticks(rotation=45)
            plt.show()

        except:
            print("Invalid selection")

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid choice")