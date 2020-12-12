import copy


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [int(entry.split('\n')[0]) for entry in f.readlines()]
        return entries


def find_twos(value, index, data):
    if index+2 >= len(data):
        return False
    print(data[index:index+2])
    if value+1 == data[index+1] and value+2 == data[index+2]:
        return True
    return False


def find_threes(value, index, data):
    if index+3 >= len(data):
        return False
    print(data[index:index+3])
    if value+1 == data[index+1] and value+2 == data[index+2] and value+3 == data[index+3]:
        return True
    return False


def program_1(data):
    data.append(0)
    data = sorted(data)
    data.append(data[-1]+3)
    print(data)
    index = 1
    jolt = 0
    ones = 0
    twos = 0
    threes = 0
    result_3 = 0
    result_2 = 0
    while True:
        if data[index] == jolt+1:
            if find_threes(data[index], index, data):
                result_3 += 1
                index+=3
            elif find_twos(data[index], index, data):
                result_2 += 1
                index+=2
            jolt = data[index]
            ones += 1
            continue
        elif data[index] == jolt+2:
            if find_threes(data[index], index, data):
                result_3 += 1
            elif find_twos(data[index], index, data):
                result_2 += 1
            jolt = data[index]
            twos += 1
        elif data[index] == jolt+3:
            if find_threes(data[index], index, data):
                result_3 += 1
                index+=3
            elif find_twos(data[index], index, data):
                result_2 += 1
                index+=2
            jolt = data[index]
            threes += 1
            continue
        index+=1
        if index >= len(data):
            print(ones, threes, result_2, result_3)
            return ones * threes


def solution(inp):
    inp.append(0)
    inp = sorted(inp)
    inp.append(max(inp)+3)

    obl = set([0])
    for x, y in zip(inp, inp[1:]):
        if y - x == 3:
            obl.add(x)
            obl.add(y)
    tot = 1
    obl = list(sorted(obl))
    for o, oo in zip(obl, obl[1:]):
        c = inp.index(oo) - inp.index(o) - 1
        if oo - o > 3:
            tot *= 2**c - (oo-o)//3
        else:
            tot *= 2**c
    return tot


def main():
    data = open_file("input.txt")
    print(solution(data))


if __name__ == '__main__':
    main()

