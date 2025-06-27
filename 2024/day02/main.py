def read_input(input_file_dir: str) -> list[list[int]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    table: list[list[int]] = []
    for line in lines:
        row: list[str] = line.split()
        int_row: list[int] = [int(n) for n in row]
        table.append(int_row)
    return table

def count_safe(table: list[list[int]]) -> int:
    sum = 0
    for row in table:
        if is_safe(row):
            sum += 1
    return sum
               
def is_safe(row: list[int]) -> bool:
    increasing = False
    decreasing = False

    for i in range(len(row)-1):
        curr = row[i]
        next = row[i+1]

        if next > curr and next - curr <= 3 and not decreasing:
            increasing = True
        elif curr > next and curr - next <= 3 and not increasing:
            decreasing = True
        else:
            return False

    return True

def count_safe_with_dampener(table: list[list[int]]) -> int:
    sum = 0
    for row in table:
        if is_safe_with_dampener(row):
            sum += 1
    return sum

def is_safe_with_dampener(row: list[int]) -> bool:
    for i in range(len(row)):
        if is_safe(row[:i] + row[i+1:]):
            return True
    return False

if __name__ == "__main__":
    table = read_input("input.txt")
    print(count_safe(table))
    print(count_safe_with_dampener(table))