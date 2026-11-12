users = [
    {"id": 1, "name": "A", "active": True},
    {"id": 2, "name": "B", "active": False},
    {"id": 3, "name": "C", "active": True},
]

# Exercise E1: produce names of active users.
active_users_names = [user["name"] for user in users if user["active"]]
print("active_users_names:", active_users_names)

# Exercise E2: produce {id: name} for active users.
user_map = {user["id"]: user["name"] for user in users if user["active"]}
print("user_map:", user_map)
