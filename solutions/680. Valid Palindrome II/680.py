def valid_palindrome(s: str) -> bool:
    def is_palindrome_range(s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(s, left + 1, right) or is_palindrome_range(s, left, right - 1)

        left += 1
        right -= 1
    return True


print(valid_palindrome('abca'))
