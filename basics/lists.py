list = [0, 2, 4, 6]
list.append("3" * 3)
list.reverse()
print(list.count(2))
list.remove(6)
print(list[0:3])

# Basic operations and tuples
print(list * 3)
tuple = (1, 2, 4, 4, 4)
print(tuple.count(4))
# tuple[0] = 8 tuples are immutable
