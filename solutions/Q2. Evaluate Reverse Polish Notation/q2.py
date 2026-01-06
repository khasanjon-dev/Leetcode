def eval_rpn(tokens: list[str]) -> int:
    result = []
    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            num2 = result.pop()
            num1 = result.pop()
            if token == "+":
                result.append(num1 + num2)
            elif token == "-":
                result.append(num1 - num2)
            elif token == "*":
                result.append(num1 * num2)
            elif token == "/":
                result.append(int(num1 / num2))
        else:
            result.append(int(token))
    return result[0]


print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
