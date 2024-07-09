def average_waiting_time(customers: list[list[int]]) -> float:
    total_time = 0
    waiting_times = []
    for customer in customers:
        if customer[0] < total_time:
            total_time += customer[1]
            waiting_times.append(total_time - customer[0])
        else:
            total_time = customer[1] + customer[0]
            waiting_times.append(customer[1])
    return round(sum(waiting_times) / len(customers), 5)


print(average_waiting_time([[1, 2], [2, 5], [4, 3]]))
