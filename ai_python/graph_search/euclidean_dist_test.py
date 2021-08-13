import unittest
import utility
import search_submission

class EuclideanDistTest(unittest.TestCase):

    def test_euclidean_dist_A_A(self):
        g = utility.build_graph('Romania.in')
        res = search_submission.euclidean_dist_heuristic(g, 'A', 'A')
        self.assertAlmostEqual(0.0, res, delta=0.0001)

    def test_euclidean_dist_A_B(self):
        g = utility.build_graph('Romania.in')
        res = search_submission.euclidean_dist_heuristic(g, 'A', 'B')
        self.assertAlmostEqual(350.294162098, res, delta=0.0001)

    def test_euclidean_dist_O_N(self):
        g = utility.build_graph('Romania.in')
        res = search_submission.euclidean_dist_heuristic(g, 'O', 'N')
        self.assertAlmostEqual(277.09384691833196, res, delta=0.0001)

    def test_euclidean_dist_D_E(self):
        g = utility.build_graph('Romania.in')
        res = search_submission.euclidean_dist_heuristic(g, 'D', 'E')
        self.assertAlmostEqual(397.04533746160524, res, delta=0.0001)

    def test_euclidean_dist_E_D(self):
        g = utility.build_graph('Romania.in')
        res = search_submission.euclidean_dist_heuristic(g, 'E', 'D')
        self.assertAlmostEqual(397.04533746160524, res, delta=0.0001)

    def test_euclidean_dist_R_L(self):
        g = utility.build_graph('Romania.in')
        res = search_submission.euclidean_dist_heuristic(g, 'R', 'L')
        self.assertAlmostEqual(74.73285756613352, res, delta=0.0001)
