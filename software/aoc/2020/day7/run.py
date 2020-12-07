

def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries


def program_2(data):
    bags_check = ["shiny gold"]
    count_bag = {}
    count_bag_list = list()
    count = 0
    total = {}
    for bag in bags_check:
        for d in data:
            if bag in d.split("contain ")[0]:
                other_half = d.split("contain ")[1]
                total[bag] = 0
                count_bag[bag] = []
                for pair in other_half.split(", "):
                    bag_name = pair.split(" ", 1)[1]
                    num = int(pair.split(" ", 1)[0]) if (pair.split(" ", 1)[0]).isdigit() else (0 if "no" in pair.split(" ", 1)[0] else 1)
                    count += num
                    total[bag] += num
                    bag_to_add = bag_name.split(" bag")[0]
                    count_bag[bag] += [bag_to_add] * num
                    count_bag_list += [bag_to_add] * num
                    print(bag, d, count, bag_to_add)
                    bags_check.append(bag_to_add)
                    num = 0
    print(bags_check)
    print(total)
    print(count_bag)
    print(count_bag_list)

    def get_bag(bag):
        add = len(count_bag.get(bag, []))
        for b in count_bag.get(bag, []):
            add += get_bag(b)
        return add

    add = get_bag("shiny gold")
    print(add)


def program_1(data):
    bags_check = ["shiny gold"]
    for bag in bags_check:
        for d in data:
            if bag in d.split("contain")[0]:
                bag_to_add = d.split(" bag")[0]
                bags_check.append(bag_to_add)
                print(bag, d, bag_to_add)
    print(len(set(bags_check))-1)


def main():
    data = open_file("input.txt")
    program_2(data)


if __name__ == '__main__':
    main()




