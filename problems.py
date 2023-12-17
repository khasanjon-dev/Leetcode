def fun(text: str, first: str, second: str) -> list[str]:
    result = []
    text = text.split()
    for i in range(len(text)):
        if len(text) - 1 != i and len(text) - 2 != i:
            if text[i] == first and text[i + 1] == second:
                result.append(text[i + 2])
    return result


print(
    fun("ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv ypkk",
        "lnlqhmaohv",
        "ypkk"))
