with open("inputs/2.txt", "r") as f:
    mem = f.read().replace("\n", "").split(",")
    mem = [int(b) for b in mem]

mem[1] = 12
mem[2] = 2
op = mem[0]
mem_pointer = 0

while op is not 99:


    if op is 1:
        mem[mem[mem_pointer+3]] = mem[mem[mem_pointer+1]] + mem[mem[mem_pointer+2]]
    else:
        mem[mem[mem_pointer+3]] = mem[mem[mem_pointer+1]] * mem[mem[mem_pointer+2]]

    mem_pointer += 4
    op = mem[mem_pointer]

print(mem[0])
