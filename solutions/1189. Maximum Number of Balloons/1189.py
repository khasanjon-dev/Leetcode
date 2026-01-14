from collections import Counter


def max_number_of_ballons(text: str) -> int:
    counter = Counter(text)
    return min(
        counter.get("b", 0),
        counter.get("a", 0),
        counter.get("n", 0),
        counter.get("l", 0) // 2,
        counter.get("o", 0) // 2,
    )


print(max_number_of_ballons("leetcode"))
