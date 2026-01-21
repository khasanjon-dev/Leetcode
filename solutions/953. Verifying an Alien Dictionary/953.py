def is_alien_sorted(words: list[str], order: str) -> bool:
    dict_order = {s: i for i, s in enumerate(order)}
    return sorted(words, key=lambda word: [dict_order[s] for s in word]) == words



print(is_alien_sorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
