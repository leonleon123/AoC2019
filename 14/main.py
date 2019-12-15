from math import ceil
def produce(amount, chemical, recipes):
    if chemical == "ORE":
        return amount
    if amount <= recipes[chemical][2]:
        recipes[chemical][2] -= amount
        return 0
    if amount > recipes[chemical][2]:
        amount -= recipes[chemical][2]
        recipes[chemical][2] = 0
    batches = ceil(amount / recipes[chemical][0])
    recipes[chemical][2] += batches*recipes[chemical][0] - amount
    return sum(produce(batches*recipes[chemical][1][ch], ch, recipes) for ch in recipes[chemical][1])
with open("input1.txt") as file:
    data = [line.replace("\n","").split(" => ") for line in file]
    recipes = {x[1].split(" ")[1]:[int(x[1].split(" ")[0]),{y.split(" ")[1]:int(y.split(" ")[0]) for y in x[0].split(", ")}, 0] for x in data}
    print(produce(1, "FUEL", recipes))
    i = 2371600 # brute forced / guessed around in which ballpark my number is
    while produce(i+1, "FUEL", recipes) < 1000000000000:
        recipes = {x[1].split(" ")[1]:[int(x[1].split(" ")[0]),{y.split(" ")[1]:int(y.split(" ")[0]) for y in x[0].split(", ")}, 0] for x in data}
        i+=1
    print(i)