import copy


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries


def program_2(data):
    number = int(program_1(25, data))
    start = 0
    sum = 0
    index = 0
    l = 0
    result = []
    while True:
        if sum < number:
            sum += int(data[index])
            index += 1
            l += 1
            print(number, start, l, sum)
        if sum > number:
            sum -= int(data[start])
            start += 1
            l -= 1
            print(number, start, l, sum)
        if sum == number:
            for x in range(start, start+l):
                result.append(int(data[x]))
            return sorted(result)[0] + sorted(result)[-1]


def program_1(index,data):
    start = 0
    end = index
    check = index

    while True:

        if check >= len(data):
            print("error")

        list = []
        for x in range(start, end):
            for y in range(start, end):
                list.append(int(data[x])+int(data[y]))

        # print(start, end, check, data[check])
        if int(data[check]) in list:
            start += 1
            end += 1
            check += 1
        else:
            return data[check]


def main():
    data = open_file("input.txt")
    print(program_2(data))


if __name__ == '__main__':
    main()