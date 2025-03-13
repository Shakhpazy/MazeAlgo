from collections import deque

FNAME = "maze1.txt"

def mazeFileToMatrix(theFileName):
    result = []
    try:
        with open(theFileName,"r") as file:
            lines = file.readlines()
            for line in lines:
                result.append(line.strip())
    except FileNotFoundError:
        print("File is not found")
    
    return result

def find_start_end(maze):
    start = None
    end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            current = maze[i][j]
            if current == "S":
                start = [i, j]
            elif current == "E":
                end = [i, j]
    if start is None:
        print("Error: Start position 'S' not found in maze.")
    if end is None:
        print("Error: End position 'E' not found in maze.")

    return start, end



def dfs(maze, currentPos, start, end, visited):
    if (currentPos == end):
        return True
    
    visited.add(tuple(currentPos))
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # Right, Left, Down, Up

    for move in moves:
        nextrow = currentPos[0] + move[0]
        nextcol = currentPos[1] + move[1]
        nextPos = [nextrow, nextcol]
        nextPosTuple = tuple(nextPos)

        if (0 <= nextrow < len(maze) and 0 <= nextcol < len(maze[0]) and nextPos != "X" and nextPosTuple not in visited):
            if dfs(maze, nextPos, start, end, visited):
                return True
    
    return False

def solve_maze_bfs(maze, start, end):
    queue = deque([(start, [start])]) 
    visited = {tuple(start)}

    while queue:
        (row, col), path = queue.popleft()

        if [row, col] == end:
            return True

        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            new_pos = [new_row, new_col]
            new_pos_tuple = tuple(new_pos)

            if (0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and
                    maze[new_row][new_col] != 'X' and new_pos_tuple not in visited):
                queue.append(([new_row, new_col], path + [[new_row, new_col]]))
                visited.add(new_pos_tuple)

    return None



maze = mazeFileToMatrix(FNAME)
start, end = find_start_end(maze)
check1 = dfs(maze, start, start, end, set())
check2 = solve_maze_bfs(maze, start, end)

print(check1)
print(check2)
