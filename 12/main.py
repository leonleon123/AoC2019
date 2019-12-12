import numpy as np
def get_velocity(data, vec_idx):
    return [sum(int(data[vec_idx][x]<data[i][x])-int(data[vec_idx][x]>data[i][x]) for i in range(len(data)) if i != vec_idx) for x in range(3)]
with open("input1.txt") as file:
    moons = [[int(x[2:]) for x in line.replace("\n", "")[1:-1].split(", ")] for line in file]
    velocity, total_energy = [[0]*3 for _ in range(len(moons))], 0
    states, periods, i = [list(map(lambda x: x[i], moons+velocity)) for i in range(3)], [0 for _ in range(3)], 0
    while True:
        if all(x>0 for x in periods): break
        for idx in range(3): periods[idx] = i if states[idx]==list(map(lambda x: x[idx], moons+velocity)) and periods[idx]==0 else periods[idx]
        tmp_velocity = [get_velocity(moons, idx) for idx in range(len(moons))]
        velocity = [[velocity[idx][v]+tmp_velocity[idx][v] for v in range(3)] for idx in range(len(moons))]
        moons = [[moons[idx][v]+velocity[idx][v] for v in range(3)] for idx in range(len(moons))]
        print(f"total_energy:{total_energy}") if i == 1000 else None
        total_energy = sum(sum(abs(x) for x in moons[idx])*sum(abs(x) for x in velocity[idx]) for idx in range(len(moons))) if i <= 1000 else 0
        i+=1
    print(f"steps:{np.lcm.reduce(periods, dtype=np.uint64)}")