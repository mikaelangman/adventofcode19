def calc_fuel(w):

    req = int(w/3)-2

    if req > 0:
        return req + calc_fuel(req)
    else:
        return 0

with open("inputs/1.txt", "r") as f:
    inputs = [int(line.strip()) for line in f]

print(sum([calc_fuel(inpt) for inpt in inputs]))
