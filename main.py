import csv
import random
import threading
import time
import tkinter as tk


import pygame
pygame.mixer.init()
correct_answer = pygame.mixer.Sound("correct-83487.mp3")
wrong_answer = pygame.mixer.Sound("y2mate.com - Wrong Answer Sound effect.mp3")
time_out = pygame.mixer.Sound("mixkit-sad-game-over-trombone-471.wav")
pygame.mixer.music.load("y2mate.com - Merry Go Round Of Life from Howls Moving Castle  Vitamin String Quartet.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)
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
    def __init__(self, questions, total_time = 100):
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
        # timer_thread = threading.Thread(target=self.countdown, args=(10,))  # 10 seconds timer
        # timer_thread.start()


        cowsay.cow(f"{Fore.RED}Question {index}{Style.RESET_ALL}: {Fore.BLUE}{question[0]}{Style.RESET_ALL}")

        user_input = input("Enter your answer: ")

        if self.time_out:
            time_out.play()
            cowsay.tux(f"{Fore.RED}your time is out!!!{Style.RESET_ALL} The answer is: {Fore.BLUE}{question[1]}{Style.RESET_ALL}")

        else:
            if user_input.strip().lower() == question[1].lower():
                correct_answer.play()
                cowsay.tux(f"{Fore.BLUE}Correct!{Style.RESET_ALL}")
                self.score += 1
            else:
                wrong_answer.play()
                cowsay.tux(
                    f"{Fore.RED}Wrong!{Style.RESET_ALL} The answer is: {Fore.BLUE}{question[1]}{Style.RESET_ALL}")

        #timer_thread.join()  # Wait for the timer thread to finish
        print(f"Your current score: {self.score}/{index}\n")
    def word_question(self, index, question):
        user_input = input("Enter a letter")


        answer_length = len(question[1])  # Length of the correct answer
        hidden_word = ['_' for _ in range(answer_length)]  # Create a list of underscores
        attempts = 0  # Track the number of attempts

        while '_' in hidden_word and not self.time_out:
            # Display the current state of the word with underscores
            print("Your answer: " + ' '.join(hidden_word))
            user_input = input(f"Guess a letter (Attempt {attempts + 1}): ").strip().lower()

            if len(user_input) != 1 or not user_input.isalpha():
                print("Please enter a single letter.")
                continue

            if user_input in question[1].lower():
                for i, letter in enumerate(question[1].lower()):
                    if letter == user_input:
                        hidden_word[i] = question[1][i]  # Reveal the correct letter
                print(f"{Fore.BLUE}Correct guess!{Style.RESET_ALL}")
            else:
                wrong_answer.play()
                print(f"{Fore.RED}Wrong guess!{Style.RESET_ALL}")
            attempts +=1

    def countdown(self, time_limit):
        print(f"You have{Fore.LIGHTRED_EX} {time_limit}{Style.RESET_ALL} seconds to answer this question.")
        self.time_out = True

def save_results(pangalan,difficulty, file_name,  score):
    with open('quiz_results.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([pangalan,difficulty, file_name,  score])


def main():
    print_title()
    while True:
        pangalan = input("Enter your name first before we proceed: ").strip()
        if pangalan:  # Check if the input is not empty
            break
        else:
            print("You need to enter your name!")

    print(f"Welcome {pangalan} to UCQ!!")
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
            file_name = "WWTBAPBnormal.csv"  # Use TriviaNormal.csv for normal difficulty
        elif difficulty_choice == '3':
            difficulty = "expert"
            file_name = "WWTBAPBexpert.csv"  # Assuming you have this file for expert questions
        else:
            print("Invalid choice. Please select a valid difficulty level.")
            return

    elif choice == '3':
        if difficulty_choice == '1':
            difficulty = "easy"
            file_name = "MathC.csv"  # Assuming you have this file for easy question
        elif difficulty_choice == '2':
            difficulty = "normal"
            file_name = "MathCNormal.csv"  # Use TriviaNormal.csv for normal difficulty
        elif difficulty_choice == '3':
            difficulty = "expert"
            file_name = "MathCExpert.csv"  # Assuming you have this file for expert questions
        else:
            print("Invalid choice. Please select a valid difficulty level.")
            return

    elif choice == '4':


        if difficulty_choice == '1':
            difficulty = "easy"
            file_name = "Word Puzzle.csv"  # Assuming you have this file for easy question
        elif difficulty_choice == '2':
            difficulty = "normal"
            file_name = "WordPuzzleNormal.csv"  # Use TriviaNormal.csv for normal difficulty
        elif difficulty_choice == '3':
            difficulty = "expert"
            file_name = "WWTBAPBexpert.csv"  # Assuming you have this file for expert questions
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
    while True:
        main()
        choice = input("play again? ")
        if(choice == "no"):
            break