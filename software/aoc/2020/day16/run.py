def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries


def program_1(cat, ticket_val):
    sum = 0
    for v in ticket_val:
        if v in cat:
            continue
        else:
            sum += v
    return(sum)

def get_cat_vector(data):
    vec = []
    for d in data:
        d = d.split(' ')
        range_1 = (int(d[1].split("-")[0]),int(d[1].split("-")[1]))
        vec.extend([x for x in range(range_1[0],range_1[1]+1)])
        range_1 = (int(d[3].split("-")[0]),int(d[3].split("-")[1]))
        vec.extend([x for x in range(range_1[0],range_1[1]+1)])
        vec = list(set(vec))
    # print(vec)
    return vec


def get_ticket_value(data):
    vec = []
    for d in data:
        d = d.split(',')
        vec.extend([int(x) for x in d])
    print(vec)
    return vec

def main1():
    cat = open_file("cat.txt")
    other_tkt = open_file("other_tkt.txt")
    # print(cat, other_tkt)
    v_cat = get_cat_vector(cat)
    v_tkt = get_ticket_value(other_tkt)
    print(program_1(v_cat, v_tkt))


def get_cat(data):
    cat = {}
    vec = []
    for d in data:
        d = d.split(' ')
        cat_name = d[0]
        range_1 = (int(d[1].split("-")[0]),int(d[1].split("-")[1]))
        vec.extend([x for x in range(range_1[0],range_1[1]+1)])
        range_1 = (int(d[3].split("-")[0]),int(d[3].split("-")[1]))
        vec.extend([x for x in range(range_1[0],range_1[1]+1)])
        vec = list(set(vec))
        cat[cat_name] = vec
        vec = []
    return cat


def get_tickets(data):
    vec = []
    cat = get_cat_vector(open_file("cat.txt"))
    for d in data:
        d = d.split(',')
        current_ticket = [int(x) for x in d]
        sum = 0
        for v in current_ticket:
            if v in cat:
                continue
            else:
                sum += v
        if sum == 0:
            vec.append([int(x) for x in d]) 
    print(f'OG: {len(data)} New: {len(vec)}')
    return vec


def get_cat_list(cat_dict, ticket_vec):
    count = [[]]* len(ticket_vec[0])
    print("start", count)
    for l in range(len(ticket_vec[0][0])):
        for w in range(len(ticket_vec)):
            cat_mask = count[w]
            cat_list_for_val = []
            for name, numbers in cat_dict.items():
                if ticket_vec[l][w] in numbers:
                    cat_list_for_val.append(name)
            # count[w] = list(set(cat_mask).intersection(cat_list_for_val))
            count[w] = cat_list_for_val
        # if len(count[w]) == 1:
        #     intersection = count[w][0]
        #     for keys in count:
        #         if intersection in keys:
        #             keys.remove(intersection)
        #     count[w] = [intersection]
        print(f'at {w} of {len(ticket_vec[0])}')
    print(count)
    return count



def main():
    cat = open_file("cat.txt")
    other_tkt = open_file("other_tkt.txt")
    cat_dict = get_cat(cat)
    ticket_vec = get_tickets(other_tkt)
    # print(cat_dict)
    # print(ticket_vec)
    cat_list = get_cat_list(cat_dict,ticket_vec)
    print(len(cat_list), cat_list)
    result = 1
    my_ticket = [157,73,79,191,113,59,109,61,103,101,67,193,97,179,107,89,53,71,181,83]
    print(len(my_ticket),my_ticket)
    for index, cat in enumerate(cat_list):
        print(index, cat)
    

    # for index, cat in enumerate(cat_list):
        # if cat[0].startswith("departure"):
            # result += my_ticket[index]

    

if __name__ == '__main__':
    main()
