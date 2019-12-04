def run(mem, verb, noun):    

    mem[1] = noun
    mem[2] = verb
    op = mem[0]
    mem_pointer = 0

    while op is not 99:
        if op is 1:
            mem[mem[mem_pointer+3]] = mem[mem[mem_pointer+1]] + mem[mem[mem_pointer+2]]
        else:
            mem[mem[mem_pointer+3]] = mem[mem[mem_pointer+1]] * mem[mem[mem_pointer+2]]

        mem_pointer += 4
        op = mem[mem_pointer]
    return mem[0]

with open("inputs/2.txt", "r") as f:
    mem = f.read().replace("\n", "").split(",")
    mem = [int(b) for b in mem]   

for verb in range(100):
    for noun in range(100):

        output = run(mem.copy(), verb, noun)
        if output == 19690720:
            print(verb, noun, 100*noun + verb)
            break
