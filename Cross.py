print(f"Scramble: L' B2 R2 U L2 U F2 D' F2 U L2 B2 F' R D2 B U B R2'")

from Operations import *
class Cube:
    def __init__(self):
        self.topSide = np.array([
            ['o', 'o', 'w'],
            ['o', 'w', 'w'],
            ['g', 'g', 'g']
        ])
        self.leftSide = np.array([
            ['b', 'w', 'r'],
            ['y', 'o', 'g'],
            ['o', 'r', 'r']
        ])
        self.frontSide = np.array([
            ['w', 'y', 'w'],
            ['o', 'g', 'g'],
            ['y', 'r', 'g']
        ])
        self.rightSide = np.array([
            ['o', 'r', 'r'],
            ['r', 'r', 'b'],
            ['y', 'b', 'r']
        ])
        self.backSide = np.array([
            ['b', 'y', 'w'],
            ['w', 'b', 'b'],
            ['b', 'g', 'b']
        ])
        self.bottomSide = np.array([
            ['g', 'y', 'o'],
            ['b', 'y', 'o'],
            ['y', 'w', 'y']
        ])


    @property
    def green_bottom(self):
        return list(map(str, [self.bottomSide[0][1], self.frontSide[2][1]]))
    @property
    def orange_bottom(self):
        return list(map(str, [self.bottomSide[1][0], self.leftSide[2][1]]))
    @property
    def blue_bottom(self):
        return list(map(str, [self.bottomSide[2][1], self.backSide[2][1]]))
    @property
    def red_bottom(self):
        return list(map(str, [self.bottomSide[1][2], self.rightSide[2][1]]))


    @property
    def blue_top(self):
        return list(map(str, [self.topSide[0][1], self.backSide[0][1]]))
    @property
    def red_top(self):
        return list(map(str, [self.topSide[1][2], self.rightSide[0][1]]))
    @property
    def green_top(self):
        return list(map(str, [self.topSide[2][1], self.frontSide[0][1]]))
    @property
    def orange_top(self):
        return list(map(str, [self.topSide[1][0], self.leftSide[0][1]]))
    @property
    def blue_mid(self):
        return list(map(str, [self.backSide[1][2], self.leftSide[1][0]]))
    @property
    def red_mid(self):
        return list(map(str, [self.backSide[1][0], self.rightSide[1][2]]))
    @property
    def green_mid(self):
        return list(map(str, [self.frontSide[1][2], self.rightSide[1][0]]))
    @property
    def orange_mid(self):
        return list(map(str, [self.frontSide[1][0], self.leftSide[1][2]]))


    green_tuple = ('y', 'g')
    orange_tuple = ('y', 'o')
    blue_tuple = ('y', 'b')
    red_tuple = ('y', 'r')




    def turn(self, side):
        turns(self, side)


    def side(self, edge_tuple):
        if sorted(edge_tuple) == sorted(self.red_top):
            return 'right'
        elif sorted(edge_tuple) == sorted(self.blue_top):
            return 'back'
        elif sorted(edge_tuple) == sorted(self. orange_top):
            return 'left'
        elif sorted(edge_tuple) == sorted(self.green_top):
            return 'front'



    def solved_pieces(self, edge_tuple=None):
        current = [self.green_bottom, self.orange_bottom, self.blue_bottom, self.red_bottom]
        solved = [self.green_tuple, self.orange_tuple, self.blue_tuple, self.red_tuple]

        dictionary = {
            0: 'front',
            1: 'left',
            2: 'back',
            3: 'right'
        }
        if edge_tuple in solved:
            index = solved.index(edge_tuple)
            if tuple(current[index]) == edge_tuple:
                return True
            else:
                return False
        solved_pieces = []
        for i in range(4):
            if tuple(current[i]) == solved[i]:
                solved_pieces.append(dictionary[i])

        return solved_pieces


    def locate_edge(self, edge_tuple): #input tuple
        top = [self.blue_top, self.red_top, self.green_top, self.orange_top]
        mid = [self.blue_mid, self.red_mid, self.green_mid, self.orange_mid]
        bottom = [self.blue_bottom, self.red_bottom, self.green_bottom, self.orange_bottom]

        dictionary = {0: ['top', top], 1: ['mid', mid], 2: ['bottom', bottom]}
        dictionary1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

        for j in range(3):
            for i in range(4):
                if sorted(edge_tuple) == sorted(tuple(dictionary[j][1][i])):
                    if edge_tuple == tuple(dictionary[j][1][i]):
                        return [dictionary[j][0], 'aligned', dictionary1[i]]
                    else:
                        return [dictionary[j][0], 'misaligned', dictionary1[i]]


    def solve_top_aligned(self, edge_tuple):
        if self.locate_edge(edge_tuple)[0] != 'top' or self.locate_edge(edge_tuple)[1] != 'aligned':
            raise ValueError(f"{edge_tuple} is not in top or is not aligned ({self.locate_edge(edge_tuple)[0], self.locate_edge(edge_tuple)[1]})")
        align_green = {'A': 'U2', 'B': 'U', 'C': '', 'D': '-U'}
        align_red = {'A': 'U', 'B': '', 'C': '-U', 'D': 'U2'}
        align_blue = {'A': '', 'B': '-U', 'C': 'U2', 'D': 'U'}
        align_orange = {'A': '-U', 'B': 'U2', 'C': 'U', 'D': ''}

        insert_edge_mapping = {self.green_tuple: 'F2', self.red_tuple: 'R2',
                               self.blue_tuple: 'B2', self.orange_tuple: 'L2'}

        dictionary = {self.green_tuple: align_green, self.red_tuple: align_red,
                      self.blue_tuple: align_blue, self.orange_tuple: align_orange}
        print([dictionary[edge_tuple][self.locate_edge(edge_tuple)[2]], insert_edge_mapping[edge_tuple]])
        moves = [dictionary[edge_tuple][self.locate_edge(edge_tuple)[2]], insert_edge_mapping[edge_tuple]]
        for move in moves:
            self.turn(move)


    def solve_top_misaligned(self, edge_tuple):
        if self.locate_edge(edge_tuple)[0] != 'top' or self.locate_edge(edge_tuple)[1] != 'misaligned':
            raise ValueError(
                f"{edge_tuple} is not in top or is not misaligned ({self.locate_edge(edge_tuple)[0], self.locate_edge(edge_tuple)[1]})")

        green_solve = {
            'A': ['U -R F'.split(), '-U L -F'.split()],
            'B': ['-R F'.split()],
            'C': ['-U -R F'.split(), 'U L -F'.split()],
            'D': ['L -F'.split()]
        }
        order = {
            self.green_tuple: 'A B C D'.split(),
            self.red_tuple: 'B C D A'.split(), #rotate_moves right
            self.blue_tuple: 'C D A B'.split(), #rotate_moves back
            self.orange_tuple: 'D A B C'.split() #rotate_moves left
        }
        rotate = {
            self.red_tuple: 'right',
            self.blue_tuple: 'back',
            self.orange_tuple: 'left'
        }

        general_dictionary = {}
        for i in range(4):
            general_dictionary[list(green_solve.keys())[i]] = green_solve[order[edge_tuple][i]]

        solved_edges = self.solved_pieces()


        if len(general_dictionary[self.locate_edge(edge_tuple)[2]]) == 1: #len(solved_edges) == 0:
            moves = general_dictionary[self.locate_edge(edge_tuple)[2]][0]
            if edge_tuple != self.green_tuple:
                moves = rotate_moves(moves, rotate[edge_tuple])
            if self.side(edge_tuple) in solved_edges:
                moves.extend(undo_moves(list(moves[-2])))
            print(moves)
            for move in moves:
                self.turn(move)
                return
        elif len(general_dictionary[self.locate_edge(edge_tuple)[2]]) > 1:
            bad_inserts = {
                self.green_tuple: {'left', 'right'},
                self.red_tuple: {'front', 'back'},
                self.blue_tuple: {'left', 'right'},
                self.orange_tuple: {'front', 'back'}
            }
            intersection = bad_inserts[edge_tuple] & set(solved_edges)






        #Use solved_pieces() to see if a correcting move must be done
        #Make dictionary like: solve_green = {'D': ['-U L -F'.split(),
        # 'U -R F'.split(), etc.} but make it general
        #Check if we need correction move to fix other piece
        #Create a general dictionary using rotate moves


    def solve_edge(self, edge_direction): # ('left', 'front', etc)
        if edge_direction in self.solved_pieces():
            return




def main():

    cross = Cube()

    def cube_state():
        print("         [" + " ".join(cross.topSide[0, :]) + "]")
        print("         [" + " ".join(cross.topSide[1, :]) + "]")
        print("         [" + " ".join(cross.topSide[2, :]) + "]")
        print()
        for i in range(3):
            print("[" + " ".join(cross.leftSide[i, :]) + "]" + "   " +
                  "[" + " ".join(cross.frontSide[i, :]) + "]" + "   " +
                  "[" + " ".join(cross.rightSide[i, :]) + "]" + "   " +
                  "[" + " ".join(cross.backSide[i, :]) + "]")
        print()
        print("         [" + " ".join(cross.bottomSide[0, :]) + "]")
        print("         [" + " ".join(cross.bottomSide[1, :]) + "]")
        print("         [" + " ".join(cross.bottomSide[2, :]) + "]")



    moves = ''.split()
    for move in moves:
        cross.turn(move)

    cross.solve_top_misaligned(cross.green_tuple)

    cube_state()

if __name__ == '__main__':
    main()




