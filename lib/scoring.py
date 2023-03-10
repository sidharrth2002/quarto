from quarto.objects import Quarto


def score_board(state: Quarto):

    positions = {
        'couples': 0,
        'triplets': 0,
    }

    board = state.state_as_array()

    # Array for checking if a certain row already contains a triplet
    row_done = [False, False, False, False]

    # Check all the rows

    for i in range(state.BOARD_SIDE):
        if board[i, 0] != -1 and board[i, 1] != -1 and board[i, 2] != -1 and board[i, 3] == -1:
            piece_1 = state.get_piece_charachteristics(board[i, 0])
            piece_2 = state.get_piece_charachteristics(board[i, 1])
            piece_3 = state.get_piece_charachteristics(board[i, 2])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['triplets'] += 1
                row_done[i] = True
            if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['triplets'] += 1
                row_done[i] = True
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['triplets'] += 1
                row_done[i] = True
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['triplets'] += 1
                row_done[i] = True
        if board[i, 0] == -1 and board[i, 1] != -1 and board[i, 2] != -1 and board[i, 3] != -1:
            piece_1 = state.get_piece_charachteristics(board[i, 1])
            piece_2 = state.get_piece_charachteristics(board[i, 2])
            piece_3 = state.get_piece_charachteristics(board[i, 3])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['triplets'] += 1
                row_done[i] = True
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['triplets'] += 1
                row_done[i] = True
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['triplets'] += 1
                row_done[i] = True
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['triplets'] += 1
                row_done[i] = True
        if board[i, 0] != -1 and board[i, 1] != -1 and board[i, 2] == -1 and board[i, 3] != -1:
            piece_1 = state.get_piece_charachteristics(board[i, 0])
            piece_2 = state.get_piece_charachteristics(board[i, 1])
            piece_3 = state.get_piece_charachteristics(board[i, 3])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['triplets'] += 1
                row_done[i] = True
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['triplets'] += 1
                row_done[i] = True
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['triplets'] += 1
                row_done[i] = True
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['triplets'] += 1
                row_done[i] = True
        if board[i, 0] != -1 and board[i, 1] == -1 and board[i, 2] != -1 and board[i, 3] != -1:
            piece_1 = state.get_piece_charachteristics(board[i, 0])
            piece_2 = state.get_piece_charachteristics(board[i, 2])
            piece_3 = state.get_piece_charachteristics(board[i, 3])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['triplets'] += 1
                row_done[i] = True
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['triplets'] += 1
                row_done[i] = True
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['triplets'] += 1
                row_done[i] = True
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['triplets'] += 1
                row_done[i] = True
        # Before checking a row for couples, control the boolean flag
        if not row_done[i] and board[i, 0] != -1 and board[i, 1] != -1 and board[i, 2] == -1 and board[i, 3] == -1:
            piece_1 = state.get_piece_charachteristics(board[i, 0])
            piece_2 = state.get_piece_charachteristics(board[i, 1])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['couples'] += 1
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['couples'] += 1
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['couples'] += 1
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['couples'] += 1
        if not row_done[i] and board[i, 0] == -1 and board[i, 1] != -1 and board[i, 2] != -1 and board[i, 3] == -1:
            piece_1 = state.get_piece_charachteristics(board[i, 1])
            piece_2 = state.get_piece_charachteristics(board[i, 2])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['couples'] += 1
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['couples'] += 1
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['couples'] += 1
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['couples'] += 1
        if not row_done[i] and board[i, 0] == -1 and board[i, 1] == -1 and board[i, 2] != -1 and board[i, 3] != -1:
            piece_1 = state.get_piece_charachteristics(board[i, 2])
            piece_2 = state.get_piece_charachteristics(board[i, 3])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['couples'] += 1
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['couples'] += 1
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['couples'] += 1
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['couples'] += 1

    # Array for checking if a certain column already contains a triplet
    column_done = [False, False, False, False]

    # Check all the columns

    for i in range(state.BOARD_SIDE):
        if board[0, i] != -1 and board[1, i] != -1 and board[2, i] != -1 and board[3, i] == -1:
            piece_1 = state.get_piece_charachteristics(board[0, i])
            piece_2 = state.get_piece_charachteristics(board[1, i])
            piece_3 = state.get_piece_charachteristics(board[2, i])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['triplets'] += 1
                column_done[i] = True
            if piece_1.HIGH == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['triplets'] += 1
                column_done[i] = True
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['triplets'] += 1
                column_done[i] = True
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['triplets'] += 1
                column_done[i] = True
        if board[0, i] == -1 and board[1, i] != -1 and board[2, i] != -1 and board[3, i] != -1:
            piece_1 = state.get_piece_charachteristics(board[1, i])
            piece_2 = state.get_piece_charachteristics(board[2, i])
            piece_3 = state.get_piece_charachteristics(board[3, i])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['triplets'] += 1
                column_done[i] = True
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['triplets'] += 1
                column_done[i] = True
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['triplets'] += 1
                column_done[i] = True
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['triplets'] += 1
                column_done[i] = True
        if board[0, i] != -1 and board[1, i] == -1 and board[2, i] != -1 and board[3, i] != -1:
            piece_1 = state.get_piece_charachteristics(board[0, i])
            piece_2 = state.get_piece_charachteristics(board[2, i])
            piece_3 = state.get_piece_charachteristics(board[3, i])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['triplets'] += 1
                column_done[i] = True
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['triplets'] += 1
                column_done[i] = True
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['triplets'] += 1
                column_done[i] = True
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['triplets'] += 1
                column_done[i] = True
        if board[0, i] != -1 and board[1, i] != -1 and board[2, i] == -1 and board[3, i] != -1:
            piece_1 = state.get_piece_charachteristics(board[0, i])
            piece_2 = state.get_piece_charachteristics(board[1, i])
            piece_3 = state.get_piece_charachteristics(board[3, i])
            if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['triplets'] += 1
                column_done[i] = True
            if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['triplets'] += 1
                column_done[i] = True
            if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['triplets'] += 1
                column_done[i] = True
            if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['triplets'] += 1
                column_done[i] = True
        # Before checking a column for couples, control the boolean flag
        if not column_done[i] and board[0, i] != -1 and board[1, i] != -1 and board[2, i] == -1 and board[3, i] == -1:
            piece_1 = state.get_piece_charachteristics(board[0, i])
            piece_2 = state.get_piece_charachteristics(board[1, i])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['couples'] += 1
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['couples'] += 1
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['couples'] += 1
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['couples'] += 1
        if not column_done[i] and board[0, i] == -1 and board[1, i] != -1 and board[2, i] != -1 and board[3, i] == -1:
            piece_1 = state.get_piece_charachteristics(board[1, i])
            piece_2 = state.get_piece_charachteristics(board[2, i])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['couples'] += 1
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['couples'] += 1
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['couples'] += 1
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['couples'] += 1
        if not column_done[i] and board[0, i] == -1 and board[1, i] == -1 and board[2, i] != -1 and board[3, i] != -1:
            piece_1 = state.get_piece_charachteristics(board[2, i])
            piece_2 = state.get_piece_charachteristics(board[3, i])
            if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
                positions['couples'] += 1
            if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
                positions['couples'] += 1
            if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
                positions['couples'] += 1
            if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
                positions['couples'] += 1

    # Array for checking if a certain diagonal already contains a triplet
    diagonal_done = [False, False]

    # Check first diagonal

    if board[0, 0] != -1 and board[1, 1] != -1 and board[2, 2] != -1 and board[3, 3] == -1:
        piece_1 = state.get_piece_charachteristics(board[0, 0])
        piece_2 = state.get_piece_charachteristics(board[1, 1])
        piece_3 = state.get_piece_charachteristics(board[2, 2])
        if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
        if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
        if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
        if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
    if board[0, 0] == -1 and board[1, 1] != -1 and board[2, 2] != -1 and board[3, 3] != -1:
        piece_1 = state.get_piece_charachteristics(board[1, 1])
        piece_2 = state.get_piece_charachteristics(board[2, 2])
        piece_3 = state.get_piece_charachteristics(board[3, 3])
        if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
        if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
        if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
        if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
    if board[0, 0] != -1 and board[1, 1] == -1 and board[2, 2] != -1 and board[3, 3] != -1:
        piece_1 = state.get_piece_charachteristics(board[0, 0])
        piece_2 = state.get_piece_charachteristics(board[2, 2])
        piece_3 = state.get_piece_charachteristics(board[3, 3])
        if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
        if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
        if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
        if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
    if board[0, 0] != -1 and board[1, 1] != -1 and board[2, 2] == -1 and board[3, 3] != -1:
        piece_1 = state.get_piece_charachteristics(board[0, 0])
        piece_2 = state.get_piece_charachteristics(board[1, 1])
        piece_3 = state.get_piece_charachteristics(board[3, 3])
        if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
        if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
        if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
        if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['triplets'] += 1
            diagonal_done[0] = True
    # Before checking a diagonal for couples, control the boolean flag
    if not diagonal_done[0] and board[0, 0] != -1 and board[1, 1] != -1 and board[2, 2] == -1 and board[3, 3] == -1:
        piece_1 = state.get_piece_charachteristics(board[0, 0])
        piece_2 = state.get_piece_charachteristics(board[1, 1])
        if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['couples'] += 1
        if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['couples'] += 1
        if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['couples'] += 1
        if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['couples'] += 1
    if not diagonal_done[0] and board[0, 0] == -1 and board[1, 1] != -1 and board[2, 2] != -1 and board[3, 3] == -1:
        piece_1 = state.get_piece_charachteristics(board[1, 1])
        piece_2 = state.get_piece_charachteristics(board[2, 2])
        if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['couples'] += 1
        if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['couples'] += 1
        if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['couples'] += 1
        if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['couples'] += 1
    if not diagonal_done[0] and board[0, 0] == -1 and board[1, 1] == -1 and board[2, 2] != -1 and board[3, 3] != -1:
        piece_1 = state.get_piece_charachteristics(board[2, 2])
        piece_2 = state.get_piece_charachteristics(board[3, 3])
        if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['couples'] += 1
        if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['couples'] += 1
        if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['couples'] += 1
        if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['couples'] += 1

    # Check second diagonal

    if board[0, 3] != -1 and board[1, 2] != -1 and board[2, 1] != -1 and board[3, 0] == -1:
        piece_1 = state.get_piece_charachteristics(board[0, 3])
        piece_2 = state.get_piece_charachteristics(board[1, 2])
        piece_3 = state.get_piece_charachteristics(board[2, 1])
        if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
        if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
        if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
        if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
    if board[0, 3] == -1 and board[1, 2] != -1 and board[2, 1] != -1 and board[3, 0] != -1:
        piece_1 = state.get_piece_charachteristics(board[1, 2])
        piece_2 = state.get_piece_charachteristics(board[2, 1])
        piece_3 = state.get_piece_charachteristics(board[3, 0])
        if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
        if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
        if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
        if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
    if board[0, 3] != -1 and board[1, 2] != -1 and board[2, 1] == -1 and board[3, 0] != -1:
        piece_1 = state.get_piece_charachteristics(board[0, 3])
        piece_2 = state.get_piece_charachteristics(board[1, 2])
        piece_3 = state.get_piece_charachteristics(board[3, 0])
        if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
        if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
        if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
        if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
    if board[0, 3] != -1 and board[1, 2] == -1 and board[2, 1] != -1 and board[3, 0] != -1:
        piece_1 = state.get_piece_charachteristics(board[0, 3])
        piece_2 = state.get_piece_charachteristics(board[2, 1])
        piece_3 = state.get_piece_charachteristics(board[3, 0])
        if piece_1.HIGH == piece_2.HIGH and piece_3.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
        if piece_1.COLOURED == piece_2.COLOURED and piece_3.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
        if piece_1.SQUARE == piece_2.SQUARE and piece_3.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
        if piece_1.SOLID == piece_2.SOLID and piece_3.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['triplets'] += 1
            diagonal_done[1] = True
    # Before checking a diagonal for couples, control the boolean flag
    if not diagonal_done[1] and board[0, 3] != -1 and board[1, 2] != -1 and board[2, 1] == -1 and board[3, 0] == -1:
        piece_1 = state.get_piece_charachteristics(board[0, 3])
        piece_2 = state.get_piece_charachteristics(board[1, 2])
        if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['couples'] += 1
        if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['couples'] += 1
        if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['couples'] += 1
        if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['couples'] += 1
    if not diagonal_done[1] and board[0, 3] == -1 and board[1, 2] != -1 and board[2, 1] != -1 and board[3, 0] == -1:
        piece_1 = state.get_piece_charachteristics(board[1, 2])
        piece_2 = state.get_piece_charachteristics(board[2, 1])
        if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['couples'] += 1
        if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['couples'] += 1
        if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['couples'] += 1
        if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['couples'] += 1
    if not diagonal_done[1] and board[0, 0] == -1 and board[1, 2] == -1 and board[2, 1] != -1 and board[3, 0] != -1:
        piece_1 = state.get_piece_charachteristics(board[2, 1])
        piece_2 = state.get_piece_charachteristics(board[3, 0])
        if piece_1.HIGH == piece_2.HIGH and piece_1.HIGH == True:
            positions['couples'] += 1
        if piece_1.COLOURED == piece_2.COLOURED and piece_1.COLOURED == True:
            positions['couples'] += 1
        if piece_1.SQUARE == piece_2.SQUARE and piece_1.SQUARE == True:
            positions['couples'] += 1
        if piece_1.SOLID == piece_2.SOLID and piece_1.SOLID == True:
            positions['couples'] += 1

    return positions['couples']+2*positions['triplets']
