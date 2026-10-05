import pandas as pd
import matplotlib.pyplot as plt
import os


data = {
    "SalesID": [101, 102, 103, 104, 105],

    "Product": ["Product A", "Product B", "Product C", "Product D", "Product E"],

    "Region": ["North", "East", "West Coast", "South", "Central"],
    
    "Sales": [500, 600, 700, 800, 550],
        
    "Year": [2022, 2022, 2022, 2022, 2022]
}

df = pd.DataFrame(data)

os.makedirs("data", exist_ok=True)

df.to_csv("Customer_data.csv", index=False)

plot = None


while True:

    print("\n========== Data Analysis & Visualization Program ==========")
    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("==========================================================")

    choice = input("\nEnter your choice: ")


    if choice == "1":

        print("\n== Load Dataset ==")

        path = input(
            "Enter the path of the dataset (CSV file): "
        )

        try:
            df = pd.read_csv(path)
            print("Dataset loaded successfully!")

        except FileNotFoundError:
            print("Dataset file not found!")


    elif choice == "2":

        print("\n== Explore Data ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")

        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":

            print()
            print(df.head())

        elif sub_choice == "2":

            print()
            print(df.tail())

        elif sub_choice == "3":

            print()
            print(df.columns)

        elif sub_choice == "4":

            print()
            print(df.dtypes)

        elif sub_choice == "5":

            print()
            df.info()



    elif choice == "3":

        print("\n== Perform DataFrame Operations ==")
        print("1. Display Shape")
        print("2. Display Columns")
        print("3. Sort Data")
        print("4. Filter Data")

        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":

            print("\nShape:")
            print(df.shape)

        elif sub_choice == "2":

            print("\nColumns:")
            print(df.columns.tolist())

        elif sub_choice == "3":

            print("\nSorted Data:")
            print(df.sort_values("Sales"))

        elif sub_choice == "4":

            print("\nFiltered Data:")
            print(df[df["Sales"] > 600])


    elif choice == "4":

        print("\n== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")

        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":

            if df.isnull().sum().sum() == 0:

                print(
                    "\nNo missing values found in the dataset!"
                )

            else:

                print(
                    df[df.isnull().any(axis=1)]
                )

        elif sub_choice == "2":

            df.fillna(
                df.mean(numeric_only=True),
                inplace=True
            )

            print(
                "Missing values filled successfully!"
            )

        elif sub_choice == "3":

            df.dropna(inplace=True)

            print(
                "Rows with missing values dropped!"
            )

        elif sub_choice == "4":

            value = input(
                "Enter value: "
            )

            df.fillna(value,inplace=True)
            

            print("Missing values replaced successfully!")


    elif choice == "5":

        print("\n== Descriptive Statistics ==")
        
        print(df.describe())

    elif choice == "6":

        print("\n== Data Visualization ==")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")

        sub_choice = input("Enter your choice: ")
        

        if sub_choice == "1":

            x = input( "Enter x-axis column name: ")
            
            y = input("Enter y-axis column name: ")
            
            plt.figure()

            plt.bar(
                df[x],
                df[y]
            )

            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("Bar Plot")

            plot = plt.gcf()

            print("Generating bar plot...")
            
            plt.show()

            print("Bar plot displayed successfully!")
            

        elif sub_choice == "2":

            x = input("Enter x-axis column name: ")
            

            y = input("Enter y-axis column name: ")
            
            plt.figure()

            plt.plot(
                df[x],
                df[y],
                marker="o"
            )

            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("Line Plot")

            plot = plt.gcf()

            print("Generating line plot...")
            
            plt.show()

            print("Line plot displayed successfully!")
            

        elif sub_choice == "3":

            print("\n== Scatter Plot ==")

            x = input("Enter x-axis column name: ")
            

            y = input("Enter y-axis column name: ")
            
            plt.figure()

            plt.scatter(
                df[x],
                df[y]
            )

            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("Scatter Plot")

            plot = plt.gcf()

            print("Generating scatter plot...")
            

            plt.show()

            print("Scatter plot displayed successfully!")
            

        elif sub_choice == "4":

            column = input("Enter column name: ")
  
            values = df[column].value_counts()

            plt.figure()

            plt.pie(
                values,
                labels=values.index,
                autopct="%1.1f%%"
            )

            plt.title("Pie Chart")

            plot = plt.gcf()

            print("Generating pie chart...")
            
            plt.show()

            print("Pie chart displayed successfully!")
            

        elif sub_choice == "5":

            column = input("Enter column name: ")
            
            plt.figure()

            plt.hist(
                df[column],
                bins=10
            )

            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.title("Histogram")

            plot = plt.gcf()

            print("Generating histogram...")
            

            plt.show()

            print("Histogram displayed successfully!")
            

        elif sub_choice == "6":

            numeric = df.select_dtypes(include="number")
            
            plt.figure()

            plt.stackplot(
                range(len(df)),
                *numeric.iloc[:, :3].T.values,
                labels=numeric.columns[:3]
            )

            plt.xlabel("Index")
            plt.ylabel("Values")
            plt.title("Stack Plot")

            plt.legend()

            plot = plt.gcf()

            print("Generating stack plot...")
            

            plt.show()

            print("Stack plot displayed successfully!" )

    elif choice == "7":

        print("\n== Save Visualization ==")

        filename = input(
            "Enter file name to save the plot "
            "(e.g., scatter_plot.png): "
        )

        if plot is not None:

            plot.savefig(filename)

            print(
                "Visualization saved as "
                + filename
                + " successfully!"
            )

        else:

            print("No visualization available!")

    elif choice == "8":

        print("\nExiting the program. Goodbye!")

        break

    else:

        print("\nInvalid choice! Please try again.")