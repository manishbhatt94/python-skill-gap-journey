def modify(values):
    values.append(4)
    values = [100]
    return values


original = [1, 2, 3]
result = modify(original)

print(f"{result=}")  # result=[100]
print(f"{original=}")  # original=[1,2,3,4]
