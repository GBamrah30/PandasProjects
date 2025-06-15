import matplotlib.pyplot as plt
from tracker import BudgetTracker
from data_graphs import Graphs

def show_menu():
    print(f"\nWelcome to the Budget Tracker App! Please select from the menu below.")
    print(f"\n1) Load your data")
    print(f"2) View your data")
    print(f"3) Add new entry (row)")
    print(f"4) Add new column")
    print(f"5) Delete row")
    print(f"6) Delete column")
    print(f"7) Show graphs")
    print(f"8) Save data")
    print(f"9) Exit Program\n")
    
def main():
    tracker = BudgetTracker()
    
    while True:
        show_menu()
        
        choice = input(f"\nEnter your choice from 1-9: ").strip()
        if choice == '1':
            tracker.load_data()
        elif choice == '2':
            tracker.data_overview()
        elif choice == '3':
            tracker.add_entry()
        elif choice == '4':
            tracker.add_column()
        elif choice == '5':
            tracker.delete_row()
        elif choice == '6':
            tracker.delete_column()
        elif choice == '7':
            if tracker.df.empty:
                print("No data loaded. Please load your data first.")
                continue
            
            graph = Graphs(tracker.df)
                
            while True:
                print(f"\nPlease select which graph you would like from the options below: ")
                print(f"\na) Spend by category")
                print(f"b) Average spend")
                print(f"c) Spend over time")
                print(f"d) Monthly spend")
                print(f"e) Stats by category")
                print(f"f) Cumulative spend")
                print(f"g) KDE plot")
                print(f"h) Return to main menu")
                
                graph_choice = input("Select a graph from a-h: ").strip().lower()
                
                if graph_choice == 'a':
                    fig = graph.spend_by_category()
                elif graph_choice == 'b':
                    fig = graph.average_spend()
                elif graph_choice == 'c':
                    fig = graph.spend_over_time()
                elif graph_choice == 'd':
                    fig = graph.monthly_spend()
                elif graph_choice == 'e':
                    fig = graph.category_stats()
                elif graph_choice == 'f':
                    fig = graph.cumulative_spend()
                elif graph_choice == 'g':
                    fig = graph.kde_plot()
                elif graph_choice == 'h':
                    break
                else:
                    print(f"Please select a valid value between a-h.")
                    continue
                
                plt.show()
            
        elif choice == '8':
            tracker.save_data()
        elif choice == '9':
            print(f"Now exiting the program.")
            break
        else:
            print(f"Please enter a value between 1-9")
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram exited by user.")
    main()     