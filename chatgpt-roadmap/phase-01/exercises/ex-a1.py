a = [1, 2]
# Name 'a' points to a list [1, 2] in memory

b = a
# Name 'b' now also points to the same list

a.append(3)
# This same list is mutated using .append() and so the list now becomes [1,2,3].
# Currently, both names 'a' and 'b' point at this very list ([1,2,3]) in memory.

a = [10]
# Name 'a' now points to a new list [10] in memory.
# Name 'b' continues to point to the list [1,2,3] it was already referring to.

print(a)
# Prints: [10]

print(b)
# Prints: [1,2,3]

print(a is b)
# Prints: False
