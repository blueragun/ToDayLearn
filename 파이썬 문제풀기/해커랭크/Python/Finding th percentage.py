n = int(input())
student_marks = {}

result = 0

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

print("{:.2f}".format(sum(student_marks[query_name]) / len(student_marks[query_name])))