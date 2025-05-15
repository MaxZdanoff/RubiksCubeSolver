
import numpy as np
turn_history = []


def history(moves):
    if type(moves) is not str:
        moves = str(moves).split()
    turn_history.append(moves)

    return turn_history


def turns(self, side):

    if side == 'R':
        self.rightSide = np.rot90(self.rightSide, 3)
        top_col = self.topSide[:, 2].copy()
        front_col = self.frontSide[:, 2].copy()
        back_col = self.backSide[:, 0].copy()
        bottom_col = self.bottomSide[:, 2].copy()

        self.frontSide[:, 2] = bottom_col
        self.topSide[:, 2] = front_col
        self.bottomSide[:, 2] = back_col[::-1]
        self.backSide[:, 0] = top_col[::-1]
    if side == '-R':
        self.rightSide = np.rot90(self.rightSide)
        top_col = self.topSide[:, 2].copy()
        front_col = self.frontSide[:, 2].copy()
        back_col = self.backSide[:, 0].copy()
        bottom_col = self.bottomSide[:, 2].copy()

        self.frontSide[:, 2] = top_col
        self.bottomSide[:, 2] = front_col
        self.backSide[:, 0] = bottom_col[::-1]
        self.topSide[:, 2] = back_col[::-1]
    if side == 'R2':
        self.rightSide = np.rot90(self.rightSide, 2)
        top_col = self.topSide[:, 2].copy()
        front_col = self.frontSide[:, 2].copy()
        back_col = self.backSide[:, 0].copy()
        bottom_col = self.bottomSide[:, 2].copy()

        self.frontSide[:, 2] = back_col[::-1]
        self.bottomSide[:, 2] = top_col
        self.backSide[:, 0] = front_col[::-1]
        self.topSide[:, 2] = bottom_col
    if side == 'L':
        self.leftSide = np.rot90(self.leftSide, 3)
        top_col = self.topSide[:, 0].copy()
        front_col = self.frontSide[:, 0].copy()
        back_col = self.backSide[:, 2].copy()
        bottom_col = self.bottomSide[:, 0].copy()

        self.frontSide[:, 0] = top_col
        self.bottomSide[:, 0] = front_col
        self.backSide[:, 2] = bottom_col[::-1]
        self.topSide[:, 0] = back_col[::-1]
    if side == '-L':
        self.leftSide = np.rot90(self.leftSide)
        top_col = self.topSide[:, 0].copy()
        front_col = self.frontSide[:, 0].copy()
        back_col = self.backSide[:, 2].copy()
        bottom_col = self.bottomSide[:, 0].copy()

        self.frontSide[:, 0] = bottom_col
        self.topSide[:, 0] = front_col
        self.backSide[:, 2] = top_col[::-1]
        self.bottomSide[:, 0] = back_col[::-1]
    if side == 'L2':
        self.leftSide = np.rot90(self.leftSide, 2)
        top_col = self.topSide[:, 0].copy()
        front_col = self.frontSide[:, 0].copy()
        back_col = self.backSide[:, 2].copy()
        bottom_col = self.bottomSide[:, 0].copy()


        self.frontSide[:, 0] = back_col[::-1]
        self.topSide[:, 0] = bottom_col
        self.backSide[:, 2] = front_col[::-1]
        self.bottomSide[:, 0] = top_col
    if side == 'U':
        self.topSide = np.rot90(self.topSide, 3)
        front_row = self.frontSide[0].copy()
        left_row = self.leftSide[0].copy()
        back_row = self.backSide[0].copy()
        right_row = self.rightSide[0].copy()

        self.leftSide[0] = front_row
        self.backSide[0] = left_row
        self.rightSide[0] = back_row
        self.frontSide[0] = right_row
    if side == '-U':
        self.topSide = np.rot90(self.topSide)
        front_row = self.frontSide[0].copy()
        left_row = self.leftSide[0].copy()
        back_row = self.backSide[0].copy()
        right_row = self.rightSide[0].copy()

        self.leftSide[0] = back_row
        self.frontSide[0] = left_row
        self.rightSide[0] = front_row
        self.backSide[0] = right_row
    if side == 'U2':
        self.topSide = np.rot90(self.topSide, 2)
        front_row = self.frontSide[0].copy()
        left_row = self.leftSide[0].copy()
        back_row = self.backSide[0].copy()
        right_row = self.rightSide[0].copy()

        self.leftSide[0] = right_row
        self.frontSide[0] = back_row
        self.rightSide[0] = left_row
        self.backSide[0] = front_row
    if side == 'D':
        self.bottomSide = np.rot90(self.bottomSide, 3)
        front_row = self.frontSide[2].copy()
        left_row = self.leftSide[2].copy()
        back_row = self.backSide[2].copy()
        right_row = self.rightSide[2].copy()

        self.leftSide[2] = back_row
        self.frontSide[2] = left_row
        self.rightSide[2] = front_row
        self.backSide[2] = right_row
    if side == '-D':
        self.bottomSide = np.rot90(self.bottomSide)
        front_row = self.frontSide[2].copy()
        left_row = self.leftSide[2].copy()
        back_row = self.backSide[2].copy()
        right_row = self.rightSide[2].copy()

        self.leftSide[2] = front_row
        self.backSide[2] = left_row
        self.rightSide[2] = back_row
        self.frontSide[2] = right_row
    if side == 'D2':
        self.bottomSide = np.rot90(self.bottomSide, 2)
        front_row = self.frontSide[2].copy()
        left_row = self.leftSide[2].copy()
        back_row = self.backSide[2].copy()
        right_row = self.rightSide[2].copy()

        self.leftSide[2] = right_row
        self.frontSide[2] = back_row
        self.rightSide[2] = left_row
        self.backSide[2] = front_row
    if side == 'F':
        self.frontSide = np.rot90(self.frontSide, 3)
        top_row = self.topSide[2].copy()
        right_col = self.rightSide[:, 0].copy()
        bottom_row = self.bottomSide[0].copy()
        left_col = self.leftSide[:, 2].copy()

        self.rightSide[:, 0] = top_row
        self.bottomSide[0] = right_col[::-1]
        self.leftSide[:, 2] = bottom_row
        self.topSide[2] = left_col[::-1]
    if side == '-F':
        self.frontSide = np.rot90(self.frontSide)
        top_row = self.topSide[2].copy()
        right_col = self.rightSide[:, 0].copy()
        bottom_row = self.bottomSide[0].copy()
        left_col = self.leftSide[:, 2].copy()

        self.rightSide[:, 0] = bottom_row[::-1]
        self.bottomSide[0] = left_col
        self.leftSide[:, 2] = top_row[::-1]
        self.topSide[2] = right_col
    if side == 'F2':
        self.frontSide = np.rot90(self.frontSide, 2)
        top_row = self.topSide[2].copy()
        right_col = self.rightSide[:, 0].copy()
        bottom_row = self.bottomSide[0].copy()
        left_col = self.leftSide[:, 2].copy()


        self.rightSide[:, 0] = left_col[::-1]
        self.bottomSide[0] = top_row[::-1]
        self.leftSide[:, 2] = right_col[::-1]
        self.topSide[2] = bottom_row[::-1]
    if side == 'B':
        self.backSide = np.rot90(self.backSide, 3)
        top_row = self.topSide[0].copy()
        right_col = self.rightSide[:, 2].copy()
        bottom_row = self.bottomSide[2].copy()
        left_col = self.leftSide[:, 0].copy()

        self.rightSide[:, 2] = bottom_row[::-1]
        self.topSide[0] = right_col
        self.leftSide[:, 0] = top_row[::-1]
        self.bottomSide[2] = left_col
    if side == '-B':
        self.backSide = np.rot90(self.backSide)
        top_row = self.topSide[0].copy()
        right_col = self.rightSide[:, 2].copy()
        bottom_row = self.bottomSide[2].copy()
        left_col = self.leftSide[:, 0].copy()

        self.rightSide[:, 2] = top_row
        self.bottomSide[2] = right_col[::-1]
        self.leftSide[:, 0] = bottom_row
        self.topSide[0] = left_col[::-1]
    if side == 'B2':
        self.backSide = np.rot90(self.backSide, 2)
        top_row = self.topSide[0].copy()
        right_col = self.rightSide[:, 2].copy()
        bottom_row = self.bottomSide[2].copy()
        left_col = self.leftSide[:, 0].copy()

        self.topSide[0] = bottom_row[::-1]
        self.rightSide[:, 2] = left_col [::-1]
        self.bottomSide[2] = top_row[::-1]
        self.leftSide[:, 0] = right_col[::-1]
    if side == 'M':
        top_col = self.topSide[:, 1].copy()
        back_col = self.backSide[:, 1].copy()
        bottom_col = self.bottomSide[:, 1].copy()
        front_col = self.frontSide[:, 1].copy()

        self.topSide[:, 1] = back_col[::-1]
        self.frontSide[:, 1] = top_col
        self.bottomSide[:, 1] = front_col
        self.backSide[:, 1] = bottom_col[::-1]
    if side == '-M':
        top_col = self.topSide[:, 1].copy()
        back_col = self.backSide[:, 1].copy()
        bottom_col = self.bottomSide[:, 1].copy()
        front_col = self.frontSide[:, 1].copy()

        self.topSide[:, 1] = front_col
        self.frontSide[:, 1] = bottom_col
        self.bottomSide[:, 1] = back_col[::-1]
        self.backSide[:, 1] = top_col[::-1]
    if side == 'M2':
        top_col = self.topSide[:, 1].copy()
        back_col = self.backSide[:, 1].copy()
        bottom_col = self.bottomSide[:, 1].copy()
        front_col = self.frontSide[:, 1].copy()

        self.topSide[:, 1] = bottom_col
        self.frontSide[:, 1] = back_col[::-1]
        self.bottomSide[:, 1] = top_col
        self.backSide[:, 1] = front_col[::-1]


