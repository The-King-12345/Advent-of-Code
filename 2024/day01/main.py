def read_input(input_file_dir: str) -> tuple[list[int], list[int]]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    list1: list[int] = []
    list2: list[int] = []
    for line in lines:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))
    return list1, list2

def calc_distance(list1: list[int], list2: list[int]) -> int:
    list1 = sorted(list1)
    list2 = sorted(list2)

    sum = 0
    for i in range(len(list1)):
        sum += abs(list1[i] - list2[i])
    return sum

def calc_similarity(list1: list[int], list2: list[int]) -> int:
    freq: dict[int, int] = {}
    for num in list2:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    sum = 0
    for num in list1:
        if num in freq:
            sum += num * freq[num]
    return sum

if __name__ == "__main__":
    list1, list2 = read_input("input.txt")
    print(calc_distance(list1, list2))
    print(calc_similarity(list1, list2))

