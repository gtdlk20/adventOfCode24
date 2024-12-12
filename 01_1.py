

def sorted_distance(datapath):
    """
    datapath: string
    return: int
    """

    #load data
    with open(datapath, 'r') as f:

        # cast to string
        data = str(f.read())
        # split  by new line
        data = data.split('\n')
        # init collect lists to be sorted
        x1s, x2s = [], []

        # I know I should consolodate split calls but it's late and eaasier to read this way
        for line in data:
            # some lines don't contain any data.
            if len(line) > 0:
                # splot lines and cast to int
                parsed = [int(x.strip()) for x in line.split()]
                x1s.append(parsed[0])
                x2s.append(parsed[1])
        
        x1s.sort()
        x2s.sort()

        # do the math
        return sum(abs(x1 - x2) for x1, x2 in zip(x1s, x2s))
            



def __main__():
    path = 'files/input01.txt'
    print(sorted_distance(path))

__main__()