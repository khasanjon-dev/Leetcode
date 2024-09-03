from string import ascii_lowercase as letters


def get_lucky(s: str, k: int) -> int:
    numbers = ""
    for let in s:
        numbers += str(letters.index(let) + 1)
    for _ in range(k):
        numbers = sum((int(num) for num in str(numbers)))
    return int(numbers)


print(get_lucky("leetcode", 2))
