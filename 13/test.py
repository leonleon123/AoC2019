with open("test_input2.txt") as file:
    data = file.readline().split(",")[2:]
    key_values = [" ", "█", "░", "▉","O"]
    print(*["".join([key_values[int(y)] for y in data[x:x+44]]) for x in range(0,len(data),44)], sep="\n")