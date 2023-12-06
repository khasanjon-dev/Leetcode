def merger_the_tools(string: str, k: int):
    for i in range(0, len(string), k):
        s = string[i: i + k]
        if len(set(s)) == len(s):
            print(s)
        else:
            unique_s = ''
            for j in s:
                if j not in unique_s:
                    unique_s += j
            print(unique_s)


string = 'AABCAAADA'
merger_the_tools(string, 3)
