def min_moves_to_seat(seats: list[int], students: list[int]) -> int:
    seats_sort = sorted(seats)
    students_sort = sorted(students)
    moves = 0
    for i, student in enumerate(students_sort):
        seat = seats_sort[i]
        if student != seat:
            moves += abs(student - seat)
    return moves


print(min_moves_to_seat([4, 1, 5, 9], [1, 3, 2, 6]))
