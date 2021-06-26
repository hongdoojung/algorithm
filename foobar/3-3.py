# Prepare the Bunnies' Escape
# ===========================

# You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

# You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

# Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
# Output:
#     7

import copy

def get_near_items(matrix, row, col):
    a = 1000 if row == 0 else matrix[row-1][col]
    b = 1000 if col == len(matrix[0])-1 else matrix[row][col+1]
    c = 1000 if row == len(matrix)-1 else matrix[row+1][col]
    d = 1000 if col == 0 else matrix[row][col-1]
    return a, b, c, d

def get_update_matrix(need_updates, new_matrix, matrix):
    new_new_matrix = copy.deepcopy(new_matrix)
    while need_updates:
        (row, col,) = need_updates[0]
        # print(row, col)
        A,B,C,D = get_near_items(matrix, row, col)
        a,b,c,d = get_near_items(new_new_matrix, row, col)

        if A==0 and a > new_new_matrix[row][col] + 1:
            need_updates.append((row-1, col,))
            new_new_matrix[row-1][col] = new_new_matrix[row][col] + 1
        
        if B==0 and b > new_new_matrix[row][col] + 1:
            need_updates.append((row, col+1,))
            new_new_matrix[row][col+1] = new_new_matrix[row][col] + 1
        
        if C==0 and c > new_new_matrix[row][col] + 1:
            need_updates.append((row+1, col,))
            new_new_matrix[row+1][col] = new_new_matrix[row][col] + 1

        if D==0 and d > new_new_matrix[row][col] + 1:
            need_updates.append((row, col-1,))
            new_new_matrix[row][col-1] = new_new_matrix[row][col] + 1

        del need_updates[0]

    return new_new_matrix

def solution(matrix):
    new_matrix = [[1000 for item in row] for row in matrix]
    row, col = 0, 0
    new_matrix[row][col] = 1
    need_updates = [(0,0,)]

    new_matrix = get_update_matrix(need_updates, new_matrix, matrix)
    candidates = [new_matrix[-1][-1]]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                matrix[row][col] = 0
                new_new_matrix = copy.deepcopy(new_matrix)
                a,b,c,d = get_near_items(new_new_matrix, row, col)
                new_new_matrix[row][col] = min(a,b,c,d) + 1
                need_updates = [(row, col,)]
                new_new_matrix = get_update_matrix(need_updates, new_new_matrix, matrix)
                candidates.append(new_new_matrix[-1][-1])
                matrix[row][col] = 1
    
    return min(candidates)
    
def main():
    print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))

if __name__ == "__main__":
    main()