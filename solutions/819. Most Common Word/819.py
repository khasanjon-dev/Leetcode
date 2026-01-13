import re
from collections import Counter


def most_common_word(paragraph: str, banned: list[str]) -> str:
    cleaned_paragraph = re.split(r"[!?',;. ]", paragraph.lower())
    counter_words = Counter(cleaned_paragraph)
    for word, _ in counter_words.most_common():
        if word not in banned and word != "":
            return word


print(most_common_word("Bob. hIt, baLl", ["bob", "hit"]))
