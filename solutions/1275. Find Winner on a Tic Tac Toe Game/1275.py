def tictactoe(moves: list[list[int]]) -> str:
    responses = ('A', 'B', 'Pending', 'Draw')
    len_moves = len(moves)

    # draw
    if len_moves == 9:
        return responses[3]
    try:
        # a
        a_y = moves[0][0]
        j = 0
        for i in range(0, len_moves, 2):
            j += 1
            if moves[i][0] != a_y:
                break
        else:
            if j == 3:
                return responses[0]
        j = 0
        a_x = moves[0][1]
        for i in range(0, len_moves, 2):
            j += 1
            if moves[i][1] != a_x:
                break
        else:
            if j == 3:
                return responses[0]
        j = 0
        for i in range(0, len_moves, 2):
            j += 1
            if moves[i][0] != moves[i][1]:
                break
        else:
            if j == 3:
                return responses[0]
        for i in range(0, len_moves, 2):
            if moves[i][0] == moves[i][1]:
                if i == 0:
                    if moves[i + 2][0] == moves[i + 4][1] == 0 and moves[i + 2][1] == moves[i + 4][0] == 2:
                        return responses[0]
                elif i == 2:
                    if moves[i - 2][0] == moves[i + 2] == 0 and moves[i - 2][1] == moves[i + 2][0] == 2:
                        return responses[0]
                elif i == 4:
                    if moves[i - 4][0] == moves[i - 2] == 0 and moves[i - 4][1] == moves[i - 2][0] == 2:
                        return responses[0]
        # b
        j = 0
        b_y = moves[1][0]
        for i in range(1, len_moves, 2):
            j += 1
            if moves[i][0] != b_y:
                break
        else:
            if j == 3:
                return responses[1]
        b_x = moves[1][1]
        j = 0
        for i in range(1, len_moves, 2):
            j += 1
            if moves[i][1] != b_x:
                break
        else:
            if j == 3:
                return responses[1]
        j = 0
        for i in range(1, len_moves, 2):
            j += 1
            if moves[i][0] != moves[i][1]:
                break
        else:
            if j == 3:
                return responses[1]
        for i in range(1, len_moves, 2):
            if moves[i][0] == moves[i][1]:
                if i == 1:
                    if moves[i + 2][0] == moves[i + 4][1] == 0 and moves[i + 2][1] == moves[i + 4][0] == 2:
                        return responses[1]
                elif i == 3:
                    if moves[i - 2][0] == moves[i + 2][1] == 0 and moves[i - 2][1] == moves[i + 2][0] == 2:
                        return responses[1]
                elif i == 5:
                    if moves[i - 4][0] == moves[i - 2][1] == 0 and moves[i - 4][1] == moves[i - 2][0] == 2:
                        return responses[1]
    except:
        pass

    # pending
    return responses[2]


print(tictactoe([[1, 2], [2, 1], [1, 0], [0, 0], [0, 1], [2, 0], [1, 1]]))
