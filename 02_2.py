def is_increasing(sequence):
    """Check if sequence is increasing."""
    for i in range(1, len(sequence)):
        if sequence[i] - sequence[i-1] not in [1,2,3]:
            return False
    return True


def is_decreasing(sequence):
    """Check if sequence is decreasing."""
    for i in range(1, len(sequence)):
        if sequence[i] - sequence[i-1] not in [-1,-2,-3]:
            return False
    return True

def is_safe(sequence):
    return is_increasing(sequence) or is_decreasing(sequence)

def is_dropout_safe(sequence):
    """
    Check if sequence is exclusively increasing/decreasing 
    and if deltas are between 1 and 3 for an
    y consecutive pair of elements.
    """
    if not is_safe(sequence):
        for i in range(len(sequence)):
            new_seq = sequence[:i] + sequence[i+1:]
            if is_safe(new_seq):
                return True
        return False
    else:
        return True


def count_arrangements(sequences):
    """
    Count the number of sequences
    that are safe.
    """
    return sum(is_dropout_safe(sequence) for sequence in sequences)


def load_data(datapath):
    """
    Load data from file.
    """
    with open(datapath, 'r') as f:
        data = str(f.read())
        data = data.split('\n')
        return [[int(x) for x in line.split()] for line in data if len(line) > 0]


def __main__():
    path = 'files/input02.txt'
    data = load_data(path)
    print("loaded data")
    print(count_arrangements(data))


__main__()

