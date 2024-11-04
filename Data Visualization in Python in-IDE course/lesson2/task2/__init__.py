def test_answers():
    # Učenik unosi svoje odgovore ovde
    answers = {
        "Question 1": "a",  # <-- Zameni sa svojim odgovorom, npr. "a", "b", ili "c"
        "Question 2": "c",
        "Question 3": "a",
        "Question 4": "a"
    }

    # Tačni odgovori
    correct_answers = {
        "Question 1": "a",
        "Question 2": "c",
        "Question 3": "a",
        "Question 4": "a"
    }

    # Provera odgovora
    for question, correct_answer in correct_answers.items():
        user_answer = answers[question]
        assert user_answer == correct_answer, f"{question} is incorrect. The correct answer is '{correct_answer}'."

    print("All answers are correct!")


test_answers()
