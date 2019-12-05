num_of_operands = [0, 3, 3, 1, 1, 2, 2, 3, 3]
def run(line):
    program = [int(x) for x in line]
    i = 0
    instruction = program[0]
    while instruction != 99:
        modes = [int(x) for x in f"{program[i]:0>5}"[:3]][::-1]
        instruction = int(f"{program[i]:0>5}"[3:])
        if instruction == 99: break
        operands = [program[i+x+1] if modes[x] else program[program[i+x+1]] for x in range(num_of_operands[instruction])]
        if instruction == 1:
            program[program[i+3]] = operands[0] + operands[1]
            i += 4
        elif instruction == 2:
            program[program[i+3]] = operands[0] * operands[1]
            i += 4
        elif instruction == 3:
            program[program[i+1]] = int(input("input"))
            i += 2
        elif instruction == 4:
            print(operands[0])
            i += 2
        elif instruction == 5:
            i = operands[1] if operands[0]!=0 else (i + 3)
        elif instruction == 6:
            i = operands[1] if operands[0]==0 else (i + 3)
        elif instruction == 7:
            program[program[i+3]] = int(operands[0] < operands[1])
            i += 4
        elif instruction == 8:
            program[program[i+3]] = int(operands[0] == operands[1])
            i += 4
    return program
with open("input3.txt") as file:
    run(file.readline().split(","))