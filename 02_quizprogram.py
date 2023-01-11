# Lets make A Quiz Program :)

quiz = {
    "question1": {
        "question": "What is the Capital of Punjab",
        "answer": "Chandigarh"
    },
    "question2": {
        "question": "What is the Capital of Turkey",
        "answer": "Istanbul"
    },
    "question3": {
        "question": "What is the Capital of France",
        "answer": "Paris"
    },
    "question4": {
        "question": "What is the Capital of Russian Federation",
        "answer": "Moscow"
    },
    "question5": {
        "question": "What is the Capital of USA",
        "answer": "Washington D.C."
    },
    "question5": {
        "question": "What is the Capital of Switzerland",
        "answer": "Bern"
    },
    "question6": {
        "question": "What is the Capital of Austria",
        "answer": "Vienna"
    },
    "question7": {
        "question": "What is the Capital of Germany",
        "answer": "Berlin"
    },
}

score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value[ 'answer'] . lower():
        print("Correct")
        score = score + 1
        print("Your Score Is: " +str(score))
        print("")
        print("")
    else:
        print("Wrong")
        print("The Answer is: " + value[ ' answer'])
        print("Your Score Is: " +str(score))
        print("")
        print("")
    
print(" You Got" + str(score) + "out of 7 questions correctly")
print("Your Percentage is " + str(int(score/7 * 100)) + "%")

# lets Run It
# some bug lets ignore it