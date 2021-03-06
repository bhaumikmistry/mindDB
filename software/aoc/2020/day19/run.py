def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries


def get_rule_dict(rule):
    def get_num_list(string_data):
        return [n for n in string_data.split(" ") if n]
    rules = {}
    for r in rule:
        lhs = r.split(":")[0]
        rhs = r.split(":")[1]
        val_list = []
        if "|" in rhs:
            for num in rhs.split("|"):
                val_list.append(get_num_list(num))
        elif "\"" in rhs:
            rhs = rhs.replace("\"","")
            val_list.append(get_num_list(rhs))
        else:
            val_list.append(get_num_list(rhs))
        rules[lhs] = val_list
        print(lhs, val_list)
    return rules
        

def get_valid_list(r_dict, key, prefix):
    data = prefix    
    d_l = []
    # print("stack start", r_dict, key, prefix)
    for l in r_dict[key]:
        # print("___Change of l___", data, l)
        data = prefix
        for entry in l:
            # print(key, r_dict[key], l, entry, d_l, data)
            if entry in list(r_dict.keys()):
                # print("->>",key, r_dict[key], l, entry, d_l, data)
                temp_data, temp_d_l = get_valid_list(r_dict, entry, data)
                data = temp_data
                # print("->>>> ", data, temp_data, temp_d_l, d_l)
            else:
                # print(key, r_dict[key], l, entry, d_l, data)
                data = data+entry
        # print(data, d_l)
        d_l.append(data)
        # print("d+e", data, entry)
        # data = ""
    # print("DL", len(d_l), d_l)
    return data, d_l


def program_1(data):
    index = data.index('')
    rule = data[:index]
    validation = data[index+1:]
    print(rule)
    print(validation)
    rule_dict = get_rule_dict(rule)
    print(rule_dict)
    print(get_valid_list(rule_dict, '3', ""))
    print(get_valid_list(rule_dict, '2', ""))

    final = []
    mix = []
    for l in [['4'],['2','3'], ['3','2']]:
        for i in l:
            print(i)
            mix_new = []
            if mix:
                print(mix)
                while mix:
                    x = mix.pop()
                    mix_new.append(get_valid_list(rule_dict, i, x)[1])
                print("mix_new", mix_new)
            mix.extend(get_valid_list(rule_dict, i, "")[1])
        final.extend(mix_new)
        print(mix)
    print(final)

def main():
    ip = open_file("input.txt")
    program_1(ip)


if __name__ == '__main__':
    main()
