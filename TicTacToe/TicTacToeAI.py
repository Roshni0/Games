def minimax(board):#Returns the optimal action for the current player on the board.
    currentactions = actions(board)
    if player(board) == X:
        vT = -math.inf
        move = set()
        for action in currentactions:
            v, count = maxvalue(result(board,action), 0)
            if v > vT:
                vT = v
                move = action
    else:
        vT = math.inf
        move = set()
        for action in currentactions:
            v, count = minvalue(result(board,action), 0)
            if v < vT:
                vT = v
                move = action
    print(count)
    return move
def maxvalue(board, count):#Calculates the max value of a given board recursively together with minvalue
    if terminal(board): return utility(board), count+1
    v = -math.inf
    posactions = actions(board)
    for action in posactions:
        vret, count = minvalue(result(board, action), count)
        v = max(v, vret)
    return v, count+1
def minvalue(board, count):#Calculates the min value of a given board recursively together with maxvalue
    if terminal(board): return utility(board), count+1
    v = math.inf
    posactions = actions(board)
    for action in posactions:
        vret, count = maxvalue(result(board, action), count)
        v = min(v, vret)
    return v, count+1 
