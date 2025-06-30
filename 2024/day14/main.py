from re import search

def read_input(input_file_dir: str) -> list[list[tuple[int,int]]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    robots = []
    for line in lines:
        if match := search(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line):
            robots.append([(int(match.group(1)), int(match.group(2))),(int(match.group(3)), int(match.group(4)))])

    return robots

def calc_safety(robots: list[list[tuple[int,int]]], width: int, height: int, seconds: int) -> int:
    quad1, quad2, quad3, quad4 = 0,0,0,0

    for robot in robots:
        x, y = get_final_pos(robot, width, height, seconds)
        if x < width // 2 and y < height // 2:
            quad1 += 1
        elif x > width // 2 and y < height // 2:
            quad2 += 1
        elif x < width // 2 and y > height // 2:
            quad3 += 1
        elif x > width // 2 and y > height // 2:
            quad4 += 1

    return quad1 * quad2 * quad3 * quad4

def get_final_pos(robot: list[tuple[int,int]], width: int, height: int, seconds: int) -> tuple[int,int]:
    x_start, y_start = robot[0]
    dx, dy = robot[1]

    x = (x_start + dx * seconds) % width
    y = (y_start + dy * seconds) % height

    return (x, y)

def find_christmas_tree(robots: list[list[tuple[int,int]]], width: int, height: int) -> int:
    # finds the lowest safety score that is not 0

    time: list[int] = []
    scores: list[int] = []

    for i in range(10000):
        time.append(i)
        scores.append(calc_safety(robots, width, height, i))

    min_time = -1
    min = float("inf")
    for i, score in enumerate(scores):
        if score != 0 and score < min:
            min = score
            min_time = i

    return min_time

if __name__ == "__main__":
    input_file_dir = "input.txt"
    robots = read_input(input_file_dir)

    if input_file_dir == "input.txt":
        width, height = 101, 103
    else:
        width, height = 11, 7

    print(calc_safety(robots, width, height, 100))
    print(find_christmas_tree(robots, width, height))