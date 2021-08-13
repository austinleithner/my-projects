from copy import copy
import math
from PriorityQueue import PriorityQueue


def breadth_first_search(graph, start, goal):
    # TODO: Complete this method
    if start == goal:
        return []
    #path = [start]
    frontier = [(start, [])]

    #frontier.append((start, ))
    #for neighbor in graph[start]:
    #    frontier.append((neighbor, path))
    #print(frontier)
    #cnt = 1
    #just in case I forget my code will not work if the count limit is 4 or less
    while len(frontier) > 0 :#and cnt < 5:
        #cnt += 1
        current, path = frontier[0]
        #print(frontier)
        #del frontier[0]
        frontier = frontier[1:]
        temp_path = copy(path)
        #print(temp_path)
        temp_path.append(current)
        if current == goal:
            return temp_path

        for neighbor in graph[current]:
            if neighbor == goal:
                # print(temp_path)
                temp_path.append(neighbor)
                return temp_path

            #print("Next is {}".format(current))
            if neighbor not in graph.get_explored_nodes() and not is_in_frontier(neighbor, frontier):
                frontier.append((neighbor, temp_path))

        #print(frontier)
    #if frontier is empty then no path was found so we return None
    return None


def is_in_frontier(v, frontier):
    for node, path in frontier:
        if node == v:
            return True
    return False


def uniform_cost_search(graph, start, goal):
    # TODO: Complete this method
    if start == goal:
        return []

    frontier = PriorityQueue()
    frontier.append((0, (start, [])))
    while frontier.has_next():
        #cnt += 1
        cost, node_data = frontier.pop()
        current, path = node_data
        #print(current)
        #print(path)

        #del frontier[0]
        #frontier = frontier[1:]
        temp_path = copy(path)
        #print(temp_path)
        temp_path.append(current)
        if current == goal:
            return temp_path

        for neighbor in graph[current]:
            #if neighbor == goal:
                # print(temp_path)
            #    temp_path.append(neighbor)
            #    return temp_path

            #print("Next is {}".format(current))
            if neighbor not in graph.get_explored_nodes() and not frontier.__contains__(neighbor):
                #need to add current weight to neighbor weight
                # todo get weight
                weight = graph[current][neighbor]['weight']
                weight += cost
                frontier.append((weight, (neighbor, temp_path)))

        #print(frontier)
    #if frontier is empty then no path was found so we return None
    return None


def euclidean_dist_heuristic(graph, v, goal):
    # TODO: Complete this method
    # get x,y pos for v and goal
    v_pos = graph.get_node_position(v)
    goal_pos = graph.get_node_position(goal)
    d_squared = (v_pos[0]-goal_pos[0])**2 + (v_pos[1]-goal_pos[1])**2
    return math.sqrt(d_squared)


def a_star(graph, start, goal, heuristic=euclidean_dist_heuristic):
    # TODO: Complete this method
    if start == goal:
        return []

    frontier = PriorityQueue()
    frontier.append((0, (start, [])))
    while frontier.has_next():
        #cnt += 1
        cost, node_data = frontier.pop()
        current, path = node_data
        #print(current)
        #print(path)
        cost -= heuristic(graph, current, goal)
        #del frontier[0]
        #frontier = frontier[1:]
        temp_path = copy(path)
        #print(temp_path)
        temp_path.append(current)
        if current == goal:
            return temp_path

        for neighbor in graph[current]:
            #if neighbor == goal:
                # print(temp_path)
            #    temp_path.append(neighbor)
            #    return temp_path

            #print("Next is {}".format(current))
            if neighbor not in graph.get_explored_nodes() and not frontier.__contains__(neighbor):
                #need to add current weight to neighbor weight
                # todo get weight
                weight = graph[current][neighbor]['weight']
                weight += cost
                weight += heuristic(graph, neighbor, goal)
                frontier.append((weight, (neighbor, temp_path)))

        #print(frontier)
    #if frontier is empty then no path was found so we return None
    return None


# Bonus Credit
def bidirectional_ucs(graph, start, goal):
    # TODO: Complete this method for Bonus
    return None


# Bonus Credit
def bidirectional_a_star(graph, start, goal, heuristic=euclidean_dist_heuristic):
    # TODO: Complete this method for Bonus
    return None

