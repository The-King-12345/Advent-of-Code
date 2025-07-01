import heapq

def read_input(input_file_dir: str) -> list[tuple[int,int]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()

    incoming = []
    for line in lines:
        row, col = line.split(",")
        incoming.append((int(row),int(col)))

    return incoming

def calc_steps(incoming: list[tuple[int,int]], size: int, fallen: int) -> int:
    walls: set[tuple[int,int]] = set()

    for row, col in incoming[:fallen]:
        walls.add((row,col))

    queue: list[tuple[int,int,int]] = [(0,0,0)]
    seen: set[tuple[int,int]] = {(0,0)}

    while queue:
        step, row, col = heapq.heappop(queue)
        seen.add((row,col))

        if (row,col) == (size-1,size-1):
            return step
        if has_space(row-1,col,size,seen,walls,step,queue):
            heapq.heappush(queue, (step+1, row-1, col))
        if has_space(row+1,col,size,seen,walls,step,queue):
            heapq.heappush(queue, (step+1, row+1, col))
        if has_space(row,col-1,size,seen,walls,step,queue):
            heapq.heappush(queue, (step+1, row, col-1))
        if has_space(row,col+1,size,seen,walls,step,queue):
            heapq.heappush(queue, (step+1, row, col+1))

    return -1

def has_space(row: int, col: int, size: int, seen: set[tuple[int,int]], walls: set[tuple[int,int]], step: int, queue: list[tuple[int,int,int]]) -> bool:
    return (row >= 0 and col >= 0 and row < size and col < size 
            and (row,col) not in seen 
            and (row,col) not in walls
            and (step+1,row,col) not in queue)

def calc_block(incoming: list[tuple[int,int]], size: int) -> str:
    for fallen in range(len(incoming)):
        if calc_steps(incoming, size, fallen) == -1:
            return f"{incoming[fallen-1][0]},{incoming[fallen-1][1]}"
        
    return "None"

if __name__ == "__main__":
    input_file_dir = "input.txt"
    incoming = read_input(input_file_dir)

    if input_file_dir == "input.txt":
        size = 71
        fallen = 1024
    else:
        size = 7
        fallen = 12

    print(calc_steps(incoming, size, fallen))
    print(calc_block(incoming, size))
