def min_cost_to_move_chips(position: list[int]) -> int:
    even_count = sum(1 for pos in position if pos % 2 == 0)
    odd_count = len(position) - even_count
    return min(even_count, odd_count)


print(min_cost_to_move_chips([1, 10000000]))
