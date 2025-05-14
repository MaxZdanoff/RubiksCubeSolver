
import Cube_array
from Operations import *
Cube_array.cube.corners_info()


class EdgesSolve:
    def __init__(self):
        self.topSide = Cube_array.return_solved_layer()[0]
        self.leftSide = Cube_array.return_solved_layer()[1]
        self.frontSide = Cube_array.return_solved_layer()[2]
        self.rightSide = Cube_array.return_solved_layer()[3]
        self.backSide = Cube_array.return_solved_layer()[4]
        self.bottomSide = Cube_array.return_solved_layer()[5]

        self.move_list = []


    @property
    def A_edge(self):
        return list(map(str, [self.backSide[0][1], self.topSide[0][1]]))
    @property
    def B_edge(self):
        return list(map(str, [self.rightSide[0][1], self.topSide[1][2]]))
    @property
    def C_edge(self):
        return list(map(str, [self.frontSide[0][1], self.topSide[2][1]]))
    @property
    def D_edge(self):
        return list(map(str, [self.leftSide[0][1], self.topSide[1][0]]))


    @property
    def a_slot(self):
        return list(map(str, [self.backSide[1][2], self.leftSide[1][0]]))
    @property
    def b_slot(self):
        return list(map(str, [self.backSide[1][0], self.rightSide[1][2]]))
    @property
    def c_slot(self):
        return list(map(str, [self.frontSide[1][2], self.rightSide[1][0]]))
    @property
    def d_slot(self):
        return list(map(str, [self.frontSide[1][0], self.leftSide[1][2]]))


    def turn(self, side):
        history(side)
        return turns(self, side)


    def is_solved(self):
        dictionary = {
            1: [['b', 'o'], self.a_slot],
            2: [['b', 'r'], self.b_slot],
            3: [['g', 'r'], self.c_slot],
            4: [['g', 'o'], self.d_slot]
        }

        for key in dictionary.keys():
            if dictionary[key][0] != dictionary[key][1]:
                return False
        return True


    def complication_slot_search(self)  :
        dictionary = {
            1: [['b', 'o'], self.a_slot],
            2: [['b', 'r'], self.b_slot],
            3: [['g', 'r'], self.c_slot],
            4: [['g', 'o'], self.d_slot]
        }

        for key in dictionary.keys():

            if dictionary[key][0] != dictionary[key][1]:
                return key
        raise ValueError("No complication found")


    def fix_complication(self):
        alg = ['R', '-U', '-R', '-U', '-F', 'U', 'F']
        if self.complication_slot_search() == 3:
            for move in alg:
                self.turn(move)
        else:
            dictionary = {1: 'back', 2: 'right', 4: 'left'}
            alg = rotate_moves(alg, dictionary[self.complication_slot_search()])
            for move in alg:
                self.turn(move)


    def insert_piece(self, direction, side=None):
        if direction == 'right':
            alg = ['U', 'R', '-U', '-R', '-U', '-F', 'U', 'F']
        elif direction == 'left':
            alg = ['-U', '-L', 'U', 'L', 'U', 'F', '-U', '-F']
        else:
            raise ValueError("Direction parameter must be 'left' or 'right'")

        if side == None:
            for move in alg:
                self.turn(move)
        else:
            alg = rotate_moves(alg, side)
            for move in alg:
                self.turn(move)


    def left_or_right(self, edge_piece):
        if 'w' in edge_piece:
            raise ValueError(f"{edge_piece} does not belong in middle layer")

        right_edges = [['g', 'r'], ['o', 'g'], ['r', 'b'], ['b', 'o']]

        for i in range(len(right_edges)-1):
            if edge_piece == right_edges[i]:
                return 'right'

        return 'left'


    def top_edge_solve(self):
        if self.is_solved():
            return
        i = 0
        while 'w' in self.C_edge:
            self.turn('U')
            i += 1
            if i == 4:
                self.fix_complication()
                return

        if self.C_edge[0] == 'g':
            direction = self.left_or_right(self.C_edge)

            self.insert_piece(direction)
        else:

            dictionary = {
                'o': ['U', self.C_edge, 'left'],
                'r': ['-U', self.C_edge, 'right'],
                'b': ['U2', self.C_edge, 'back']
            }
            color_key = self.C_edge[0]
            self.turn(dictionary[color_key][0])
            direction = self.left_or_right(dictionary[color_key][1])
            self.insert_piece(direction, dictionary[color_key][2])


def main():
    edge = EdgesSolve()

    while not edge.is_solved():
        edge.top_edge_solve()

    for i in range(0, len(turn_history), 10):
        print(turn_history[i:i + 10])



    if ['b', 'o'] == edge.a_slot:
        print("True")
    else:
        print("False")
    if ['b', 'r'] == edge.b_slot:
        print("True")
    else:
        print("False")
    if ['g', 'r'] == edge.c_slot:
        print("True")
    else:
        print("False")
    if ['g', 'o'] == edge.d_slot:
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    main()