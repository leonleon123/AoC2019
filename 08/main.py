def apply_layer(a,b):
    for i in range(6):
        for j in range(25):
            a[i][j] = b[i][j] if a[i][j] == "2" else a[i][j]
with open("input1.txt") as file:
    a=file.readline()
    data=[a[x:x+150] for x in range(0,len(a),150)]
    layers = list(map(lambda x: [list(x[i:i+25]) for i in range(0,len(x),25)], data))
    [apply_layer(layers[0], layers[i]) for i in range(int(len(a)/150))]
    print(list(map(lambda x: x.count("1")*x.count("2"), sorted(data, key=lambda x: x.count("0"))))[0])
    print(*[" ".join(line).replace("0",".") for line in layers[0]],sep="\n")
