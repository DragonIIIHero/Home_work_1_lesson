src = [2, 12, 41, 65, 3, 2, 1, 4, 134, 12, 44, 1231, 51]
num_list = []

for i in range(len(src)):
     if src[i] > src[i - 1]:
         num_list.append(src[i])

print(num_list)