def rotate_moves(moves, side):
    rotated_moves = []

    if side == 'left':
        rotate_left = {
            'R': 'F', 'R2': 'F2', '-R': '-F', 'L': 'B', 'L2': 'B2', '-L': '-B',
            'F': 'L', 'F2': 'L2', '-F': '-L', 'B': 'R', 'B2': 'R2', '-B': '-R'
        }

        for i in range(len(moves)):
            if moves[i] in rotate_left.keys():
                rotated_moves.append(rotate_left[moves[i]])
            else:
                rotated_moves.append(moves[i])


    if side == 'back':
        rotate_back = {
            'R': 'L', 'R2': 'L2', '-R': '-L', 'L': 'R', 'L2': 'R2', '-L': '-R',
            'F': 'B', 'F2': 'B2', '-F': '-B', 'B': 'F', 'B2': 'F2', '-B': '-F'
        }

        for i in range(len(moves)):
            if moves[i] in rotate_back.keys():
                rotated_moves.append(rotate_back[moves[i]])
            else:
                rotated_moves.append(moves[i])


    if side == 'right':
        rotate_right = {
            'R': 'B', 'R2': 'B2', '-R': '-B', 'L': 'F', 'L2': 'F2', '-L': '-F',
            'F': 'R', 'F2': 'R2', '-F': '-R', 'B': 'L', 'B2': 'L2', '-B': '-L'
        }

        for i in range(len(moves)):
            if moves[i] in rotate_right.keys():
                rotated_moves.append(rotate_right[moves[i]])
            else:
                rotated_moves.append(moves[i])


    return rotated_moves


