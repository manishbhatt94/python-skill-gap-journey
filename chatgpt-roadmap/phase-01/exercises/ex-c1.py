import copy

request = {"model": "x", "messages": [{"role": "user", "content": "hello"}]}
alias = request
shallow = request.copy()
deep = copy.deepcopy(request)

# Changing 'request':
print("Change through 'request':")
request["messages"][0]["content"] = "hello-request"

print("> Changes reflected in which references?")
print("  - request: ", request["messages"][0]["content"])  # "hello-request"
print("  - alias:   ", alias["messages"][0]["content"])  # "hello-request"
print("  - shallow: ", shallow["messages"][0]["content"])  # "hello-request"
print("  - deep:    ", deep["messages"][0]["content"])  # "hello"


# Reset
request = {"model": "x", "messages": [{"role": "user", "content": "hello"}]}
alias = request
shallow = request.copy()
deep = copy.deepcopy(request)

print("\n--- Reset ---\n")

# Changing 'alias':
print("Change through 'alias':")
alias["messages"][0]["content"] = "hello-alias"

print("> Changes reflected in which references?")
print("  - request: ", request["messages"][0]["content"])  # "hello-alias"
print("  - alias:   ", alias["messages"][0]["content"])  # "hello-alias"
print("  - shallow: ", shallow["messages"][0]["content"])  # "hello-alias"
print("  - deep:    ", deep["messages"][0]["content"])  # "hello"


# Reset
request = {"model": "x", "messages": [{"role": "user", "content": "hello"}]}
alias = request
shallow = request.copy()
deep = copy.deepcopy(request)

print("\n--- Reset ---\n")

# Changing 'shallow':
print("Change through 'shallow':")
shallow["messages"][0]["content"] = "hello-shallow"

print("> Changes reflected in which references?")
print("  - request: ", request["messages"][0]["content"])  # "hello-shallow"
print("  - alias:   ", alias["messages"][0]["content"])  # "hello-shallow"
print("  - shallow: ", shallow["messages"][0]["content"])  # "hello-shallow"
print("  - deep:    ", deep["messages"][0]["content"])  # "hello"


# Reset
request = {"model": "x", "messages": [{"role": "user", "content": "hello"}]}
alias = request
shallow = request.copy()
deep = copy.deepcopy(request)

print("\n--- Reset ---\n")

# Changing 'deep':
print("Change through 'deep':")
deep["messages"][0]["content"] = "hello-deep"

print("> Changes reflected in which references?")
print("  - request: ", request["messages"][0]["content"])  # "hello"
print("  - alias:   ", alias["messages"][0]["content"])  # "hello"
print("  - shallow: ", shallow["messages"][0]["content"])  # "hello"
print("  - deep:    ", deep["messages"][0]["content"])  # "hello-deep"
