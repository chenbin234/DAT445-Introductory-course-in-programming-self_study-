# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# dispaly each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is cpmpleted
quiz = {
    "question1": {
        "question": "What is the captical of France?",
        "answer": "Pairs"
    },
    "question2": {
        "question": "What is the captical of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the captical of Spain?",
        "answer": "Madrid"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer?')

    if answer.lower() == value['answer'].lower():
        print('Correct!')
        score = score + 1
        print('your score is ' + str(score))
        print("")
        print("")
    else:
        print('wrong!')
        print("The answer is: " + value['answer'])
        print('your score is ' + str(score))
        print("")
        print("")
