import re

def parse_nums(s):
    nums = re.findall(r"\d+", s)
    return (int(nums[0]), int(nums[1]))

def get_commands(line):
    commands = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
    flag = True
    collect = []
    for command in commands:
        if command == "do()":
            flag = True
        elif command == "don't()":
            flag = False
        elif flag:
            collect.append(parse_nums(command))

    return collect

def sum_of_prods(data):
    collect = [] 
    collect.extend(get_commands(data))
    print(collect)
    return sum([x*y for x,y in collect])

def load_data(datapath):
    """
    Load data from file.
    """
    with open(datapath, 'r') as f:
        data = str(f.read())
        data = data.split('\n')
        return ' '.join([line for line in data if len(line) > 0])


def __main__():
    path = 'files/input03.txt'
    data = load_data(path)
    print("loaded data")
    print(sum_of_prods(data))


__main__()