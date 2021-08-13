import unittest
import utility
import search_submission


class BFSTest(unittest.TestCase):

    def test_scenario_A_to_A(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.breadth_first_search(g, 'A', 'A')
        self.assertEqual(p, [])
        self.assertEqual(g.get_explored_nodes(), set())

    def test_scenario_A_to_B(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.breadth_first_search(g, 'A', 'B')
        self.assertEqual(p, ['A', 'S', 'F', 'B'])
        self.assertEqual(g.get_explored_nodes(), {'S', 'F', 'A', 'T', 'Z'})

    def test_scenario_A_to_C(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.breadth_first_search(g, 'A', 'C')
        self.assertEqual(p, ['A', 'S', 'R', 'C'])
        self.assertEqual(g.get_explored_nodes(), {'S', 'F', 'A', 'T', 'R', 'Z', 'O'})

    def test_scenario_B_to_E(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.breadth_first_search(g, 'B', 'E')
        self.assertEqual(p, ['B', 'U', 'H', 'E'])
        self.assertEqual(g.get_explored_nodes(), {'U', 'F', 'P', 'S', 'G', 'C', 'H', 'R', 'B'})

    def test_scenario_O_to_N(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.breadth_first_search(g, 'O', 'N')
        self.assertEqual(p, ['O', 'S', 'F', 'B', 'U', 'V', 'I', 'N'])
        self.assertEqual(g.get_explored_nodes(), {'S', 'F', 'I', 'G', 'C', 'H', 'R', 'B', 'L', 'D', 'U', 'P', 'A', 'E', 'Z', 'V', 'M', 'T', 'O'})


class UCSTest(unittest.TestCase):

    def test_scenario_A_to_A(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.uniform_cost_search(g, 'A', 'A')
        self.assertEqual(p, [])
        self.assertEqual(g.get_explored_nodes(), set())

    def test_scenario_A_to_B(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.uniform_cost_search(g, 'A', 'B')
        self.assertEqual(p, ['A', 'S', 'R', 'P', 'B'])
        self.assertEqual(g.get_explored_nodes(), {'D', 'S', 'F', 'A', 'P', 'Z', 'C', 'M', 'T', 'R', 'O', 'L'})

    def test_scenario_A_to_C(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.uniform_cost_search(g, 'A', 'C')
        self.assertEqual(p, ['A', 'S', 'R', 'C'])
        self.assertEqual(g.get_explored_nodes(), {'S', 'F', 'A', 'P', 'Z', 'M', 'T', 'R', 'O', 'L'})

    def test_scenario_B_to_E(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.uniform_cost_search(g, 'B', 'E')
        self.assertEqual(p, ['B', 'U', 'H', 'E'])
        self.assertEqual(g.get_explored_nodes(), {'U', 'F', 'P', 'G', 'V', 'C', 'H', 'R', 'B'})

    def test_scenario_O_to_N(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.uniform_cost_search(g, 'O', 'N')
        self.assertEqual(p, ['O', 'S', 'R', 'P', 'B', 'U', 'V', 'I', 'N'])
        self.assertEqual(g.get_explored_nodes(), {'S', 'F', 'I', 'G', 'C', 'H', 'R', 'B', 'L', 'D', 'U', 'P', 'A', 'E', 'Z', 'V', 'M', 'T', 'O'})


class ASTARTest(unittest.TestCase):

    def test_scenario_A_to_A(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.a_star(g, 'A', 'A')
        self.assertEqual(p, [])
        self.assertEqual(g.get_explored_nodes(), set())

    def test_scenario_A_to_B(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.a_star(g, 'A', 'B')
        self.assertEqual(p, ['A', 'S', 'R', 'P', 'B'])
        self.assertEqual(g.get_explored_nodes(), {'F', 'S', 'A', 'P', 'R'})

    def test_scenario_A_to_C(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.a_star(g, 'A', 'C')
        self.assertEqual(p, ['A', 'S', 'R', 'C'])
        self.assertEqual(g.get_explored_nodes(), {'S', 'A', 'T', 'R', 'Z', 'L'})

    def test_scenario_B_to_E(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.a_star(g, 'B', 'E')
        self.assertEqual(p, ['B', 'U', 'H', 'E'])
        self.assertEqual(g.get_explored_nodes(), {'H', 'U', 'B'})

    def test_scenario_O_to_N(self):
        g = utility.build_graph('Romania.in')
        p = search_submission.a_star(g, 'O', 'N')
        self.assertEqual(p, ['O', 'S', 'R', 'P', 'B', 'U', 'V', 'I', 'N'])
        self.assertEqual(g.get_explored_nodes(), {'F', 'S', 'I', 'G', 'C', 'R', 'B', 'L', 'U', 'P', 'A', 'Z', 'V', 'M', 'T', 'O'})

# g = utility.build_graph('Romania.in')
# p = search_submission.breadth_first_search(g, 'A', 'B')
