from collections import defaultdict

def read_input(input_file_dir: str) -> list[str]:
    with open(input_file_dir) as f:
        lines = f.read().splitlines()
    
    res: list[str] = []

    for line in lines:
        res.append(line)
    
    return res


def calc_calibration(lines: list[str]) -> int:
    res = 0

    for line in lines:
        num = ""

        for i in range(len(line)):
            if line[i].isdigit():
                num += line[i]
                break

        for i in range(len(line)-1,-1,-1):
            if line[i].isdigit():
                num += line[i]
                break

        if num != "":
            res += int(num)

    return res


def calc_word_calibration(lines: list[str]) -> int:
    res = 0

    words: dict[str, str] = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
        }

    for line in lines:
        digit1 = ""
        loc1 = len(line)+1

        digit2 = ""
        loc2 = -1

        for i in range(len(line)):
            if line[i].isdigit():
                digit1 = line[i]
                loc1 = i
                break

        for word, num in words.items():
            loc = line.find(word)

            if loc >= 0:
                if loc < loc1:
                    digit1 = num
                    loc1 = loc

        for i in range(len(line)-1,-1,-1):
            if line[i].isdigit():
                digit2 += line[i]
                loc2 = i
                break

        for word, num in words.items():
            loc = line.rfind(word)

            if loc >= 0:
                if loc > loc2:
                    digit2 = num
                    loc2 = loc

        res += int(digit1 + digit2)

    return res


if __name__ == "__main__":
    input_file_dir = "input.txt"
    lines = read_input(input_file_dir)
    print(calc_calibration(lines))
    print(calc_word_calibration(lines))