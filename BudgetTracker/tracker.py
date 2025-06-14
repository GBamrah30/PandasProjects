import numpy as np
import pandas as pd
import tempfile
import webbrowser

class BudgetTracker:
    def __init__(self):
        self.df = None
        self.load_data()
        
    def load_data(self):
        while True:    
            choice = input("Would you like to load your own dataset (y/n)?: ").strip().lower()
            if choice == 'y':
                self.user_data()
                break
            elif choice.lower() == 'n':
                print(f"Type '1' if you would like to load the default dataset, or type '2' if you would like a clean dataset")
                user_choice = input("\n Choice: ").strip()
                if user_choice == '1':
                    self.default_data()
                else:
                    self.df = pd.DataFrame(columns=['date', 'category', 'amount', 'description'])
                break
            else:
                print(f"{choice} is not a valid input. Please select 'y' or 'n'.")
    
    def user_data(self):
        user_path = input("Enter your file path here:\n")
        try:
            self.df = pd.read_csv(user_path)
            print(f"File successfully loaded")
        except FileNotFoundError:
            print("Dataset not found. Starting with an empty set.")
            self.df = pd.DataFrame(columns=['date', 'category', 'amount', 'description'])
    
    def default_data(self):
        try:
            self.df = pd.read_csv('./BudgetTracker.csv')
            print(f"Successfully loaded your Budget Tracker")
        except FileNotFoundError:
            print("No dataset found. Starting with an empty set.")
            self.df = pd.DataFrame(columns=['date', 'category', 'amount', 'description'])
    
    def save_data(self):
        save_choice = input(
            "Type '1' to save to your own file,\n"
            "Type '2' to save to the default file,\n"
            "Or press any other key to cancel.\nChoice: "
        ).strip()
        if save_choice == '1':
            user_path = input("Enter the file path to save your data:\n").strip()
            self.df.to_csv(user_path, index=False)
            print(f"Dataset successfully saved to {user_path}.")
        elif save_choice == '2':
            self.df.to_csv('./BudgetTracker.csv', index=False)
            print(f"Dataset successfully saved!")
        else:
             print("Save canceled.")
        
    def data_overview(self):
        while True:
            print(f"Please select from one of the options below to view your data\n")
            print(f"1. Descriptive Statistics of your data")
            print(f"2. Dataframe general information")
            print(f"3. First 5 rows of your data")
            print(f"4. Last 5 rows of your data")
            print(f"5. Randomly view 10 rows from your data")
            print(f"6. Return to the main menu")
            choice = input("Please select from 1-6: ")
            if choice == '1':
                print(self.df.describe())
            elif choice == '2':
                self.df.info()
            elif choice == '3':
                print(self.df.head())
            elif choice == '4':
                print(self.df.tail())
            elif choice == '5':
                print(self.df.sample(n=10))
            elif choice == '6':
                break
            else:
                print("You must enter a number between 1-6.")
            
    def show_df_in_window(self):
        # Show the file as a data frame in a seperate window
        with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as f:
            self.df.to_html(f)
            return webbrowser.open(f.name)
    
    def add_column(self):
        while True:
            print("Enter the title of your new column or press 'q' to quit.")
            title = input("New column title: ").strip()

            if title.lower() == 'q':
                return

            if title in self.df.columns:
                print(f"A column named '{title}' already exists. Try a different name.")
                continue

            # Add the new column with empty strings (or np.nan, or a default value like 0)
            self.df[title] = ""
            print(f"Column '{title}' has been added successfully.")
            
            add_another = input("Would you like to add another column? (y/n): ").strip().lower()
            if add_another != 'y':
                break

        
    def add_entry(self):
        while True:
            print("Follow the prompts below to enter data into a new row or press 'q' at any time to quit.")
            new_row = {}
            for column in self.df.columns:
                user_input = input(f"Enter information for '{column}': ")
                if user_input.lower() == 'q':
                    print("Entry cancelled. Returning to main menu.")
                    return
                new_row[column] = user_input
            # Convert the new_row dict to a DataFrame with one row
            new_row_df = pd.DataFrame([new_row])
            # Append the new row to the main DataFrame
            self.df = pd.concat([self.df, new_row_df], ignore_index=True)
            print("New entry added successfully!\n")
            add_another = input("Would you like to add another entry? (y/n): ")
            if add_another.lower() != 'y':
                break
        
    def delete_row(self):
        print("Follow the prompts below to delete a selected row:")
        while True:
            print(f"\nCurrent number of rows: {len(self.df)}")
            select_row = input("Enter the row number to delete (starting from 0), or press 'q' to quit: ")
            if select_row.lower() == 'q':
                return
            try:
                row_index = int(select_row)
            except ValueError:
                print("Invalid input. Please enter a valid row number.")
                continue

            if row_index < 0 or row_index >= len(self.df):
                print("This row does not exist. Please enter a number between 0 and ", len(self.df) - 1)
                continue

            print("\nSelected row:")
            print(self.df.iloc[row_index])

            while True:
                confirm = input("Are you sure you want to delete this row? (y/n): ").lower()
                if confirm.lower() == 'y':
                    self.df = self.df.drop(self.df.index[row_index]).reset_index(drop=True)
                    print("Row deleted successfully.")
                    break
                elif confirm.lower() == 'n':
                    print("Deletion cancelled.")
                    return
                else:
                    print("Invalid input. Please enter 'y' for yes or 'n' for no.")

    def delete_column(self):

        if len(self.df.columns) <= 1:
            print("You have one or less columns left, you cannot delete anymore.")
            return

        print("Follow the prompts below to delete a selected column:")
        print("\nBelow are your current columns:\n")
        #Print a full list of columns
        for column in self.df.columns:
            print(column)

        while True:
            print("\nPlease type in the name of the column you would like to delete or press 'q' to quit")
            user_input = input("Column name: ").strip()

            if user_input.lower() == 'q':
                return

            # Try to find a column with a matching name (case-insensitive)
            # This is better than using a for loop because this while only yield the column that matches
            matched_column = next((col for col in self.df.columns if col.lower() == user_input.lower()),None)

            if matched_column:
                while True:
                    confirm = input(f"\nAre you sure you want to delete the '{matched_column}' column? (y/n): ").lower()
                    if confirm == 'y':
                        self.df.drop(matched_column, axis=1, inplace=True)
                        print(f"\nColumn '{matched_column}' deleted successfully.")
                        return
                    elif confirm == 'n':
                        print("\nDeletion cancelled.")
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
            else:
                print("That is not one of the columns.")

        