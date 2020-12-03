# --- Day 3: Toboggan Trajectory ---


def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [list(entry.split('\n')[0]) for entry in f.readlines()]
        return entries


def program_1(data, move_right, move_down):
    length = len(data)
    width = len(data[0])
    tree_count = 0
    w = 0
    l = 0
    while l < length:
        w += move_right
        l += move_down
        w = w - width if w >= width else w
        if l >= length:
            break
        if data[l][w] == "#":
            tree_count += 1
    return tree_count


def main():
    data = open_file("input.txt")
    result = 1
    for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        result *= program_1(data, x, y)
    print(result)


if __name__ == '__main__':
    main()
