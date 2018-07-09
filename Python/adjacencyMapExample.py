powerTwos =   {2: 4, 3: 8, 4: 16}
powerThrees = {2: 9, 3: 27}

powerMap = {2: powerTwos, 3: powerThrees}

print("Length of len(powerMap):", len(powerMap),  sep = " ")
print()
print("powermap[3][3]: ", powerMap[3][3], sep = " ")
print()
print("powermap[3]:", powerMap[3], sep = " ")

for v in powerTwos:
    print(v)