import PriorityQueue as PQ
import utility

graph = utility.build_graph('Romania.in')
current_city = 'A'
goal = 'B'

"""
Example of finding the node neighbors of a given city.
NOTE: the use of 'weight' and 'pos' to get the values are not accessed the same
"""
print("Example of traversing through the graph:")
print('The value for graph["A"] = '+str(graph[current_city]))
print('Current City '+str(current_city)+' has neighbors:')
for neighbor in graph[current_city]:
    print('--'+str(neighbor))
    print('----weight: '+str(graph[current_city][neighbor]['weight']))
    print('----pos: '+str(graph.node[neighbor]['pos']))


"""
Example of setting up the frontier in a PriorityQueue
"""
frontier = PQ.PriorityQueue()
path = []
frontier.append((0, {current_city: path}))
current_cost, current_city_info = frontier.pop()
for key in current_city_info.keys(): #should only be one key but this will keep from throwing an error
    current_city = key
    current_path = current_city_info[key]

for neighbor in graph[current_city]:
    new_path = current_path+[current_city]
    frontier.append((current_cost+graph[current_city][neighbor]['weight'], {neighbor: new_path}))

print("\n\nExample of frontier values")
print(frontier)