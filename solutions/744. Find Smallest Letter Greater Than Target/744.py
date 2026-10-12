def next_greatest_letter(letters: list[str], target: str) -> str:
    left, right = 0, len(letters) - 1
    answer = 0
    while left <= right:
        mid = (right + left) // 2
        if letters[mid] <= target:
            left = mid + 1
        elif letters[mid] >= target:
            answer = mid
            right = mid - 1
    return letters[answer]


print(next_greatest_letter(letters=["c", "f", "j"], target="c"))
