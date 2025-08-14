# Questions and options in list form
questions = [
    ("Which is a correct way to create a list?", ["A) [1,2,3]", "B) (1,2,3)", "C) {1,2,3}", "D) \"1,2,3\""], "A"),
    ("Which is immutable?", ["A) List", "B) Tuple", "C) Set", "D) Dictionary"], "B"),
    ("How to create a tuple with one element 5?", ["A) (5)", "B) (5,)", "C) [5]", "D) {5}"], "B"),
    ("Which statement about sets is correct?", ["A) Allow duplicates", "B) Ordered", "C) Mutable", "D) Can store lists"], "C"),
    ("How to add 10 to s={1,2,3}?", ["A) add(10)", "B) append(10)", "C) insert(10)", "D) [10]=10"], "A")
]

# User information
user = {"name": input("Enter your name: "), "score": 0, "answers": {}}

# Quiz loop with question number and option
for idx, (question, options, correct) in enumerate(questions):
    print(f"\nQ{idx+1}: {question}")
    for opt in options:
        print(opt, end="\t")
    print()
    
    while True:
        answer = input("Enter option A/B/C/D: ").upper()
        if answer not in ["A", "B", "C", "D"]:
            print("Invalid input! Enter A, B, C, or D.")
            continue
        else:
            break
    
    # Store user answer
    user["answers"][question] = {"your_answer": answer, "correct_answer": correct}
    if answer == correct:
        user["score"] += 1

# Show results and correct answer
print("\nQuiz Over!")
print(f"{user['name']}, your score is: {user['score']}/{len(questions)}")
print("Your answers vs Correct answers:")
for q, a in user["answers"].items():
    print(f"{q} -> Your answer: {a['your_answer']} | Correct answer: {a['correct_answer']}")
