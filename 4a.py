
ctr = 0
for i in range(359282+1, 820401):
    digits = [d for d in str(i)]
    
    has_pair = any(digits[idx] == digits[idx+1] for idx in range(len(digits)-1))

    if not has_pair:
        continue

    is_not_inc = any(digits[idx_l] > digits[idx_g] for idx_g in range(-1, -(len(digits)), -1) for idx_l in range(len(digits)+idx_g) )

    if is_not_inc:
        continue
    
    ctr +=1

print(ctr)

    #lambda a : a + 10