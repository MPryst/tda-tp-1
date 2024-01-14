import sys
import csv
import functools 

def alg_sort(x, y):
    if x[1] > y[1]:
        return -1
    elif x[1] < y[1]:
        return 1
    else:
        if x[0] < y[0]:
            return -1
        elif x[0] > y[0]:
            return 1
        else:
            return 0

def algorithm(data):
    data = sorted(data, key=functools.cmp_to_key(alg_sort))
    print(data)
    S = 0
    A = 0
    for s, a in data:
        S += s
        f = S + a
        if f > A:
            A = f 
    print(A)
    return A

def load(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        data = []
        for row in reader:
            data.append((int(row[0]), int(row[1])))
    return data

def main():
    filename = sys.argv[1]
    data = load(filename)
    d = algorithm(data)
main()