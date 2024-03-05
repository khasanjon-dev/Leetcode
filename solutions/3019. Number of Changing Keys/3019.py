def count_key_changes(s: str) -> int:
    count = 0
    prefix = s[0]
    for j in range(1, len(s)):
        if prefix.lower() == s[j].lower():
            pass
        else:
            prefix = s[j]
            count += 1
    return count


print(count_key_changes('AaAaAaaA'))
