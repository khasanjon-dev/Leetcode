def make_fancy_string(s: str) -> str:
    ans = ""
    prev = ""
    count = 1
    i = 0
    while i < len(s):
        if prev == s[i]:
            count += 1
            if count <= 2:
                ans += prev
            else:
                count += 1
        else:
            prev = s[i]
            count = 1
            ans += s[i]
        i += 1

    return ans


print(make_fancy_string("leeetcode"))
