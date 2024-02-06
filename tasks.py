def keys_serializer(text: str) -> dict:
    keys = {}
    if text.isalnum():
        res = ''
        for letter in text:
            if letter.isalpha():
                res += letter
        text = res
    for i, value in enumerate(text, 1):
        keys.update({i: value})

    return keys


print(keys_serializer('1a2b3s4d5a'))
