def build_array(target: list[int], n: int) -> list[int]:
    result = []
    nums = []
    for num in range(1, n + 1):
        if nums == target:
            return result
        else:
            result.append("Push")
            if num not in target:
                result.append("Pop")
            else:
                nums.append(num)

    return result


print(build_array(target=[2, 3, 4], n=4))
print(["Push", "Pop", "Push", "Push", "Push"])
