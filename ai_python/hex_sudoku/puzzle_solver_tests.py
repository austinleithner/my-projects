import unittest
from puzzle_solver import *


class TestPuzzles(unittest.TestCase):
    def _puzzle_solution(self, filename, number):
        solutions = """0123456789abcdef456789abcdef012389abcdef01234567cdef0123456789ab123056749ab8defc56749ab8defc12309ab8defc12305674defc123056749ab823016745ab89efcd6745ab89efcd2301ab89efcd23016745efcd23016745ab8930127456b89afcde7456b89afcde3012b89afcde30127456fcde30127456b89a
b2574a9f6e01c38de409b82cd53af1761afc6d734982b5e0d8635e10b7fca94207e28b4916a5dc3f3591ace724df806bcfad21368be074596b840f5d7c93e2a12e1f37b45a690dc876c892a50d1b4ef34935e0d8f2c76b1aadb0f6c1384e9725912e740baf5638dc837ad962c1b45f0ef04bc58ae32d16975cd613fe90782ab4
106fa49c7582b3eddb231560c49efa7894e5f78d0ba32c617ac8b23e61fd095438a72cb649e15d0f564b7d1a280f9e3cecfd09435a6b71822190e8f53d7c4ba669314b7fae25d8c0cfde3628b017a49547ba50d98c361f2e8502cae19fd436b7a276df0b13c8e5490d1963c4e75a82fbbe5c81a7f24960d3f3849e52d6b0c71a
9714ecaf32508bd60538bd671c9f24aeb2a61935e8d4f0c7fdce820467ba5319a4075e93c162d8bf83d97126fe0ba54c1cb2fa8d4539e670ef6540cb7da89123498a35e1df26c70bc6eba7f083451d9220f3c6d89b174ae5517d24b9a0ec3f683a2c0b7e54f1698dd8519f4cb67e023a6b9fd8120ac37e547e40635a298dbcf1
bef65947da30c821d0832ef1746cb5a9a451c6d8e92b703f2c79ba03f185de6442301c5ab8e9f7d671df84b2c603a95ec5be9d76a2f40318689ae03f5d712b4cf31bd7690ea284c50647f32c1598edba5aed481b3fc69207892c05ae4bd761f33f64ab90871d5ce2eda871c5204f369b9b023f846c5e1a7d17c562ed93ba4f80
dc0723469e85a1fb3462a5917fb0ed8cb89aecfd124365701fe5087bd6ca42397d3b5a2e0814cf96654fb0d8c9327ea10e29671cf5abd843a18c493f67de50b28ad436e25197bc0f59768db04c2f13eafbc39157a0ed8624e210cfa43b68975d40adfb65e37c2918c7f8d209b4513a6e26b17ec38af904d5935e148a2d06fbc7
""".split('\n')
        puzzle = HexsudokuPuzzle(filename)
        puzzle.solve()
        return puzzle.return_solution_as_string(), solutions[number]

    def test_puzzle0(self):
        solution, expected = self._puzzle_solution('Puzzles\\puzzle0', 0)
        self.assertEqual(solution, expected)

    def test_puzzle1(self):
        solution, expected = self._puzzle_solution('Puzzles\\puzzle1', 1)
        self.assertEqual(solution, expected)

    def test_puzzle2(self):
        solution, expected = self._puzzle_solution('Puzzles\\puzzle2', 2)
        self.assertEqual(solution, expected)

    def test_puzzle3(self):
        solution, expected = self._puzzle_solution('Puzzles\\puzzle3', 3)
        self.assertEqual(solution, expected)

    def test_puzzle4(self):
        solution, expected = self._puzzle_solution('Puzzles\\puzzle4', 4)
        self.assertEqual(solution, expected)

    def test_puzzle5(self):
        solution, expected = self._puzzle_solution('Puzzles\\puzzle5', 5)
        self.assertEqual(solution, expected)