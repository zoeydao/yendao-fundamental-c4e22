q1 = {
    "stimulus":"Answer the following algebra questions:",
    "stem":"If x = 8, then what is the value of 4(x+3)?",
    "choices":["1.35","2.36","3.40","4.44"],
    "right choice": 4,
}
q2 = {
    "stimulus":"Estimate this answer (exact calculation not needed):",
    "stem":"Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?",
    "choices":["1.About 55","2.About 65","3.About 75","4.About 85"],
    "right choice": 2,
}

quiz = []
quiz.append(q1)
quiz.append(q2)

right_answers = 0
for i in range(len(quiz)):
    print(quiz[i]["stimulus"])
    print(quiz[i]["stem"])
    print(*quiz[i]["choices"], sep='\n')
    answer = input("Your choice: ")
    if answer.isdigit():
        answer = int(answer)
        if answer == quiz[i]["right choice"]:
            print("Bingo")
            right_answers += 1
        else:
            print(":(")
    else:
        print(":(")

print("You correctly answer",right_answers,"out of",len(quiz),"questions")


