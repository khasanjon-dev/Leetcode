def reverse_words(s: str) -> str:
    result = ''
    strings = s.split()  # =>  ['God', 'Ding']
    for word in strings:  # word => 'God'
        # result += word[::-1] + ' '  # 'doG' + ' '
        res = ''
        for i in range(1, len(word) + 1):
            res += word[-i]
        result += res + ' '
    return result.strip()


# Input:
s = "God Ding"
# Output:
"doG gniD"
print(reverse_words(s))
