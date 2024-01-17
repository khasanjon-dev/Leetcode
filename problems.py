def last_visited_integers(words: list[str]) -> list[int]:
    result = []
    nums = []
    prev_count = 0
    for word in words:
        if word == 'prev':
            if prev_count >= len(nums):
                result.append(-1)
            else:
                result.append(nums[-1 - prev_count])
            prev_count += 1
        else:
            nums.append(int(word))
            result.append(int(word))
            prev_count = 0

    return result


words = ["1", "prev", "2", "prev", "prev", "3", "4", "prev", "5"]
print(last_visited_integers(words))
