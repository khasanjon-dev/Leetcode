def num_of_subarrays(arr: list[int], k: int, threshold: int) -> int:
    max_count = 0
    threshold *= k
    window_sum = sum(arr[:k])

    if window_sum >= threshold:
        max_count += 1

    for right in range(k, len(arr)):
        window_sum += arr[right]
        window_sum -= arr[right - k]

        max_count += window_sum >= threshold

    return max_count


print(num_of_subarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))
