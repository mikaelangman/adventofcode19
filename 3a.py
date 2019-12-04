wires = []

with open("inputs/3.txt", "r") as f:
    for line in f:
        wires.append(line.strip().split(","))
#(x, y)
wire_coordinates = []

for idx, wire in enumerate(wires):
    wire_coordinates.append([(0,0)])
    for inst in wire:
        
        direction = inst[0]
        length = int(inst[1:])

        dx = 0
        dy = 0

        if direction == "R":
            dx = 1
        elif direction == "D":
            dy = 1
        elif direction == "L":
            dx = -1
        elif direction == "U":
            dy = -1

        for i in range(length):
            last_coord = wire_coordinates[idx][-1]
            wire_coordinates[idx].append((last_coord[0]+dx, last_coord[1]+dy))


smallest_dist = 99999999
for coord in wire_coordinates[0]:
    if coord in wire_coordinates[1]:
        if coord != (0,0):
            dist = abs(coord[0]) + abs(coord[1])
            smallest_dist = dist if dist < smallest_dist else smallest_dist

print(smallest_dist)