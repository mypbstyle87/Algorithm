question_num = int(input())
student_answer = []
correct_answer = []
correct_count = 0

for i in range(question_num):
    student_answer.append(input())
for i in range(question_num):
    correct_answer.append(input())

for i in range(question_num):
    if student_answer[i] == correct_answer[i]:
        correct_count += 1

print(correct_count)