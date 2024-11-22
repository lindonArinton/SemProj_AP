import csv
import random

def print_title():
    title = "🅆🄴🄻🄲🄾🄼🄴 🅃🄾 🅄🄻🅃🄸🄼🄰🅃🄴 🄲🄷🄰🄻🄻🄴🄽🄶🄴 🅀🅄🄸🅉"
    width = 80
    centered_title = title.center(width)
    print("+------------------------------------------------------------------------------------------------------+")
    print(f"| {centered_title} |")
    print("|  Test Your Knowledge and Unleash Your Inner Genius!                                                  |")
    print("+------------------------------------------------------------------------------------------------------+")

def display_category_options():
    print("Choose a category:")
    options = [
        "1. Trivia",
        "2. Who Wants to be A Python Billionaire",
        "3. Math Challenge",
        "4. Word Puzzle"
    ]
    for option in options:
        print(option)
    print("=" * 50)

def display_difficulty_options():
    print("Choose a difficulty level:")
    difficulties = [
        "1. Easy",
        "2. Normal",
        "3. Expert"
    ]
    for difficulty in difficulties:
        print(difficulty)
    print("=" * 50)

def main():
    print_title()
    input("Press Enter to reveal the category...")

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

    # Shuffle the questions randomly
    random.shuffle(questions)

    # Quiz Logic
    score = 0
    for question, answer in questions:
        user_answer = input(f"{question} ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")

    print(f"Your score: {score}/{len(questions)}")  # Display final score

if __name__ == "__main__":
    main()