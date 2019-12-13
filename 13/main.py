import curses
def run(line, quarters, stdscr):
    num_of_operands = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
    program = [int(x) for x in line]+[0]*10000
    i, base = 0, 0
    output, tiles, score = [], [], 0
    tile_texture, key_values = [" ", "█", "░", "▉","O"], {"a":-1, "s":0, "d":1}
    program[0] = quarters
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
            #program[base_tmp[0]+program[i+1]] = key_values[chr(stdscr.getch())]
            program[base_tmp[0]+program[i+1]] = 0
        elif instruction == 4:
            output.append(operands[0])
            if len(output) == 3:
                if output[0] == -1 and output[1] == 0: 
                    score = output[2]
                    stdscr.addstr(0,0,str(output[2]))
                else:
                    tiles.append(output.copy())
                    stdscr.addstr(1+output[1],output[0], tile_texture[output[2]])
                stdscr.refresh()
                output = []
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
    return tiles, score
with open("input1.txt") as file:
    stdscr = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    result = run(file.readline().split(","), 2, stdscr)
    print(len([x for x in result[0] if x[2] == 2]), result[1],sep="\n")
    curses.endwin()