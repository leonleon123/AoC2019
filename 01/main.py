def rec_fuel(mass):
    return (int(mass/3)-2 + rec_fuel(int(mass/3)-2)) if int(mass/3)-2 > 0 else 0
with open("input1.txt") as file:
    data = file.readlines()
    print(sum([int(int(x)/3)-2 for x in data]), sum([rec_fuel(int(x)) for x in data]), sep="\n")