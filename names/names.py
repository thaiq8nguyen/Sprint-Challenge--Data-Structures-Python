import time
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = BinarySearchTree(value)
            
        else:
            if self.value > value:
                # go to the left side
                if self.left is not None:
                    self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)
                    return
            else:
                # go to the right side
                if self.right is not None:
                    self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)
                    return

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value > target:
            # go left
            if self.left is None:
                return False
            return self.left.contains(target)


        elif target > self.value:
            # go right
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            return True
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1: # 9.713s
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# for names_2 in names_2: #1.874s
#     if names_2 in names_1:
#         duplicates.append(names_2)

name_tree = BinarySearchTree(names_1[0]) # 0.144s

for i in range(1, len(names_1)):
    name_tree.insert(names_1[i])

for n in names_2:
    if name_tree.contains(n):
        duplicates.append(n)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
