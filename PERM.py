from itertools import permutations

n = 5
my_list = [1,2,3,4,5]

perms = list(permutations(my_list))

for perm in perms:
    perm_1 = str(perm).replace(",", "").replace("(", "").replace(")", "")
    print(perm_1)

print(len(perms))

output_file = "output.txt"

with open(output_file, 'w') as file:
    for perm in perms:
        perm_1 = str(perm).replace(",", "").replace("(", "").replace(")", "")
        file.write(perm_1 + '\n')