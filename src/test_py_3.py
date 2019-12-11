"""
Code from https://github.com/0x8b/advent-of-code-2019/blob/master/03.py
Due to bad performance of my solution, I searched for a better one and 
tried at this one. The solution to the second part is mine, the rest 
is copied
"""

from itertools import accumulate, count

with open("../Data/input_d3_alt", "r") as f:
    c = f.read()
    wires = c[c.rindex("$") + 1 : c.rindex("§")].rstrip().split("\n")

d = {"U": 1j, "R": 1, "D": -1j, "L": -1}


def manhattan(c):
    return abs(c.real) + abs(c.imag)


def steps(wire):
    step = (d[s[0]] for s in wire.split(",") for _ in range(int(s[1:])))
    print(step)
    return dict(reversed(list(zip(accumulate(step), count(1)))))


route_one = steps(wires[0])
route_two = steps(wires[1])
common_points = set(route_one.keys()) & set(route_two.keys())
closest = min(common_points, key=lambda p: manhattan(p))

part_one = int(manhattan(closest))
print(part_one)

minimal_dist = min(common_points, key=lambda p: route_one.get(p) + route_two.get(p))
print(route_one.get(minimal_dist) + route_two.get(minimal_dist))
