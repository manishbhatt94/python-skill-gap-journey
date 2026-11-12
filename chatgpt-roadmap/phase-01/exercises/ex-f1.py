values = [1, 2, 3]
it = iter(values)

print(next(it))
# Prints: 1

print(list(it))
# Prints: [2, 3]

print(list(it))
# Prints: []
# (Since iterator 'it' was exhausted in previous statement, so when list(..)
# calls next(it) then a StopIteration exception is raised & list(..) just
# returns an empty list.)

print(list(values))
# Prints: [1,2,3]
