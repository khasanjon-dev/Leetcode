from collections import Counter


def equal_frequency(word: str) -> bool:
    counter = Counter(word)
    indexes = list(counter.values())
    if (indexes.count(max(indexes)) == 1 and max(indexes) - min(indexes) == 1) or min(indexes) == 1 and max(indexes) == 1:
        return True
    return False


print(equal_frequency('abbcc'))
