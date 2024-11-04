# Import answers from main.py
from main import (
    answer_1, answer_2, answer_3, answer_4,
    answer_5, answer_6, answer_7, answer_8
)

# Correct answers
correct_answers = {
    "Question 1": "a",
    "Question 2": "b",
    "Question 3": "a",
    "Question 4": "b",
    "Question 5": "a",
    "Question 6": "b",
    "Question 7": "b",
    "Question 8": "a"
}

# User's answers from main.py
user_answers = {
    "Question 1": answer_1,
    "Question 2": answer_2,
    "Question 3": answer_3,
    "Question 4": answer_4,
    "Question 5": answer_5,
    "Question 6": answer_6,
    "Question 7": answer_7,
    "Question 8": answer_8
}


# Function to check answers
def test_answers():
    all_correct = True
    for question, correct_answer in correct_answers.items():
        user_answer = user_answers[question]
        if user_answer != correct_answer:
            print(f"{question} is incorrect. The correct answer is '{correct_answer}'.")
            all_correct = False

    if all_correct:
        print("All answers are correct!")


# Run the test
test_answers()
