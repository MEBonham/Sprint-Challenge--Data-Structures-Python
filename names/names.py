import time
import sys
sys.path.insert(0, "C:/Users/McKay/Documents/GitHub/Data-Structures/binary_search_tree")
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# tree = BinarySearchTree(names_2[0])
# for i in range(1, len(names_2)):
#     tree.insert(names_2[i])
# duplicates = []
# for name_to_match in names_1:
#     if tree.contains(name_to_match):
#         duplicates.append(name_to_match)

names_1.sort()
names_2.sort()
i, j, duplicates = 0, 0, []
while i < len(names_1) - 1 or j < len(names_2) - 1:
    if names_1[i] == names_2[j]:
        duplicates.append(names_1[i])
        i += 1
        j += 1
    elif i == len(names_1) - 1 or names_1[i] > names_2[j]:
        j += 1
    else:
        i += 1

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

