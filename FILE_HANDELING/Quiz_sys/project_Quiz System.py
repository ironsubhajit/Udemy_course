question = open('questions.txt', 'r')
question_list = [line.strip() for line in question.readlines()]
question.close()

score = 0
total = len(question_list)

for line in question_list:
    q, a = line.split("=")
    ans = input("{}=".format(q))
    if a == ans:
        score += 1

result = open("result.txt", 'w')
result.write("your final score is: {}/{}".format(score, total))
result.close()