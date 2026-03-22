import random

# Questions database
questions = [
    {"question": "What is the capital of India?",
     "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
     "answer": 1},

    {"question": "Which planet is known as the Red Planet?",
     "options": ["Earth", "Mars", "Jupiter", "Saturn"],
     "answer": 1},

    {"question": "Who wrote the national anthem of India?",
     "options": ["Rabindranath Tagore", "Mahatma Gandhi", "Subhas Chandra Bose", "Bankim Chandra Chatterjee"],
     "answer": 0},

    {"question": "Which is the largest ocean in the world?",
     "options": ["Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean"],
     "answer": 3},

    {"question": "What is the currency of Japan?",
     "options": ["Won", "Dollar", "Yen", "Euro"],
     "answer": 2},

    {"question": "Which gas do plants absorb from the atmosphere?",
     "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
     "answer": 1},

    {"question": "Who is known as the Father of Computers?",
     "options": ["Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs"],
     "answer": 1},

    {"question": "Which is the smallest prime number?",
     "options": ["0", "1", "2", "3"],
     "answer": 2},

    {"question": "Which continent is known as the Dark Continent?",
     "options": ["Asia", "Africa", "Europe", "Australia"],
     "answer": 1},

    {"question": "How many players are there in a cricket team?",
     "options": ["9", "10", "11", "12"],
     "answer": 2}
]

# Prize ladder
prizes = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000]

# Lifelines
lifelines = {
    "50-50": True,
    "skip": True
}

def use_5050(q):
    correct = q["answer"]
    options = list(range(4))
    options.remove(correct)
    wrong = random.choice(options)
    return [correct, wrong]

def play_game():
    random.shuffle(questions)
    winnings = 0

    print("\n🎮 Welcome to KBC Python Edition 🎮\n")

    for i, q in enumerate(questions):
        print(f"\n💰 Question for ₹{prizes[i]}:")
        print(q["question"])

        for idx, opt in enumerate(q["options"]):
            print(f"{idx}. {opt}")

        # Lifeline choice
        if any(lifelines.values()):
            print("\nAvailable lifelines:")
            for key, val in lifelines.items():
                if val:
                    print(f"- {key}")

            choice = input("Do you want a lifeline? (yes/no): ").lower()

            if choice == "yes":
                lifeline_choice = input("Enter lifeline name: ").lower()

                if lifeline_choice == "50-50" and lifelines["50-50"]:
                    lifelines["50-50"] = False
                    valid_options = use_5050(q)
                    print("\nRemaining options:")
                    for idx in valid_options:
                        print(f"{idx}. {q['options'][idx]}")

                elif lifeline_choice == "skip" and lifelines["skip"]:
                    lifelines["skip"] = False
                    print("⏭️ Question skipped!")
                    continue

                else:
                    print("Invalid or already used lifeline.")

        try:
            ans = int(input("Enter your answer (0-3): "))
        except:
            print("Invalid input! Game Over.")
            break

        if ans == q["answer"]:
            winnings = prizes[i]
            print(f"✅ Correct! You won ₹{winnings}")
        else:
            print("❌ Wrong answer!")
            print(f"Correct answer was: {q['options'][q['answer']]}")
            break

    print(f"\n🏁 Game Over! Your total winnings: ₹{winnings}")


# Run game
play_game()