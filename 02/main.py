def run(noun, verb, line):
    program = [int(x) for x in line.split(",")]
    program[1]=noun
    program[2]=verb
    for i in range(0,len(program),4):
        if program[i] == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
        elif program[i] == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
        elif program[i] == 99:
            break
    return program
with open("input1.txt") as file:
    program=file.readline()
    print(run(12, 2, program)[0])
    for noun in range(100):
        for verb in range(100):
            if run(noun, verb, program)[0] == 19690720:
                print(f"noun: {noun} verb: {verb}")
                print(100*noun + verb)
                break