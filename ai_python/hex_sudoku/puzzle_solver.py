import copy


class HexsudokuPuzzle:

    def __init__(self, filename):
        """
        Constructor for the class given the filename as a string.
        :param filename:  String pointing to the file
        """
        #todo parse file into str of len 256 set equal to grid
        self.grid_str = ""
        self.grid_dict = None
        self.solution_string = ""

        self.digits = '0123456789abcdef'
        self.rows = 'ABCDEFGHIJKLMNOP'
        self.cols = self.digits
        self.squares = self.cross(self.rows, self.cols)
        unit_list = ([self.cross(self.rows, c) for c in self.cols] +
                    [self.cross(r, self.cols) for r in self.rows] +
                    [self.cross(rs, cs) for rs in ('ABCD', 'EFGH', 'IJKL', 'MNOP') for cs in
                     ('0123', '4567', '89ab', 'cdef')])
        self.units = dict((s, [u for u in unit_list if s in u]) for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s], [])) - set([s])) for s in self.squares)

        with open(filename, 'r') as file:
            for line in file:
                self.grid_str += str(line)
        #if len(self.grid_str) != 256:
        #    print("file " + filename + "has the incorrect format")

    def cross(self, set_a, set_b):
        return [a + b for a in set_a for b in set_b]

    def solve(self):
        """
        finds the solution to the current puzzle
        """
        self.grid_dict = self.grid_search(self.parse_grid(self.grid_str))

    def grid_search(self, values):
        if values is False:
            return False

        if all(len(values[s]) == 1 for s in self.squares):
            return values

        n, s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
        return self.some(self.grid_search(self.assign(values.copy(), s, d))for d in values[s])

    def some(self, sequence):
        for elem in sequence:
            if elem:
                return elem
        return False

    def parse_grid(self, grid):
        #creates dict and assigns value to the dict value
        values = dict((s, self.digits) for s in self.squares)

        for s, d in self.grid_values(grid).items():
            if d in self.digits and not self.assign(values, s, d):
                return False
        return values

    def grid_values(self, grid):
        #creates dict with key = squares
        chars = [c for c in grid if c in self.digits or c in '.']
        assert len(chars) == 256
        return dict(zip(self.squares, chars))

    def assign(self, values, s, d):
        #assigns values to the value dict of key s
        other_values = values[s].replace(d, '')

        if all(self.eliminate(values, s, other) for other in other_values):
            return values
        else:
            return False

    def eliminate(self, values, s, d):
        if d not in values[s]:
            return values
        values[s] = values[s].replace(d, '')

        if len(values[s]) == 0:
            return False
        elif len(values[s]) == 1:
            d2 = values[s]

            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[s]):
                return False

        for u in self.units[s]:
            digit_places = [s for s in u if d in values[s]]

            if len(digit_places) == 0:
                return False
            elif len(digit_places) == 1:
                if not self.assign(values, digit_places[0], d):
                    return False
        return values

    def return_solution_as_string(self):
        """
        Returns the solution to the puzzle as a string of length 256 
        :return: String of length 256
        """
        #todo grid dict solution to string
        #loop through cross values?
        #does the cross product return values in grid order?
        for key in self.squares:
            self.solution_string += self.grid_dict[key]
        if len(self.solution_string) == 256:
            return self.solution_string
        return None

    def print_solution(self, grid_as_string):
        """
        print out the solution to the puzzle in the form of
            # # # # | # # # # | # # # # | # # # #
            # # # # | # # # # | # # # # | # # # #
            # # # # | # # # # | # # # # | # # # #
            # # # # | # # # # | # # # # | # # # #
            -------------------------------------
            # # # # | # # # # | # # # # | # # # #
            # # # # | # # # # | # # # # | # # # #
            # # # # | # # # # | # # # # | # # # #
            # # # # | # # # # | # # # # | # # # #
            -------------------------------------
            # # # # | # # # # | # # # # | # # # #
            # # # # | # # # # | # # # # | # # # #
            # # # # | # # # # | # # # # | # # # #
            # # # # | # # # # | # # # # | # # # #
            -------------------------------------
            # # # # | # # # # | # # # # | # # # #
            # # # # | # # # # | # # # # | # # # #
            # # # # | # # # # | # # # # | # # # #
            # # # # | # # # # | # # # # | # # # #

        :param grid_as_string: A single string of all the values in the grid with no \n
        :return: None
        """
        assert len(grid_as_string) == 256
        for i in range(len(grid_as_string)):
            print(grid_as_string[i] + ' ', end='')
            if i % 16 == 15:
                print()
                if i % 64 == 63 and i != 255:
                    print('-------------------------------------')
            elif i % 4 == 3:
                print('| ', end='')
