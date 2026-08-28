def who_won(game_board:list):
    ply1_counter = 0
    ply2_counter = 0

    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                 ply1_counter += 1
            elif game_board[i][j] == 2:
                ply2_counter += 1
    if ply1_counter > ply2_counter:
        return 1
    elif ply1_counter == ply2_counter:
        return 0
    else:
        return 2
if __name__ == "__main__":
    game_board = [
    [1, 2, 0],
    [0, 1, 2],
    [2, 0, 0],
    [2, 2, 0],
    [2, 1, 0],
    [2, 0, 2],
    [2, 1, 1],
    ]
    print(who_won(game_board))