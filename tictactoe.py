"""
Tic Tac Toe Player
"""
import copy
import math
import random

class Set:
    def __init__(self, listing):
        assert isinstance(listing, list),\
            "Arguiment must be a list"
        self.element = []
        self.count = 0
        for value in listing:
            self.add(value)

    def add(self, value):
        if value not in self.element:
            self.element.append(value)
            self.count += 1

    def __getitem__(self, ndx):
        return self.element[ndx]

    def __len__(self):
        return self.count

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    p1 = 0
    p2 = 0
    for row in board:
        for i in range(3):
            if row[i] == X:
                p1 += 1
            elif row[i] == O:
                p2 += 1
    if p2 < p1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = []
    i = 0
    j = 0
    while i < 3:
        if board[i][j] is EMPTY:
            available.append((i, j))
        if j < 2:
            j += 1
        else:
            j = 0
            i += 1
    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new = copy.deepcopy(board)
    res = player(new)
    row, col = action
    new[row][col] = res
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        hor = Set(board[i])
        if len(hor) == 1 and hor[0] is not EMPTY:
            if hor[0] == X:
                return X
            return O
        vert = Set([board[0][i], board[1][i], board[2][i]])
        if len(vert) == 1 and vert[0] is not EMPTY:
            if vert[0] == X:
                return X
            return O
    diag1 = Set([board[0][0], board[1][1], board[2][2]])
    if len(diag1) == 1 and diag1[0] is not EMPTY:
        if diag1[0] == X:
            return X
        return O
    diag2 = Set([board[2][0], board[1][1], board[0][2]])
    if len(diag2) == 1 and diag2[0] is not EMPTY:
        if diag2[0] == X:
            return X
        return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if None in row:
            return False
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1

    return 0

def minimax(board):
    """
    Return the Optimal action for the AI
    """
    if board == initial_state():
        return random.choice(actions(board))
    if player(board) == X:
        moves = actions(board)
        best_move = None
        best_score = float('-inf')
        for move in moves:
            new_board = result(board, move)
            score = min_play(new_board)
            if score > best_score:
                best_move = move
                best_score = score
        return best_move
    else:
        moves = actions(board)
        best_move = None
        best_score = float('inf')
        for move in moves:
            new_board = result(board, move)
            score = max_play(new_board)
            if score < best_score:
                best_move = move
                best_score = score
        return best_move
        


def min_play(board):
    if terminal(board):
        return utility(board)
    moves = actions(board)
    best_score = 10
    for move in moves:
        new_board = result(board, move)
        score = max_play(new_board)
        if score < best_score:
            best_score = score
    return best_score

def max_play(board):
    if terminal(board):
        return utility(board)
    moves = actions(board)
    best_score = -10
    for move in moves:
        new_board = result(board, move)
        score = min_play(new_board)
        if score > best_score:
            best_score = score
    return best_score



