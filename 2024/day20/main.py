def read_input(input_file_dir: str) -> list[str]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    return lines

def calc_saves(maze: list[str], target_time_save: int, cheat_length) -> int:
    start, end, walls = initialize_info(maze)
    path: list[tuple[int,int]] = find_path(start, end, walls)

    res = 0
    for i, pos1 in enumerate(path):
        for j, pos2 in enumerate(path[i+1:]):
            steps_between = j + 1
            manhattan = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

            if steps_between - manhattan >= target_time_save and manhattan <= cheat_length:
                res += 1

    return res

def initialize_info(maze: list[str]) -> tuple[tuple[int,int],tuple[int,int],set[tuple[int,int]]]:
    walls: set[tuple[int,int]] = set()
    
    for row, line in enumerate(maze):
        for col, char in enumerate(line):
            if char == "#":
                walls.add((row,col))
            elif char == "S":
                start = (row,col)
            elif char == "E":
                end = (row,col)
    
    return start, end, walls

def find_path(
        start: tuple[int,int], 
        end: tuple[int,int], 
        walls: set[tuple[int,int]]) -> list[tuple[int,int]]:
    
    path: list[tuple[int,int]] = []
    row, col = start

    while True:
        path.append((row,col))

        if (row, col) == end:
            break

        if (row-1,col) not in walls and (row-1,col) not in path:
            row, col = row-1, col
        elif (row+1,col) not in walls and (row+1,col) not in path:
             row, col = row+1, col
        elif (row,col+1) not in walls and (row,col+1) not in path:
             row, col = row, col+1
        elif (row,col-1) not in walls and (row,col-1) not in path:
            row, col = row, col-1

    return path 

if __name__ == "__main__":
    input_file_dir = "input.txt"
    maze = read_input(input_file_dir)
    target_time_save = 100 if input_file_dir == "input.txt" else 50

    print(calc_saves(maze, target_time_save, 2))
    print(calc_saves(maze, target_time_save, 20))

