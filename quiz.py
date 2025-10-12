from question import Question

question_prompts = [
    "What is the capital of India?\n(a) New Delhi\n(b) Mumbai\n(c) Kolkata\n\n",
    "What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n\n",
    "What is the capital of USA?\n(a) Washington D.C.\n(b) New York\n(c) Los Angeles\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")  
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer.lower():
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions)) + " correct.")

run_quiz(questions)