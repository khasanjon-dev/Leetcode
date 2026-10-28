def closing_brackets(formula: str) -> str | None:
    brackets = []

    for bracket in formula:

        if bracket in "(){}[]":
            brackets.append(bracket)

    print(brackets)


print(closing_brackets("AVG([price * {qty"))
print(closing_brackets("SUM([revenue]) / (COUNT({orders}) + 1)"))
