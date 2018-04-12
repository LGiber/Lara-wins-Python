student = 1
students = {}
K = int(input())

while True:
    student = input().rsplit(None, 3)
    if not student:
        break
    if all(not int(i) < 40 for i in student[1:]):
        students[student[0]] = sum(map(int, student[1:]))
        pass_list = sorted(students, key=students.get, reverse=True)
        if len(students) <= K:
            print(0)
        elif students[pass_list[K - 1]] > students[pass_list[K]]:
            print(students[pass_list[K - 1]])
        else:
            print(1)
