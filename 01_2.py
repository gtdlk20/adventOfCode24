from collections import Counter

""" input is the same for this problem """

def load_data(path):
    with open(path, 'r') as f:
        data = str(f.read())
        data = data.split('\n')
        return data

def calculate_similarity_score(data):
    x1s, x2s = [], []

    for line in data:
        if len(line) > 0:
            parsed = [int(x.strip()) for x in line.split()]
            x1s.append(parsed[0])
            x2s.append(parsed[1])

    x2_freqs = Counter(x2s)

    return sum(x1 * x2_freqs[x1] for x1 in x1s)


def __main__():
    path = 'files/input01.txt'
    data = load_data(path)
    print(calculate_similarity_score(data))
    


__main__()