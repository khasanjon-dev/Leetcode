def has_all_codes(s: str, k: int) -> bool:
    if len(s) < k:
        return False

    seen = set()

    for i in range(len(s) - k + 1):
        seen.add(s[i : i + k])

    return len(seen) == 2**k


print(has_all_codes("0110", 2))
