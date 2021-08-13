import numpy as np


def find_path_DFS(map, current, goal, explored, path, depth=0):
    # TODO: Create method to return the path from current to goal and all the explored nodes in that order.
    #print(path)
    if is_valid(current, map):
        path.append(current)
    if current not in explored:
        explored.append(current)
    if current == goal:
        return path, explored

    depth = depth+1
    #notice!! the function does not work
    #needs to return some things
    #correct is in my pics
    if is_valid((current[0]+1, current[1]), map) and (current[0]+1, current[1]) not in explored:
        find_path_DFS(map, (current[0]+1, current[1]), goal, explored, path, depth)

    if is_valid((current[0], current[1]+1), map) and (current[0], current[1]+1) not in explored:
        find_path_DFS(map, (current[0]+1, current[1]), goal, explored, path, depth)

    if is_valid((current[0]-1, current[1]), map) and (current[0]-1, current[1]) not in explored:
        find_path_DFS(map, (current[0]+1, current[1]), goal, explored, path, depth)

    if is_valid((current[0], current[1]-1), map) and (current[0], current[1]-1) not in explored:
        find_path_DFS(map, (current[0]+1, current[1]), goal, explored, path, depth)
    #add pop explored and path and call last explored
    #if path[-2] in explored:

    depth = depth-1
    if path[-1] in explored:
        del path[-1]
        #explored.remove(path[-1])
        find_path_DFS(map, path[-1], goal, explored, path, depth)
    #del explored[-1]
    #return None, None
    #and if not found return none, or something I guess
    return None, explored
    #problems are that elements in the full path are being skipped or added and removed


def is_valid(position, map):
    if not (0 <= position[0] < len(map) and 0 <= position[1] < len(map)):
        return False
    elif map[position[0]][position[1]] == 1:
        return False
    else:
        return True
