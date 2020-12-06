# --- Day 5: Binary Boarding ---
import math


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries


def validate(letter, lower, upper):
    if letter in ['F', 'L']:
        return lower, lower+int(math.ceil((upper-lower)/2))
    else:
        return lower+int(math.floor(1+(upper - lower)/2)), upper


def program_1(data):
    lower = 0
    upper = 127
    for letter in data[:7]:
        lower, upper = validate(letter, lower, upper)
    row = lower
    lower = 0
    upper = 7
    for letter in data[7:]:
        lower, upper = validate(letter, lower, upper)
    column = lower
    return row * 8 + column


def main():
    data = open_file("input.txt")
    seat_id = 0
    seat_list = []
    for string in data:
        id = program_1(string)
        seat_list.append(id)
        if id > seat_id:
            seat_id = id
    print("result_1", seat_id)
    seat_list.sort()
    x = seat_list[0]
    for y in seat_list[1:-1]:
        if x+1 == y:
            x = y
        else:
            print("result", x+1)
            break


if __name__ == '__main__':
    main()
