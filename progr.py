inp = input()
zakryj = 0
ost = ""

for i in range(len(inp)):
    if inp[i] == ost:
        zakryj += 1
    ost = inp[i]
print(zakryj)