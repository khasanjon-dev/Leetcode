def is_palindrome(s: str) -> bool:
    result = ''
    for letter in s:
        if 48 <= ord(letter) <= 57 or 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
            if 65 <= ord(letter) <= ord(letter) <= 90:
                result += chr(ord(letter) + 32)
            else:
                result += letter
    return result == result[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))
