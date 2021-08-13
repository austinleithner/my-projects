import numpy as np
import map_path
import unittest
from os.path import join


class MapTest(unittest.TestCase):
    def test_scenario_0(self):
        m = np.load(join('Maps', 'Map0.npy'))
        start = (0, 0)
        end = (0, 0)
        result_path, result_explored = map_path.find_path_DFS(m, start, end, [], [])
        self.assertEqual(result_path, [(0, 0)])
        self.assertEqual(result_explored, [(0, 0)])

    def test_scenario_1(self):
        m = np.load(join('Maps', 'Map0.npy'))
        start = (0, 0)
        end = (4, 4)
        result_path, result_explored = map_path.find_path_DFS(m, start, end, [], [])
        self.assertEqual(result_path, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])
        self.assertEqual(result_explored, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])

    def test_scenario_2(self):
        m = np.load(join('Maps', 'Map1.npy'))
        start = (0, 0)
        end = (4, 4)
        result_path, result_explored = map_path.find_path_DFS(m, start, end, [], [])
        self.assertEqual(result_path,
                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 3), (2, 2), (2, 1), (2, 0),
                           (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])
        self.assertEqual(result_explored,
                          [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 3), (2, 2), (2, 1), (2, 0),
                           (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])

    def test_scenario_3(self):
        m = np.load(join('Maps', 'Map2.npy'))
        start = (0, 0)
        end = (4, 4)
        result_path, result_explored = map_path.find_path_DFS(m, start, end, [], [])
        self.assertEqual(result_path, None)
        self.assertEqual(result_explored,
                          [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (0, 4), (0, 3), (0, 2), (0, 1)])

    def test_scenario_4(self):
        m = np.load(join('Maps', 'Map2.npy'))
        start = (0, 0)
        end = (0, 1)
        result_path, result_explored = map_path.find_path_DFS(m, start, end, [], [])
        self.assertEqual(result_path, [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (0, 4), (0, 3), (0, 2), (0, 1)])
        self.assertEqual(result_explored,
                          [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (0, 4), (0, 3), (0, 2), (0, 1)])

    def test_scenario_5(self):
        m = np.load(join('Maps', 'Map3.npy'))
        start = (0, 0)
        end = (4, 0)
        result_path, result_explored = map_path.find_path_DFS(m, start, end, [], [])
        self.assertEqual(result_path, [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (4, 0)])
        self.assertEqual(result_explored,
                          [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4), (3, 3), (2, 3),
                           (2, 4), (1, 3), (0, 3), (0, 4), (0, 2), (2, 2), (4, 0)])

    def test_scenario_6(self):
        m = np.load(join('Maps', 'Map4.npy'))
        start = (0, 3)
        end = (1, 1)
        result_path, result_explored = map_path.find_path_DFS(m, start, end, [], [])
        self.assertEqual(result_path,
                          [(0, 3), (1, 3), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5), (5, 5), (6, 5), (6, 4), (6, 3),
                           (5, 3), (4, 3), (4, 2), (3, 2), (2, 2), (2, 1), (1, 1)])
        self.assertEqual(result_explored,
                          [(0, 3), (1, 3), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5), (5, 5), (6, 5), (6, 6), (6, 4),
                           (6, 3), (5, 3), (4, 3), (4, 2), (3, 2), (2, 2), (2, 1), (1, 1)])

    def test_scenario_7(self):
        m = np.load(join('Maps', 'Map5.npy'))
        start = (0, 3)
        end = (0, 0)
        result_path, result_explored = map_path.find_path_DFS(m, start, end, [], [])
        self.assertEqual(result_path,
                          [(0, 3), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (6, 1), (6, 0), (5, 0),
                           (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)])
        self.assertEqual(result_explored,
                          [(0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (6, 5), (6, 6), (5, 6),
                           (4, 6), (3, 6), (2, 6), (1, 6), (0, 6), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
                           (6, 2), (6, 1), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)])

    def test_scenario_8(self):
        m = np.load(join('Maps', 'Map6.npy'))
        start = (2, 2)
        end = (2, 4)
        result_path, result_explored = map_path.find_path_DFS(m, start, end, [], [])
        self.assertEqual(result_path, None)
        self.assertEqual(result_explored,
                          [(2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1),
                           (1, 2), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])

    def test_scenario_9(self):
        m = np.load(join('Maps', 'Map7.npy'))
        start = (2, 2)
        end = (2, 4)
        result_path, result_explored = map_path.find_path_DFS(m, start, end, [], [])
        self.assertEqual(result_path,
                          [(2, 2), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (2, 6), (1, 6), (0, 6), (0, 5), (1, 5),
                           (2, 5), (2, 4)])
        self.assertEqual(result_explored,
                          [(2, 2), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (2, 6), (1, 6), (0, 6), (0, 5), (1, 5),
                           (2, 5), (2, 4)])

    def test_scenario_10(self):
        m = np.load(join('Maps', 'Map7.npy'))
        start = (2, 2)
        end = (6, 6)
        result_path, result_explored = map_path.find_path_DFS(m, start, end, [], [])
        self.assertEqual(result_path, None)
        self.assertEqual(result_explored,
                          [(2, 2), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (2, 6), (1, 6), (0, 6), (0, 5), (1, 5),
                           (2, 5), (2, 4), (1, 4), (0, 4), (3, 1), (2, 1), (1, 1), (1, 2), (0, 2), (0, 1), (0, 0),
                           (1, 0), (2, 0), (3, 0)])


if __name__ == '__main__':
    unittest.main()
