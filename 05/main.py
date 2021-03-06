def run(line):
    num_of_operands = [0, 3, 3, 1, 1, 2, 2, 3, 3]
    program = [int(x) for x in line]
    i = 0
    while program[i] != 99:
        modes = [int(x) for x in f"{program[i]:0>5}"[:3]][::-1]
        instruction = int(f"{program[i]:0>5}"[3:])
        operands = [program[i+x+1] if modes[x] else program[program[i+x+1]] for x in range(num_of_operands[instruction])]
        if instruction == 1:
            program[program[i+3]] = operands[0] + operands[1]
        elif instruction == 2:
            program[program[i+3]] = operands[0] * operands[1]
        elif instruction == 3:
            program[program[i+1]] = int(input("input: "))
        elif instruction == 4:
            print(operands[0])
        elif instruction == 5:
            i = (operands[1] - 3) if operands[0]!=0 else i
        elif instruction == 6:
            i = (operands[1] - 3) if operands[0]==0 else i
        elif instruction == 7:
            program[program[i+3]] = int(operands[0] < operands[1])
        elif instruction == 8:
            program[program[i+3]] = int(operands[0] == operands[1])
        i += num_of_operands[instruction] + 1
    return program
with open("input3.txt") as file:
    run(file.readline().split(","))