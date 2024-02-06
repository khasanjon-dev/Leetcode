def group_anagrams(strs: list[str]) -> list[list[str]]:
    result = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in result:
            result[sorted_word] = []
        result[sorted_word].append(word)
    return sorted(result.values(), key=lambda x: len(x))


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
