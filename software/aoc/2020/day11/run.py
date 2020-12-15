import copy


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [[ seat for seat in entry.split('\n')[0]] for entry in f.readlines()]
        return entries


def getl(data, index):
    if -1 < index < len(data):
        return data[index]
    return False


def getw(data, index):
    if -1 < index < len(data):
        return data[index]
    return False


def check_surround_2(data, l, w, seat):
    occupied = 0
    for ll in [-1, 0, 1]:
        for ww in [-1, 0, 1]:
            if getl(data, l + ll):
                if getw(data[l + ll], w + ww) == ".":
                    ogll = copy.deepcopy(ll)
                    ogww = copy.deepcopy(ww)
                    while True:
                        ogll += ll
                        ogww += ww
                        if getl(data, l + ogll) and getw(data[l + ogll], w + ogww):
                            if getw(data[l + ogll], w + ogww) == ".":
                                # print(data[l][w], l, w, getw(data[l + ogll], w + ogww), l + ogll, w + ogww)
                                continue
                            if getw(data[l + ogll], w + ogww) == "L":
                                # print(data[l][w], l, w, getw(data[l + ogll], w + ogww), l + ogll, w + ogww)
                                break
                            if getw(data[l + ogll], w + ogww) == "#":
                                # print(data[l][w], l, w, getw(data[l + ogll], w + ogww), l + ogll, w + ogww)
                                occupied+=1
                                break
                        else:
                            break
                elif getw(data[l + ll], w + ww) == "L":
                    continue
                elif getw(data[l + ll], w + ww) == "#":
                    occupied += 1

    if occupied > 4:
        return "L"
    return "#"



def check_surround(data, l, w, seat):
    occupied = 0
    for ll in [-1, 0, 1]:
        for ww in [-1, 0, 1]:
            if getl(data, l+ll):
                # print(l, ll, w, ww)
                if not(getw(data[l+ll], w+ww) == "." or getl(data[l+ll], w+ww) == "L"):
                    if seat == "L" or seat == "#" and occupied>3:
                        return "L"
                    if seat == "#" and occupied<4:
                        occupied+=1
    return "#"


def count_occupied(map):
    count = 0
    for l in map:
        for w in l:
            if w == "#":
                count += 1
    return count


def program_1(data):
    L = len(data)
    W = len(data[0])
    last = copy.deepcopy(data)
    while True:
        newData = copy.deepcopy(data)
        for l in range(L):
            for w in range(W):
                seat = data[l][w]
                if not(seat == "."):
                    newData[l][w] = check_surround_2(data, l, w, seat)
                    print(l, w, seat, newData[l][w])
        

        for x in newData:
            print(*x, sep='')
        print("-"*10)
        data = copy.deepcopy(newData)

        count = 0
        for r in data:
            if r in last:
                count+=1
        # print(count, len(data))
        if count == len(data):
            print("SAAMMEE")
            print(count_occupied(data))
            break
        last = copy.deepcopy(newData)




def main():
    data = open_file("input.txt")
    program_1(data)


if __name__ == '__main__':
    main()
