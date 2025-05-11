import sys
from flashcard import Flashcards

def show_menu():
    print(f"\nWelcome to the Flashcard App.")
    print("\n1. Load a flashcard")
    print("2. Test yourself")
    print("3. Display current flashcards")
    print("4. Add a flashcard")
    print("5. Remove a flashcard")
    print("6. Save flashcards")
    print("7. Quit\n")

def main():
    my_flashcards = Flashcards()
    my_flashcards.load_flashcard()
    
    while True:
        show_menu()
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            my_flashcards.load_flashcard()
        elif choice == '2':
            my_flashcards.review_flashcard()
        elif choice == '3':
            my_flashcards.display_flashcard()
        elif choice == '4':
            my_flashcards.add_flashcard()
        elif choice == '5':
            my_flashcards.remove_flashcard()
        elif choice == '6':
            my_flashcards.save_flashcard()
        elif choice == '7':
            print("Thanks for using the flashcard app!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()      