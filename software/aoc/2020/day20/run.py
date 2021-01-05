def open_file(file_path):
    with open(file_path, 'r') as f:
        entries = [entry.split('\n')[0] for entry in f.readlines()]
        return entries


def program_1(data):
    blocks = {}
    single = []
    for line in data:
        if line == "":
            blocks.append(single)
            single=[]
            continue
        single.append(line)
    print(*blocks, sep="\n")

    cols = []
    candidate = blocks[0]
    while True:


            
        

def match_top():
    return True:

def main():
    ip = open_file("input.txt")
    program_1(ip)


if __name__ == '__main__':
    main()
