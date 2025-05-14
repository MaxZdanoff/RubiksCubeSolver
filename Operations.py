

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
    i = 0
    if side == 'right':
        while i < len(moves):
            if moves[i] == 'R':
                rotated_moves.append('B')
            elif moves[i] == 'R2':
                rotated_moves.append('B2')
            elif moves[i] == '-R':
                rotated_moves.append('-B')
            elif moves[i] == 'L':
                rotated_moves.append('F')
            elif moves[i] == 'L2':
                rotated_moves.append('F2')
            elif moves[i] == '-L':
                rotated_moves.append('-F')
            elif moves[i] == 'F':
                rotated_moves.append('R')
            elif moves[i] == 'F2':
                rotated_moves.append('R2')
            elif moves[i] == '-F':
                rotated_moves.append('-R')
            else:
                rotated_moves.append(moves[i])
            i += 1
    elif side == 'left':
        while i < len(moves):
            if moves[i] == 'R':
                rotated_moves.append('F')
            elif moves[i] == 'R2':
                rotated_moves.append('F2')
            elif moves[i] == '-R':
                rotated_moves.append('-F')
            elif moves[i] == 'L':
                rotated_moves.append('B')
            elif moves[i] == 'L2':
                rotated_moves.append('B2')
            elif moves[i] == '-L':
                rotated_moves.append('-B')
            elif moves[i] == 'F':
                rotated_moves.append('L')
            elif moves[i] == 'F2':
                rotated_moves.append('L2')
            elif moves[i] == '-F':
                rotated_moves.append('-L')
            else:
                rotated_moves.append(moves[i])
            i += 1
    elif side == 'back':
        while i < len(moves):
            if moves[i] == 'R':
                rotated_moves.append('L')
            elif moves[i] == 'R2':
                rotated_moves.append('L2')
            elif moves[i] == '-R':
                rotated_moves.append('-L')
            elif moves[i] == 'L':
                rotated_moves.append('R')
            elif moves[i] == 'L2':
                rotated_moves.append('R2')
            elif moves[i] == '-L':
                rotated_moves.append('-R')
            elif moves[i] == 'F':
                rotated_moves.append('B')
            elif moves[i] == 'F2':
                rotated_moves.append('B2')
            elif moves[i] == '-F':
                rotated_moves.append('-B')
            else:
                rotated_moves.append(moves[i])
            i += 1

    return rotated_moves