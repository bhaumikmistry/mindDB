import copy


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries


def program_2(data):
    visited_list = program_1(data)
    if len(visited_list) is 1:
        return visited_list[0]
    index = 0
    old_data = copy.deepcopy(data)
    while True:
        if index >= len(data) or index < 0:
            return -1
        print(index)
        c, n = data[index]
        if c == "nop":
            print("change ", data[index], ("jmp", n))
            data = copy.deepcopy(old_data)
            data[index] = ("jmp", n)
        elif c == "jmp":
            data = copy.deepcopy(old_data)
            print("change ", data[index], ("nop", n))
            data[index] = ("nop", n)
        else:
            index += 1
            continue
        return_value = program_1(data)
        if len(return_value) is 1:
            print(len(return_value))
            return return_value
        index += 1


def program_1(data):
    index = 0
    acc = 0
    visited = []
    while True:
        if index in visited:
            return visited
        if index < 0 or index >= len(data):
            print("Acc found at ", acc)
            return [acc]
        c, n = data[index]
        if c == "nop":
            visited.append(index)
            index += 1
            continue
        elif c == "acc":
            visited.append(index)
            acc += int(n)
            index += 1
            continue
        elif c == "jmp":
            visited.append(index)
            index += int(n)
            continue
        index += 1


def main():
    data = open_file("input.txt")
    data = [((d.split(" ")[0]),(d.split(" ")[1])) for d in data]
    print(program_2(data))


if __name__ == '__main__':
    main()