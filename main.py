def fun(moves: str) -> bool:
    return moves.count('D') == moves.count('U') and moves.count('L') == moves.count('R')


print(fun("LDLLULUDLL"))
