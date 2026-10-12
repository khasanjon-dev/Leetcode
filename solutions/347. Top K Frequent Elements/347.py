def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [item[0] for item in sorted_items[:k]]


print(top_k_frequent(nums=[1, 1, 1, 2, 2, 3], k=2))
