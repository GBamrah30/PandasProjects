import json
import os
import random

class Flashcards:

    def __init__(self):
        self.flashcard_dict = {}
    
    def add_flashcard(self):
        while True:
            print("Enter the following information for the flashcard or press 'q' to quit.")
            term = input("Front of card: ")
            if term.lower() == 'q':
                print("Exiting the program.")
                break

            if term in self.flashcard_dict:
                print("This term already exists. Please enter a different term.")
                continue

            definition = input("Back of card: ")
            self.flashcard_dict[term] = definition
            print(f"Flashcard added: {term} - {definition}")
                
    def display_flashcard(self):
        print(f"Below are all your flashcards:")
        for term, definition in self.flashcard_dict.items():
            print(f"\nFront: {term}\nBack: {definition}")

        user_input = input(f"\nPress 'q' to go back to the main screen.")
        if user_input.lower() == 'q':
            return
    
    def remove_flashcard(self):
        print("Here are your current flashcards:")
        self.display_flashcard()  # Calls your method to show all cards.
        print("To delete a flashcard, type the term on the front of the card or type 'q' to quit.")
        user_input = input("Enter term: ")

        if user_input.lower() == 'q':
            return
        # Try case-insensitive match
        matched_term = None
        for term in self.flashcard_dict:
            if term.lower() == user_input.lower():
                matched_term = term
                break

        if matched_term:
            del self.flashcard_dict[matched_term]
            print(f"Flashcard '{matched_term}' removed.")
        else:
            print("That is not one of your flashcards.")
            
    def _get_file_path(self, filename):
        return os.path.join(os.path.dirname(__file__), filename)
            
    def save_flashcard(self, filename='flashcards.json'):
        path = self._get_file_path(filename)
        with open(path, 'w') as json_file:
            json.dump(self.flashcard_dict, json_file, indent=4)
            print("Flashcards saved successfully.")
        
    def load_flashcard(self, filename='flashcards.json'):
        path = self._get_file_path(filename)
        print("Loading from:", path)
        try:
            with open(path, 'r') as json_file:
                # load the json flashcard file into self.flashcard_dict to use moving forward
                self.flashcard_dict = json.load(json_file)
                print("Flashcards loaded successfully.")
        except FileNotFoundError:
            # Try/except prevents app from crashing if file does not exist
            print("No saved flashcards found. Starting with an empty set.")
        except json.JSONDecodeError as e:
            print("Error loading flashcards:", e)
    
    def review_flashcard(self):
        while True:
            review = input("Type '1' to see a term and guess the definition, '2' to see a definition and guess the term, or 'q' to quit: ")
            if review == 'q':
                return
            if not self.flashcard_dict:
                print("No flashcards available. Add some first.")
                return
            term, definition = random.choice(list(self.flashcard_dict.items()))
            if review == '1':
                print(f"What is the definition for: {term}")
                answer = input()
                if answer.strip().lower() == definition.strip().lower():
                    print("You are correct!")
                else:
                    print(f"The correct definition was: {definition}")
            elif review == '2':
                print(f"What is the term for: {definition}")
                answer = input()
                if answer.strip().lower() == term.strip().lower():
                    print("You are correct!")
                else:
                    print(f"The correct term was: {term}")   
            else:
                print("Invalid input. Please enter '1', '2' or 'q'.")         
    