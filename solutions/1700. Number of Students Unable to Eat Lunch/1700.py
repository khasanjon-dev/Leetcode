# def count_students(students: list[int], sandwiches: list[int]) -> int:
#     for i in range(len(sandwiches)):
#         if sandwiches[i] == students[i]:
#             pass
import heapq
heap = [4, 1, 7, 3, 9, 5]
heapq.heappush(heap, 2)
print(heap)