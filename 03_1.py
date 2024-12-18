import re

def parse_nums(s):
    nums = re.findall(r"\d+", s)
    return (int(nums[0]), int(nums[1]))

def get_mults(line):
    return [parse_nums(mult) for mult in re.findall(r"mul\(\d+,\d+\)", line)]

def sum_of_prods(data):
    collect = [] 
    for line in data:
        collect.extend(get_mults(line))
    return sum([x*y for x,y in collect])

def load_data(datapath):
    """
    Load data from file.
    """
    with open(datapath, 'r') as f:
        data = str(f.read())
        data = data.split('\n')
        return [line for line in data if len(line) > 0]


def __main__():
    path = 'files/input03.txt'
    data = load_data(path)
    print("loaded data")
    print(sum_of_prods(data))


__main__()