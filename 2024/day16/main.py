import heapq

def read_input(input_file_dir: str) -> list[str]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    return lines

def calc_lowest_score(maze: list[str]) -> int:
    start, end, walls = initialize_info(maze)

    # queue: cost, row, col, dr, dc
    queue: list[tuple[int,int,int,int,int]] = [(0, *start, 0, 1)]
    seen: set[tuple[int,int,int,int]] = {(*start, 0, 1)}

    while queue:
        cost, row, col, dr, dc = heapq.heappop(queue)
        seen.add((row, col, dr, dc))

        if (row, col) == end:
            return cost
        if (row+dr, col+dc) not in walls and (row+dr, col+dc, dr, dc) not in seen:
            heapq.heappush(queue, (cost+1, row+dr, col+dc, dr, dc))
        if (row, col, -dc, dr) not in seen:
            heapq.heappush(queue, (cost+1000, row, col, -dc, dr))
        if (row, col, dc, -dr) not in seen:
            heapq.heappush(queue, (cost+1000, row, col, dc, -dr))

    return -1

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

def calc_tiles_on_path(maze: list[str]) -> int:
    start, end, walls = initialize_info(maze)

    queue: list[tuple[int,int,int,int,int,list[tuple[int,int]]]] = [(0, *start, 0, 1, [start])]
    seen: set[tuple[int,int,int,int]] = {(*start, 0, 1)}
    points: set[tuple[int,int]] = set()
    min_cost = float("inf")

    while queue:
        cost, row, col, dr, dc, path = heapq.heappop(queue)
        seen.add((row, col, dr, dc))

        if (row, col) == end:
            if cost <= min_cost:
                min_cost = cost
                for point in path:
                    points.add(point)
                points.add(end)
                
        if (row+dr, col+dc) not in walls and (row+dr, col+dc, dr, dc) not in seen:
            heapq.heappush(queue, (cost+1, row+dr, col+dc, dr, dc, path + [(row,col)]))
        if (row, col, -dc, dr) not in seen:
            heapq.heappush(queue, (cost+1000, row, col, -dc, dr, path))
        if (row, col, dc, -dr) not in seen:
            heapq.heappush(queue, (cost+1000, row, col, dc, -dr, path))

    return len(points)

if __name__ == "__main__":
    input_file_dir = "input.txt"
    maze = read_input(input_file_dir)
    print(calc_lowest_score(maze))
    print(calc_tiles_on_path(maze))
