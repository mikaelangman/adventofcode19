with open("inputs/1.txt", "r") as f:
    inputs = [int(line.strip()) for line in f]

print(sum([int(ipt/3)-2 for ipt in inputs]))

