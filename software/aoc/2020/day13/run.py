import copy
import math as m


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries


def program_2(data):
    t = int(data[0])
    b = data[1].split(",")
    bus = [int(num) for num in b if num != 'x' ]
    busindex = [b.index(str(bs)) for bs in bus]
    print(t, bus, busindex)
    base_time = 100000000000000
    lcm = 1
    for offset, bus in enumerate(b):
        if bus != "x":
            bus = int(bus)
            while (base_time  + offset) % bus != 0:
                base_time += lcm
            lcm *= bus
        print(bus, offset, lcm)
    return base_time


def program_1(data):
    t = int(data[0])
    b = data[1]
    bus = [int(num) for num in data[1].split(",") if num != 'x' ]
    print(t, bus)

    closests = t*2
    cb = 0
    for b in bus:
        div = m.floor(t/b)
        if closests > (div+1)*b:
            closests=(div+1)*b
            cb = b
        print(t, b, closests, div, (div+1)*b)

    print((closests-t)*cb)




def main():
    data = open_file("input.txt")
    print(program_2(data))


if __name__ == '__main__':
    main()
