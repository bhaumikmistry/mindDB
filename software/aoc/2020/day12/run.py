import copy


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries


def program_1(data):
    dir = ["N", "E", "S", "W", "N", "E", "S", "W", "N", "E", "S", "W"]
    head = "E"

    x, y = 0, 0
    for command in data:
        d, value = command[:1], int(command[1:])
        if d in dir or d == "F":
            if d == "F":
                d = head
            if d == "N":
                y = y + value
            if d == "S":
                y = y + (value*-1)
            if d == "E":
                x = x + value
            if d == "W":
                x = x + (-1*value)
            # print(x, y)
        elif d == "L":
            value /= 90
            i = dir[4:8].index(head)
            head = dir[i-int(value)]
            # print(command, value, dir[i-int(value)], head)
        elif d == "R":
            value /= 90
            i = dir[4:8].index(head)
            head = dir[i+int(value)]
            # print(command, value, dir[i+int(value)], head)
    print(x, y, abs(x)+abs(y))


def program_2(data):
    dir = ["N", "E", "S", "W", "N", "E", "S", "W", "N", "E", "S", "W"]

    wx, wy = 10, 1
    wxd, wyd = "E", "N"

    x, y = 0, 0
    print(x, y, wx, wy, wxd, wyd)
    for command in data:
        d, value = command[:1], int(command[1:])
        if d in dir or d == "F":
            if d == "F":
                if wyd == "N":
                    y = y + value*wy
                if wyd == "S":
                    y = y + (value * -1)*wy
                if wxd == "E":
                    x = x + value*wx
                if wxd == "W":
                    x = x + (-1 * value)*wx
            if d == "N":
                multi = -1 if wyd =="S" else 1
                wy = wy + value * multi
                if wy < 0:
                    wyd = dir[dir.index(wyd)+2]
                    wy = abs(wy)
            if d == "S":
                multi = -1 if wyd =="N" else 1
                wy = wy + (value) * multi
                if wy < 0:
                    wyd = dir[dir.index(wyd)+2]
                    wy = abs(wy)
            if d == "E":
                multi = -1 if wyd =="W" else 1
                wx = wx + value * multi
                if wx < 0:
                    wxd = dir[dir.index(wxd)+2]
                    wx = abs(wx)
            if d == "W":
                multi = -1 if wyd =="E" else 1
                wx = wx + (value) * multi
                if wx < 0:
                    wxd = dir[dir.index(wxd)+2]
                    wx = abs(wx)
            print(d, value, x, y, wx, wy, wxd, wyd)
        elif d == "L":
            value /= 90
            i = dir[4:8].index(wxd)
            wxd = dir[i-int(value)]
            i = dir[4:8].index(wyd)
            wyd = dir[i-int(value)]
            if value == 1 or value == 3:
                wxd, wyd = wyd, wxd
                wx, wy = wy, wx
            print(d, value, wxd, wyd)
        elif d == "R":
            value /= 90
            i = dir[4:8].index(wxd)
            wxd = dir[i + int(value)]
            i = dir[4:8].index(wyd)
            wyd = dir[i + int(value)]
            if value == 1 or value == 3:
                wxd, wyd = wyd, wxd
                wx, wy = wy, wx
            print(d, value, wxd, wyd)
        # input("")
    print(x, y, abs(x)+abs(y))





def main():
    data = open_file("input.txt")
    program_2(data)


if __name__ == '__main__':
    main()