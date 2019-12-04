def rec_fuel(mass):
    tmp = int(mass/3) - 2
    return (tmp + rec_fuel(tmp)) if tmp > 0 else 0
with open("input1.txt") as file:
    print(sum([int(int(x)/3)-2 for x in file]))
with open("input2.txt") as file:
    print(sum([rec_fuel(int(x)) for x in file]))