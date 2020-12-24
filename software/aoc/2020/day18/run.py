def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries

def solver(d):
    sum = 0
    while True:
        d_list = d.split(" ")
        if len(d_list) == 1:
            sum += int(d_list[0])
            # print("ans:", d_list[0])
            break
        new = 0
        if d_list[1] == "+":
            new = int(d_list[0]) + int(d_list[2])
        else:
            new = int(d_list[0]) * int(d_list[2])
        d_new_list = [str(new)] + d_list[3:]
        d = " ".join(d_new_list)
        # print(d_list[0], d_list[1], d_list[2], new, d, len(d))
    return sum


def solver2(d):
    d_list = d.split(" ")
    
    while True:
        if "+" in d_list:
            sign = d_list.index("+")
            sum = int(d_list[sign-1]) + int(d_list[sign+1])
            d_list = d_list[:sign-1] + [str(sum)] + d_list[sign+2:]
            print(d_list)
        else:
            return solver(" ".join(d_list))

def reduce_parentheses(d):
    inner_par = []
    start_index = 0
    end_index = 0 
    while True:
        d_list = d.split(" ")
        start_cover = ""
        end_cover = ""
        for index, d_val in enumerate(d_list):
            if d_val.startswith("("):
                while d_val.count("(") > 1:
                    start_cover += "("
                    d_val = d_val[1:]
                # print(d_val, " with ", d_val.count("("), "start_cover", start_cover)
                start_index = index
                inner_par = [d_val[1:]]
            elif d_val.endswith(")"):
                while d_val.count(")") > 1:
                    end_cover += ")"
                    d_val = d_val[:-1]
                end_index = index
                inner_par.append(d_val[:-1])
                new_val = solver2(" ".join(inner_par))
                new_str = start_cover + str(new_val) + end_cover
                # print("here:", new_str, " for ", inner_par)
                d_list = d_list[:start_index] + [new_str] + d_list[end_index+1:] 
                d = " ".join(d_list)

                break
            elif len(inner_par) > 0:
                inner_par.append(d_val)
            if d.count("(") < 1 and d.count(")") < 1:
                final = solver2(d)
                # print("final:", final)
                return final
        # print(d, inner_par, start_index, end_index)



def program_1(data):
    # print(data)
    sum = 0
    for d in data:
        if d.count("(") > 0 or d.count(")") > 0 :
            # print("found ( or )")
            sum += reduce_parentheses(d)
        else:
            sum += solver2(d)
                
    print("Sum:", sum)


def main():
    ip = open_file("input.txt")
    program_1(ip)


if __name__ == '__main__':
    main()
