def get_jumps(a, end, planets):
    return [] if a==end else get_jumps(planets[a],end,planets)+[a]
with open("input1.txt") as file:
    pairs = [x.replace("\n","").split(")") for x in file]
    planets = {x[1]:x[0] for x in pairs}
    santa = get_jumps("SAN","COM", planets)
    you = get_jumps("YOU","COM", planets)
    print(sum(len(get_jumps(planet,"COM",planets)) for planet in list(map(lambda x: x[1], pairs))))
    for i in range(min(len(santa),len(you))):
        if santa[i] != you[i]:
            print(len(get_jumps("SAN",santa[i-1], planets))-1+len(get_jumps("YOU",you[i-1], planets))-1)
            break