def create_scramble(length):
    import random
    move_set = list('R R2 -R U U2 -U L L2 -L D D2 -D F F2 -F B B2 -B'.split())
    i = 0
    scramble = []
    while i < length:
        random_move = move_set[random.randint(0, 17)]
        if i > 0:
            while set(random_move.strip()) - {'-', '2'} == set(scramble[i-1].strip()) - {'-', '2'}:
                random_move = move_set[random.randint(0, 17)]

        scramble.append(random_move)
        i += 1
    print(scramble)
    return scramble


def simplify_moves(moves):
    def move_to_tuple(move):
        if move.endswith('2'):
            return (move[0], 2)
        elif move.startswith('-'):
            return (move[1], -1)
        else:
            return (move[0], 1)

    def tuple_to_move(face, count):
        count %= 4
        if count == 0:
            return None
        elif count == 1:
            return face
        elif count == 2:
            return face + '2'
        elif count == 3:
            return '-' + face

    stack = []

    for move in moves:
        face, count = move_to_tuple(move)
        if stack and stack[-1][0] == face:
            prev_face, prev_count = stack.pop()
            new_count = prev_count + count
            simplified = tuple_to_move(face, new_count)
            if simplified:
                stack.append(move_to_tuple(simplified))
        else:
            stack.append((face, count))

    return [tuple_to_move(face, count) for face, count in stack if tuple_to_move(face, count)]


def undo_moves(moves):
    copy = moves
    copy.reverse()
    reversed_moves = []
    for move in copy:
        face = ''.join(set(move) - {'-', '2'})

        if move == face:
            reversed_moves.append('-' + move)
        elif move == '-' + face:
            reversed_moves.append(face)
        elif move == face + '2':
            reversed_moves.append(move)
        else:
            raise ValueError("Fix this")

    return reversed_moves




