import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tempfile
import webbrowser

class BudgetTracker:
    def __init__(self):
        try:
            self.df = pd.read_csv('./BudgetTracker.csv')
            print(f"Successfully loaded your Budget Tracker")
        except FileNotFoundError:
            print("No dataset found. Starting with an empty set.")
            self.df = pd.DataFrame(columns=['date', 'category', 'amount', 'description'])
    
    def save_data(self):
        self.df.to_csv('./BudgetTracker.csv', index=False)
        print(f"Dataset successfully saved!")
        
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
            print(f"Add is the title of your new column or press q to quit.")
            title = input("\nNew column title: ")
            if title == 'q':
                return
            else:
                self.df.concat([title], axis=1)
        
    def add_entry(self):
        while True:
            print(f"Follow the prompts below to enter data into a new row or press q to quit.")
            for column in self.df.columns:
                new_row = {}}
                if row == 'q':
                    return
                else:
                    pass
        
    def remove_entry(self):
        pass
