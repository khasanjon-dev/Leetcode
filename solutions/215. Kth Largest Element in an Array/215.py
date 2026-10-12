import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            heapq.heappushpop(heap, num)
    return heap[0]


print(find_kth_largest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
