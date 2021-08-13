from puzzle_solver import *
from os import listdir
from os.path import isfile, join

puzzles_dir = 'Puzzles'


for puzzle_file in [f for f in listdir(puzzles_dir) if isfile(join(puzzles_dir, f))]:
#for puzzle_file in ['puzzle5']:
    puzzle = HexsudokuPuzzle(puzzles_dir + '\\' + puzzle_file)
    puzzle.solve()
    solution = puzzle.return_solution_as_string()
    print(solution)
    #puzzle.print_solution(solution)

