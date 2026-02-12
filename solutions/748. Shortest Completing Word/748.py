from collections import Counter


def shortest_completing_word(licensePlate: str, words: list[str]) -> str:
    license_count = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
    result = None
    for word in words:
        word_count = Counter(word)
        if all(word_count[w] >= c for w, c in license_count.items()):
            if result is None or len(word) < len(result):
                result = word

    return result


print(
    shortest_completing_word(
        licensePlate="1s3 PSt", words=["step", "steps", "stripe", "stepple"]
    )
)
