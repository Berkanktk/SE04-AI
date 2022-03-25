# Constants
win = {
    0: [0, 4, 8],  # Diagonal '\'
    1: [2, 4, 6],  # Diagonal '/'
    2: [0, 1, 2],  # Top (Horizontal)
    3: [3, 4, 5],  # Center (Horizontal)
    4: [6, 7, 8],  # Bottom (Horizontal)
    5: [0, 3, 6],  # First column (Vertical)
    6: [1, 4, 7],  # Center (Vertical)
    7: [2, 5, 8]  # Last column (Vertical)
}


# Functions and general logic
def minmax_decision(state):
    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        # print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    if state.count('X') >= 3 and check_terminal(state, 'X'):
        return True
    elif state.count('O') >= 3 and check_terminal(state, 'O'):
        return True
    elif state.count('X') + state.count('O') >= len(state):
        return True

    return False


def check_terminal(state, player):
    checked_player = []

    for i in range(0, 9):
        if state[i] == player:
            checked_player.append(i)

    for i in range(0, len(win)):
        if len([value for value in win[i] if value in checked_player]) == 3:
            return True
    return False


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    if check_terminal(state, 'X'):
        return 1
    elif check_terminal(state, 'O'):
        return -1
    else:
        return 0


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    moves = []

    for i in range(0, 9):
        if state[i] != 'X' and state[i] != 'O':
            total = []
            for j in range(0, 9):
                if j == i and state.count('X') == state.count('O'):
                    total.append('X')
                elif j == i and state.count('X') > state.count('O'):
                    total.append('O')
                else:
                    total.append(state[j])

            moves.append((i, total.copy()))

    return moves


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    print("Welcome to the game of Tic-Tac-Toe! Game starts in 3 seconds...")
    main()
