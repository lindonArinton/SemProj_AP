import csv
import random
import threading
import time

import cowsay
from colorama import Fore, Style


def print_title():
    title = f"{Fore.BLUE}-----🅆🄴🄻🄲🄾🄼🄴 🅃🄾 🅄🄻🅃🄸🄼🄰🅃🄴 🄲🄷🄰🄻🄻🄴🄽🄶🄴 🅀🅄🄸🅉-----{Style.RESET_ALL}"
    width = 89
    centered_title = title.center(width)
    print("+------------------------------------------------------------------------------------------------------+")
    print(f"| {centered_title} |")
    print(f"| {Fore.LIGHTGREEN_EX} Test Your Knowledge and Unleash Your Inner Genius!                                                  {Style.RESET_ALL}|")
    print("+------------------------------------------------------------------------------------------------------+")

def display_category_options():

    print(f"Choose a {Fore.GREEN}CATEGORY{Style.RESET_ALL}:")
    categories = [
        f"{Fore.CYAN}1. Trivia{Style.RESET_ALL}",
        f"{Fore.CYAN}2. Who Wants to be A Python Billionaire{Style.RESET_ALL}",
        f"{Fore.CYAN}3. Math Challenge{Style.RESET_ALL}",
        f"{Fore.CYAN}4. Word Puzzle{Style.RESET_ALL}"
    ]
    for category in categories:
        print(category)
    print("=" * 50)

def display_difficulty_options():
    print("Choose a difficulty level:")
    difficulties = [
        f"{Fore.GREEN}1. Easy{Style.RESET_ALL}",
        f"{Fore.BLUE}2. Normal{Style.RESET_ALL}",
        f"{Fore.RED}3. Expert{Style.RESET_ALL}"
    ]
    for difficulty in difficulties:
        print(difficulty)
    print("=" * 50)

class MgaTanong:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.time_out = False
        random.shuffle(questions)

    def start_quiz(self):
        for index, question in enumerate(self.questions, start=1):
            self.ask_question(index, question)
        print(f"Your final score: {self.score}/{len(self.questions)}")
        return self.score

    def ask_question(self, index, question):
        self.time_out = False
        timer_thread = threading.Thread(target=self.countdown, args=(10,))  # 10 seconds timer
        timer_thread.start()

        cowsay.cow(f"{Fore.RED}Question {index}{Style.RESET_ALL}: {Fore.BLUE}{question[0]}{Style.RESET_ALL}")
        user_answer = input(f"Enter your {Fore.LIGHTGREEN_EX}answer:{Style.RESET_ALL} ")

        if self.time_out:
            cowsay.tux(f"{Fore.RED}your time is out!!!{Style.RESET_ALL} The answer is: {Fore.BLUE}{question[1]}{Style.RESET_ALL}")

        else:
            if user_answer.strip().lower() == question[1].lower():
                cowsay.tux(f"{Fore.BLUE}Correct!{Style.RESET_ALL}")
                self.score += 1
            else:
                cowsay.tux(
                    f"{Fore.RED}Wrong!{Style.RESET_ALL} The answer is: {Fore.BLUE}{question[1]}{Style.RESET_ALL}")

        timer_thread.join()  # Wait for the timer thread to finish
        print(f"Your current score: {self.score}/{index}\n")

    def countdown(self, time_limit):
        print(f"You have{Fore.LIGHTRED_EX} {time_limit}{Style.RESET_ALL} seconds to answer this question.")
        time.sleep(time_limit)
        self.time_out = True

def save_results(pangalan,difficulty, file_name,  score):
    with open('quiz_results.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([pangalan,difficulty, file_name,  score])


def main():
    print_title()
    pangalan = input("Enter your name first before we proceed: ")
    print (f"welcome {pangalan} to UCQ!!")
    ENTER = f"{Fore.BLUE}ENTER{Style.RESET_ALL}"
    input(f"Press {ENTER} to reveal the category...")

    display_category_options()

    choice = input("Please select an option (1-4): ")

    display_difficulty_options()

    difficulty_choice = input("Please select a difficulty level (1-3): ")

    if choice == '1':
        if difficulty_choice == '1':
            difficulty = "easy"
            file_name = "Trivia.csv"  # Assuming you have this file for easy question
        elif difficulty_choice == '2':
            difficulty = "normal"
            file_name = "TriviaNormal.csv"  # Use TriviaNormal.csv for normal difficulty
        elif difficulty_choice == '3':
            difficulty = "expert"
            file_name = "TriviaExpert.csv"  # Assuming you have this file for expert questions
        else:
            print("Invalid choice. Please select a valid difficulty level.")
            return

    elif choice == '2':
        if difficulty_choice == '1':
            difficulty = "easy"
            file_name = "WWTBAPB.csv"  # Assuming you have this file for easy question
        elif difficulty_choice == '2':
            difficulty = "normal"
            file_name = "TriviaNormal.csv"  # Use TriviaNormal.csv for normal difficulty
        elif difficulty_choice == '3':
            difficulty = "expert"
            file_name = "TriviaExpert.csv"  # Assuming you have this file for expert questions
        else:
            print("Invalid choice. Please select a valid difficulty level.")
            return

    elif choice == '3':
        if difficulty_choice == '1':
            difficulty = "easy"
            file_name = "Trivia.csv"  # Assuming you have this file for easy question
        elif difficulty_choice == '2':
            difficulty = "normal"
            file_name = "TriviaNormal.csv"  # Use TriviaNormal.csv for normal difficulty
        elif difficulty_choice == '3':
            difficulty = "expert"
            file_name = "TriviaExpert.csv"  # Assuming you have this file for expert questions
        else:
            print("Invalid choice. Please select a valid difficulty level.")
            return

    elif choice == '4':
        if difficulty_choice == '1':
            difficulty = "easy"
            file_name = "Trivia.csv"  # Assuming you have this file for easy question
        elif difficulty_choice == '2':
            difficulty = "normal"
            file_name = "TriviaNormal.csv"  # Use TriviaNormal.csv for normal difficulty
        elif difficulty_choice == '3':
            difficulty = "expert"
            file_name = "TriviaExpert.csv"  # Assuming you have this file for expert questions
        else:
            print("Invalid choice. Please select a valid difficulty level.")
            return

    else:
        print("Invalid choice. Please select a valid option.")
        return


    # Load questions based on the selected category and difficulty
    print(f"\n--- {file_name.replace('.csv', '').replace('_', ' ').title()} - {difficulty.capitalize()} ---")

    questions = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['difficulty'].lower() == difficulty:
                questions.append((row['question'], row['answer']))  # Store as tuples


    game = MgaTanong(questions)
    score = game.start_quiz()
    random.shuffle(questions)

    save_results(pangalan,difficulty, file_name,  score)
    print(f"Your results have been saved. Thank you for playing, {pangalan}!")


if __name__ == "__main__":
    main()