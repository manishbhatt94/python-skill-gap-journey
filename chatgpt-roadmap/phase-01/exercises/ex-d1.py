def send_request(prompt, model="gpt", *, timeout, retries):
    print(f"{prompt=}")
    print(f"{model=}")
    print(f"{timeout=}")
    print(f"{retries=}")


# Invalid call:
# send_request("hello", "gpt", 10, 3)
# TypeError: send_request() takes from 1 to 2 positional arguments but 4 were give

# Valid call:
send_request("hello", "gpt-astra-6", timeout=10, retries=3)

# Valid call:
send_request("hello", timeout=10, retries=3)
# Testing default value for `model` parameter


args = ["hello", "model-x"]
options = {"timeout": 5, "retries": 2}

send_request(*args, **options)
