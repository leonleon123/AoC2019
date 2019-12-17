def run(line, parameter):
    num_of_operands = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
    program = [int(x) for x in line]+[0]*10000
    i, base = 0, 0
    field,x,y = [[""]*50 for _ in range(48)], 0, 0
    program[0] = parameter
    #did it by hand lol
    input_data, input_data_i= [\
        65, 44, 66, 44, 65, 44, 66, 44, 65, 44, 67, 44, 65, 44, 67, 44, 66, 44, 67, 10, \
        82, 44, 54, 44, 76, 44, 49, 48, 44, 82, 44, 49, 48, 44, 82, 44, 49, 48, 10,\
        76, 44, 49, 48, 44, 76, 44, 49, 50, 44, 82, 44, 49, 48, 10,\
        82, 44, 54, 44, 76, 44, 49, 50, 44, 76, 44, 49, 48, 10, 110, 10], 0
    while program[i] != 99:
        modes = [int(x) for x in f"{program[i]:0>5}"[:3]][::-1]
        instruction = int(f"{program[i]:0>5}"[3:])
        base_tmp = [base if modes[x]==2 else 0 for x in range(num_of_operands[instruction])]
        operands = [program[i+x+1] if modes[x]==1 else program[base_tmp[x]+program[i+x+1]] for x in range(num_of_operands[instruction])]
        if instruction == 1:
            program[base_tmp[2]+program[i+3]] = operands[0] + operands[1]
        elif instruction == 2:
            program[base_tmp[2]+program[i+3]] = operands[0] * operands[1]
        elif instruction == 3:
            program[base_tmp[0]+program[i+1]] = input_data[input_data_i]
            input_data_i += 1
        elif instruction == 4:
            if parameter == 1:
                field[x][y] = chr(operands[0])
                if operands[0] == 10:
                    x += 1  
                    y = 0 
                else:
                    y += 1
            else:
                print(chr(operands[0]),end="") if operands[0]<256 else print(operands[0])
        elif instruction == 5:
            i = (operands[1] - 3) if operands[0]!=0 else i
        elif instruction == 6:
            i = (operands[1] - 3) if operands[0]==0 else i
        elif instruction == 7:
            program[base_tmp[2]+program[i+3]] = int(operands[0] < operands[1])
        elif instruction == 8:
            program[base_tmp[2]+program[i+3]] = int(operands[0] == operands[1])
        elif instruction == 9:
            base += operands[0]
        i += num_of_operands[instruction] + 1
    return field
with open("input1.txt") as file:
    data = file.readline().split(",")
    field = run(data, 1)
    pos,intersections = [12,0],[]
    for i in range(1,len(field)):
        for j in range(1,len(field[i])-1):
            if all(field[i+x][j+y]=="#" for x,y in [(0,0),(0,1),(0,-1),(1,0),(-1,0)]):
                intersections.append((i,j))
    print(sum(map(lambda el: el[0]*el[1], intersections)))
    directions, d, counter = [[(0,1),(0,-1)],[(1,0),(-1,0)]], [0,0], 0
    path = []
    moves =  {"0110":"R","01-10":"L","0-110":"L","0-1-10":"R","1001":"L","100-1":"R","-1001":"R","-100-1":"L"}
    tmp_move = ["R"]
    while field[pos[0]][pos[1]] != ".":
        pos = [pos[0] + directions[d[0]][d[1]][0], pos[1] + directions[d[0]][d[1]][1]]
        if field[pos[0]+directions[d[0]][d[1]][0]][pos[1]+directions[d[0]][d[1]][1]] != "#":
            tmp = directions[d[0]][d[1]]
            d[0] = (d[0] + 1) % 2
            d[1] = int(field[pos[0]+directions[d[0]][1][0]][pos[1]+directions[d[0]][1][1]] == "#")
            tmp_move.append(moves[f"{tmp[0]}{tmp[1]}{directions[d[0]][d[1]][0]}{directions[d[0]][d[1]][1]}"])
            path.append(tmp_move.pop(0)+str(counter+1))
            counter = 0
        else:
            counter+=1
    print(path)
    run(data, 2)