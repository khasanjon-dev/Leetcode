def keys_serializer(text: str):
    if text.isalnum():
        res = ''
        for letter in text:
            if letter.isalpha():
                res += letter
        return res
    return text


res = keys_serializer('1a2b3c4d5a6b7b8d9a10b11c12b13b14a15b16b17c18b19a20b21a22b23c24b25b26b27a28c29a30b')
print(len(res))
