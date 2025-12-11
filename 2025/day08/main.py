import sys
import math
import heapq

def read_input(input_file_dir: str) -> list[list[int]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    boxes: list[list[int]] = []

    for line in lines:
        coords = line.split(",")
        boxes.append([int(coords[0]), int(coords[1]), int(coords[2])])

    return boxes


def get_three_largest(boxes: list[list[int]], n_conn: int) -> int:
    distances: list[tuple[int, tuple[int, int]]] = get_distances(boxes)
    circuits_result: tuple[list[set], tuple[int, int]] = make_circuits(distances, n_conn)
    circuits: list[set] = circuits_result[0]
    
    scircuits = sorted(circuits, key=len, reverse=True)

    return len(scircuits[0]) * len(scircuits[1]) * len(scircuits[2])


def get_distances(boxes: list[list[int]]) -> list[tuple]:
    distances: list[tuple] = [] 

    for i in range(len(boxes)):
        for j in range(i+1,len(boxes)):
            box1 = boxes[i]
            box2 = boxes[j]
            heapq.heappush(distances, (get_distance(box1, box2),(i,j)))

    return distances


def get_distance(box1: list[int], box2: list[int]) -> float:
    x1, y1, z1 = box1
    x2, y2, z2 = box2

    return math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)


def make_circuits(distances: list[tuple], n_conn: int) -> tuple[list[set], tuple[int, int]]:
    circuits: list[set] = [{i} for i in range(len(boxes))]
    count = 0

    while n_conn == -1 or count < n_conn:
        _, pair = heapq.heappop(distances)
        box1, box2 = pair

        idx1 = -1
        idx2 = -1

        for i, circuit in enumerate(circuits):
            if box1 in circuit:
                idx1 = i
            if box2 in circuit:
                idx2 = i

        if idx1 == -1 and idx2 != -1:
            circuits[idx2].add(box1)
        elif idx1 != -1 and idx2 == -1:
            circuits[idx1].add(box2)
        elif idx1 != -1 and idx2 != -1 and idx1 != idx2:
            if idx1 < idx2:
                idx1, idx2 = idx2, idx1
            temp1 = circuits.pop(idx1)
            temp2 = circuits.pop(idx2)
            circuits.append(temp1.union(temp2))

        if len(circuits) == 1:
            return circuits, (box1, box2)

        count += 1

    return circuits, (-1,-1)


def get_last_two(boxes: list[list[int]]) -> int:
    distances: list[tuple[int, tuple[int, int]]] = get_distances(boxes)
    circuits_result: tuple[list[set], tuple[int, int]] = make_circuits(distances, -1)
    pair: tuple[int, int] = circuits_result[1]

    return boxes[pair[0]][0] * boxes[pair[1]][0]


if __name__ == "__main__":
    input_file_dir = "input.txt"

    if len(sys.argv) > 1:
        input_file_dir = sys.argv[1]

    if input_file_dir == "input.txt":
        n_conn = 1000
    else:
        n_conn = 10

    boxes = read_input(input_file_dir)
    print(get_three_largest(boxes, n_conn))
    print(get_last_two(boxes))
