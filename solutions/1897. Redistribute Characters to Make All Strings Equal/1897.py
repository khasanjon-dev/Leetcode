from itertools import chain


def make_equal(words: list[str]) -> bool:
    chain_len = len(list(chain(*words)))
    print(chain_len / len(words))
    return False if len(list(chain(*words))) % len(words) else True


print(make_equal(
    ["a", "bbbbbbbbbbbbbbbbbbbbbbbbbbb", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
     "s", "t", "u", "v", "w", "x", "y", "z"]))
