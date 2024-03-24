def find_peaks(mountain: list[int]) -> list[int]:
    return [i for i in range(1, len(mountain) - 1) if mountain[i - 1] < mountain[i] > mountain[i + 1]]


print(find_peaks([4, 2, 1]))
