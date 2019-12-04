def get_lines(wire):
    directions = {"U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}
    tmp = [[0,0],[0,0]]
    lines = []
    for move in wire:
        tmp[0] = tmp[1].copy()
        tmp[1][0] = tmp[1][0]+directions[move[0]][0]*int(move[1:])
        tmp[1][1] = tmp[1][1]+directions[move[0]][1]*int(move[1:])
        lines.append([tmp[0].copy(), tmp[1].copy()])
    return lines

def intersects(w1, w2):
    vector1 = [w1[1][0]-w1[0][0],w1[1][1]-w1[0][1]]
    vector2 = [w2[1][0]-w2[0][0],w2[1][1]-w2[0][1]]
    if vector1[0]*vector2[0]+vector1[1]*vector2[1] == 0:
        if vector1[1] == 0:
            if  w2[0][0] <= max(w1[0][0],w1[1][0]) and w2[0][0] >= min(w1[0][0],w1[1][0])\
            and w1[0][1] <= max(w2[0][1],w2[1][1]) and w1[0][1] >= min(w2[0][1],w2[1][1]):
                return [w2[0][0],w1[0][1]]
        elif vector1[0] == 0:
            if  w1[0][0] <= max(w2[0][0],w2[1][0]) and w1[0][0] >= min(w2[0][0],w2[1][0])\
            and w2[0][1] <= max(w1[0][1],w1[1][1]) and w2[0][1] >= min(w1[0][1],w1[1][1]):
                return [w1[0][0],w2[0][1]]

with open("input3.txt") as file:
    wire1 = file.readline().split(",")
    wire2 = file.readline().split(",")
    wire1_lines = get_lines(wire1)
    wire2_lines = get_lines(wire2)
    intersections = []
    steps_list = []
    for i in range(len(wire1_lines)):
        for j in range(len(wire2_lines)):
            tmp = intersects(wire1_lines[i],wire2_lines[j])
            if tmp and tmp[0]!=0 and tmp[1]!=0:
                intersections.append(tmp)
                steps = sum(int(x[1:]) for x in wire1[:i])+sum(int(x[1:]) for x in wire2[:j])
                steps +=abs(tmp[0]-wire1_lines[i][0][0])+abs(tmp[1]-wire1_lines[i][0][1])+\
                        abs(tmp[0]-wire2_lines[j][0][0])+abs(tmp[1]-wire2_lines[j][0][1])
                steps_list.append(steps)
    print(min(steps_list))
    print(min(abs(x[0])+abs(x[1]) for x in intersections))
