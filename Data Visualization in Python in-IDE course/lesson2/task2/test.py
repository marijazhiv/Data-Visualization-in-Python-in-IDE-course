# Učitavanje odgovora iz main.py
from main import answer_1, answer_2, answer_3, answer_4

# Tačni odgovori
correct_answers = {
    "Question 1": "a",
    "Question 2": "c",
    "Question 3": "a",
    "Question 4": "a"
}


# Provera odgovora
def test_answers():
    answers = {
        "Question 1": answer_1,
        "Question 2": answer_2,
        "Question 3": answer_3,
        "Question 4": answer_4
    }

    all_correct = True
    for question, correct_answer in correct_answers.items():
        user_answer = answers[question]
        if user_answer != correct_answer:
            print(f"{question} is incorrect. The correct answer is '{correct_answer}'.")
            all_correct = False

    if all_correct:
        print("All answers are correct!")


test_answers()
