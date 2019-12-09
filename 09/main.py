def run(line):
    num_of_operands = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
    program = [int(x) for x in line]+[0]*10000
    i = 0
    base = 0
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
            program[base_tmp[0]+program[i+1]] = int(input("input: "))
        elif instruction == 4:
            print(operands[0])
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
    return program
with open("input1.txt") as file:
    run(file.readline().split(","))