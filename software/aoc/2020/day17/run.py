def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [[list(e) for e in entry.split('\n')[0]] for entry in f.readlines()]
        return entries

def get_value(x,y,z, data):
    if -1 < z < len(data[0]):
        if -1 < y < len(data[z][0]):
            if -1 < x < len(data[z][y][0]):
                return data[z][y][x]
    return "."


def get_neighbors(x,y,z,data):
    neighbors = []
    for zz in [0,1,2]:
        for yy in [0,1,2]:
            for xx in [0,1,2]:
                neighbors.append(get_value(x,y,z,data))

def program_1(data):
    z = 1
    for y in range(len(data[z])):
        for x in range(len(data[z][y])):
            print(data[z][y],data[z][y][x])


def main():
    ip = open_file("input.txt")
    ip = [[], ip, []]
    print(ip)
    program_1(ip)


if __name__ == '__main__':
    main()
