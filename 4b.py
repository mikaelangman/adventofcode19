
ctr = 0
for i in range(359282+1, 820401):
    digits = [d for d in str(i)]
    
    has_pair_start = (digits[0] == digits[1]) and (digits[1] != digits[2])
    has_pair = any((digits[idx+1] == digits[idx+2]) and ((digits[idx] != digits[idx+1]) and (digits[idx+2] != digits[idx+3])) for idx in range(len(digits)-3))
    has_pair_end = (digits[-1] == digits[-2]) and (digits[-2] != digits[-3])


    if not (has_pair or has_pair_start or has_pair_end):
        continue

    is_not_inc = any(digits[idx_l] > digits[idx_g] for idx_g in range(-1, -(len(digits)), -1) for idx_l in range(len(digits)+idx_g) )

    if is_not_inc:
        continue
    ctr +=1

print(ctr)