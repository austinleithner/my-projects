import search_submission
import utility


start = 'O'
goal = 'N'
g = utility.build_graph('Romania.in')

print("Start node {} is at position {}".format(start, g.get_node_position(start)))
print("Goal node {} is at position {}".format(goal, g.get_node_position(goal)))

p = search_submission.breadth_first_search(g, start, goal)
utility.draw_graph(g, start, goal, p)

