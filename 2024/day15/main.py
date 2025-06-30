def read_input(input_file_dir: str) -> tuple[list[list[str]], list[tuple[int,int]]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    grid = []
    moves = []
    for line in lines:
        if line.startswith("#"):
            grid.append([char for char in line])
        elif line.startswith(("^","v","<",">")):
            for move in line:
                if move == "^":
                    moves.append((-1,0))
                elif move == "v":
                    moves.append((1,0))
                elif move == "<":
                    moves.append((0,-1))
                elif move == ">":
                    moves.append((0,1))

    return grid, moves

def calc_boxsum(grid: list[list[str]], moves: list[tuple[int,int]]) -> int:
    robot: set[tuple[int,int]] = set()
    walls: set[tuple[int,int]] = set()
    boxes: set[tuple[int,int]] = set()

    initialize_sets(grid,robot,walls,boxes)
    for move in moves:
        simulate_move(robot,walls,boxes,move)

    res = 0
    for box in boxes:
        row, col = box
        res += 100 * row + col

    return res

def initialize_sets(
        grid: list[list[str]], 
        robot: set[tuple[int,int]], 
        walls: set[tuple[int,int]], 
        boxes: set[tuple[int,int]]) -> None:
    
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == "@":
                robot.add((row,col))
            elif char == "#":
                walls.add((row,col))
            elif char == "O":
                boxes.add((row,col))
    
    return

def simulate_move(
        robot: set[tuple[int,int]], 
        walls: set[tuple[int,int]], 
        boxes: set[tuple[int,int]],
        move: tuple[int,int]) -> None:
    
    move_list: set[tuple[int,int]] = set()
    row, col = next(iter(robot))
    dr, dc = move

    if check_move(move_list, walls, boxes, row, col, dr, dc):
        do_move(move_list, robot, boxes, dr, dc)

    return

def check_move(
        move_list: set[tuple[int,int]],
        walls: set[tuple[int,int]], 
        boxes: set[tuple[int,int]],
        row: int,
        col: int,
        dr: int,
        dc: int) -> bool:
    # Also updates the move_list with movable objects
    
    move_list.add((row, col))
    if (row+dr, col+dc) in walls:
        return False
    elif (row+dr, col+dc) in boxes:
        return check_move(move_list,walls,boxes,row+dr,col+dc,dr,dc)
    else:
        return True

def do_move(
        move_list: set[tuple[int,int]],
        robot: set[tuple[int,int]],
        boxes: set[tuple[int,int]],
        dr: int,
        dc: int) -> None:
    
    robot_queue: set[tuple[int,int]] = set()
    boxes_queue: set[tuple[int,int]] = set()

    for pos in move_list:
        row, col = pos

        if pos in robot:
            robot.remove(pos)
            robot_queue.add((row+dr, col+dc))
        if pos in boxes:
            boxes.remove(pos)
            boxes_queue.add((row+dr, col+dc))

    robot.update(robot_queue)
    boxes.update(boxes_queue)

    return

def calc_big_boxsum(grid: list[list[str]], moves: list[tuple[int,int]]) -> int:
    robot: set[tuple[int,int]] = set()
    walls: set[tuple[int,int]] = set()
    l_boxes: set[tuple[int,int]] = set()
    r_boxes: set[tuple[int,int]] = set()

    initialize_big_sets(grid,robot,walls,l_boxes,r_boxes)
    for move in moves:
        simulate_big_move(robot,walls,l_boxes,r_boxes,move)

    res = 0
    for box in l_boxes:
        row, col = box
        res += 100 * row + col

    return res

def initialize_big_sets(
        grid: list[list[str]], 
        robot: set[tuple[int,int]], 
        walls: set[tuple[int,int]], 
        l_boxes: set[tuple[int,int]],
        r_boxes: set[tuple[int,int]]) -> None:
    
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == "@":
                robot.add((row,col*2))
            elif char == "#":
                walls.add((row,col*2))
                walls.add((row,col*2+1))
            elif char == "O":
                l_boxes.add((row,col*2))
                r_boxes.add((row,col*2+1))
    
    return

def simulate_big_move(
        robot: set[tuple[int,int]], 
        walls: set[tuple[int,int]], 
        l_boxes: set[tuple[int,int]],
        r_boxes: set[tuple[int,int]],
        move: tuple[int,int]) -> None:
    
    move_list: set[tuple[int,int]] = set()
    row, col = next(iter(robot))
    dr, dc = move

    if check_big_move(move_list, walls, l_boxes, r_boxes, row, col, dr, dc):
        do_big_move(move_list, robot, l_boxes, r_boxes, dr, dc)

    return

def check_big_move(
        move_list: set[tuple[int,int]],
        walls: set[tuple[int,int]], 
        l_boxes: set[tuple[int,int]],
        r_boxes: set[tuple[int,int]],
        row: int,
        col: int,
        dr: int,
        dc: int) -> bool:
    # Also updates the move_list with movable objects
    
    move_list.add((row, col))
    if (row+dr, col+dc) in walls:
        return False
    elif (row+dr, col+dc) in l_boxes:
        if dr != 0:
            return (check_big_move(move_list,walls,l_boxes,r_boxes,row+dr,col+dc,dr,dc) 
                    and check_big_move(move_list,walls,l_boxes,r_boxes,row+dr,col+dc+1,dr,dc))
        else:
            return check_big_move(move_list,walls,l_boxes,r_boxes,row+dr,col+dc,dr,dc) 
    elif (row+dr, col+dc) in r_boxes:
        if dr != 0:
            return (check_big_move(move_list,walls,l_boxes,r_boxes,row+dr,col+dc,dr,dc) 
                and check_big_move(move_list,walls,l_boxes,r_boxes,row+dr,col+dc-1,dr,dc))
        else:
            return check_big_move(move_list,walls,l_boxes,r_boxes,row+dr,col+dc,dr,dc) 
    else:
        return True

def do_big_move(
        move_list: set[tuple[int,int]],
        robot: set[tuple[int,int]],
        l_boxes: set[tuple[int,int]],
        r_boxes: set[tuple[int,int]],
        dr: int,
        dc: int) -> None:
    
    robot_queue: set[tuple[int,int]] = set()
    l_boxes_queue: set[tuple[int,int]] = set()
    r_boxes_queue: set[tuple[int,int]] = set()

    for pos in move_list:
        row, col = pos

        if pos in robot:
            robot.remove(pos)
            robot_queue.add((row+dr, col+dc))
        if pos in l_boxes:
            l_boxes.remove(pos)
            l_boxes_queue.add((row+dr, col+dc))
        if pos in r_boxes:
            r_boxes.remove(pos)
            r_boxes_queue.add((row+dr, col+dc))

    robot.update(robot_queue)
    l_boxes.update(l_boxes_queue)
    r_boxes.update(r_boxes_queue)

    return

if __name__ == "__main__":
    input_file_dir = "input.txt"
    grid, moves = read_input(input_file_dir)
    print(calc_boxsum(grid,moves))
    print(calc_big_boxsum(grid,moves))
