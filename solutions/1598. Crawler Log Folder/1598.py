def min_operations(logs: list[str]) -> int:
    count = 0
    for log in logs:
        operation, _ = log.split("/")
        if operation == ".":
            continue
        elif operation == "..":
            if count > 0:
                count -= 1
        else:
            count += 1
    return count


print(min_operations(["d1/", "d2/", "./", "d3/", "../", "d31/"]))
