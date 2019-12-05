with open("inputs/5.txt", "r") as f:
    mem = f.read().replace("\n", "").split(",")
    mem = [int(b) for b in mem]

op = mem[0]
mem_pointer = 0
inpt = 1
outpt = 0

while op is not 99:

    modes = [0, 0, 0]

    if op > 9: #This op has a param in immediate mode

        im_modes = [int(m) for m in str(op)][:-2]
        modes[-len(im_modes):] = im_modes
        op = [int(m) for m in str(op)][-2:]
        op = op[0] * 10 + op[1]

    print("Input:", mem_pointer, modes, op)



    output_addr = 0
    acc = 0
    reg = [0, 0]
    op_len = 2

    if op is 1 or op is 2:

        output_addr = mem[mem_pointer+3]
        reg[0] = mem[mem_pointer+1] if modes[-1] else mem[mem[mem_pointer+1]]
        reg[1] = mem[mem_pointer+2] if modes[-2] else mem[mem[mem_pointer+2]]
        acc = reg[0] + reg[1] if op is 1 else reg[0] * reg[1]
        op_len = 4

    elif op is 3:
        output_addr = mem[mem_pointer+1]
        acc = inpt

    elif op is 4:
        acc = mem[mem[mem_pointer+1]]


    print(output_addr, acc)

    mem[output_addr] = acc

    mem_pointer += op_len
    op = mem[mem_pointer]

print(mem[0])
