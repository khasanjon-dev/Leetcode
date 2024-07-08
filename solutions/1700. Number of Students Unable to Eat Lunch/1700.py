def count_students(students: list[int], sandwiches: list[int]) -> int:
    while students and sandwiches:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
        else:
            if len(set(students)) == 1:
                return len(students)
            student = students.pop(0)
            students.append(student)
    return 0

print(count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
