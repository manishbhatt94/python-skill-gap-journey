a = {"config": {"timeout": 10}}
b = a.copy()

b["config"]["timeout"] = 30

print(f"{b["config"]["timeout"]=}")  # Prints 30
print(f"{a["config"]["timeout"]=}")  # Also, Prints 30
