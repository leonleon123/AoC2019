from numpy import dot, absolute, cumsum
def generate_matrix(n):
    repeat = [0,1,0,-1]
    return [[repeat[int((j+1)/(i+1))%len(repeat)] for j in range(n)] for i in range(n)]
with open("input1.txt") as file:
    num1 = [int(x) for x in file.readline().replace("\n","")]
    num2 = num1 * 10000
    matrix1 = generate_matrix(len(num1))
    for i in range(100):
        num1 = absolute(dot(matrix1,num1)) % 10
    print("".join(str(x) for x in num1[:8]))
    offset = int("".join(str(x) for x in num2[:7]))
    for i in range(100):
        num2 = absolute(cumsum(num2[::-1])[::-1]) % 10
    print("".join(str(x) for x in num2[offset:offset+8]))
