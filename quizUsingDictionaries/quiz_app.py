# dictionary (quiz questions and answers)
# variable to keep track of the score
# loop through the dictionary (key : value) pairs
# display the question
# get the user answer
# check if the answer is correct
# show the final result when the loop ends

quiz = {
    "question1": {
        "question": "What musical term is indicates a chord where the notes are played one after another rather than all together?",
        "answer": "Arpeggio"
    },
    "question2": {
        "question": "Which architect designed the Woolworth Building in New York City?",
        "answer": "Gilbert Cass"
    },
    "question3": {
        "question": "At which hospital did the first heart transplant take place?",
        "answer": "Groote Schuur Hospital"
    },
    "question4": {
        "question": "Ken Thompson and Dennis Ritchie co-created which operating system?",
        "answer": "Unix"
    },
    "question5": {
        "question": "What were the earliest forms of contraceptive made from?",
        "answer": "Crocodile Dung"
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Your answer: ")

    # .lower is being used to make the comparison case-insensitive
    if answer.lower() == value["answer"].lower():
        print("Correct!")
        score = score + 1
        print(f"Your score is {score} \n")
    else:
        print("Incorrect!")
        print(f"The correct answer is {value['answer']}")
        print(f"Your score is {score} \n")

print(f"Your final score is {score} out of {len(quiz)}")
print(f"Your percentage score is {score / len(quiz) * 100}%")
print("Thank you for playing!")
