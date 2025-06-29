def read_input(input_file_dir: str) -> list[list[int]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    map: list[list[int]] = []
    for line in lines:
        map += [[int(n) for n in line]]
    return map

def calc_trailscores(map: list[list[int]]) -> int:
    res = 0

    for row, line in enumerate(map):
        for col, num in enumerate(line):
            if num == 0:
                reached: set[tuple[int,int]] = set()
                find_trail_score(reached,map,num,row,col)
                res += len(reached)
    
    return res

def find_trail_score(reached: set[tuple[int,int]], map: list[list[int]], num: int, row: int, col: int) -> None:
    if num == 9:
        reached.add((row,col))
    
    target = num + 1
    if row + 1 < len(map) and map[row+1][col] == target:
        find_trail_score(reached, map, target, row+1, col)
    if col + 1 < len(map[row]) and map[row][col+1] == target:
        find_trail_score(reached, map, target, row, col+1)
    if row - 1 >= 0 and map[row-1][col] == target:
        find_trail_score(reached, map, target, row-1, col)
    if col - 1 >= 0 and map[row][col-1] == target:
        find_trail_score(reached, map, target, row, col-1)

    return 

def calc_ratings(map: list[list[int]]) -> int:
    reached: list[int] = [0]

    for row, line in enumerate(map):
        for col, num in enumerate(line):
            if num == 0:
                find_trail_rating(reached,map,num,row,col)
    
    return reached[0]

def find_trail_rating(reached: list[int], map: list[list[int]], num: int, row: int, col: int) -> None:
    if num == 9:
        reached[0] += 1
    
    target = num + 1
    if row + 1 < len(map) and map[row+1][col] == target:
        find_trail_rating(reached, map, target, row+1, col)
    if col + 1 < len(map[row]) and map[row][col+1] == target:
        find_trail_rating(reached, map, target, row, col+1)
    if row - 1 >= 0 and map[row-1][col] == target:
        find_trail_rating(reached, map, target, row-1, col)
    if col - 1 >= 0 and map[row][col-1] == target:
        find_trail_rating(reached, map, target, row, col-1)

    return 

if __name__ == "__main__":
    map = read_input("input.txt")
    print(calc_trailscores(map))
    print(calc_ratings(map))