Here is the 80/20 learning path for Phase 1. We are completely bypassing beginner syntax and focusing entirely on how Python handles data in memory and moves it across function boundaries.

### Key Mental Model Shifts (Java/JS -> Python)

* **Variables are "Tags", not "Boxes":** In Java, `int x = 5;` creates a typed box in memory named `x` and puts `5` inside. In Python, `x = 5` creates an integer object `5`, and slaps a sticky note named `x` on it. If you say `y = x`, you put a `y` sticky note on the *exact same object*.
* **"Pass-by-Assignment" (Call-by-Sharing):** Python doesn't strictly use Java's pass-by-value or pass-by-reference. When you pass a variable to a function, the function's local parameter becomes a new sticky note attached to the *caller's original object*.
* If the object is **mutable** (like a `list` or `dict`) and you change it (`item.append(1)`), the caller sees the change.
* If you **reassign** the parameter (`item = [1]`), you just moved the local sticky note to a new object. The caller's object is unaffected.


* **Everything is an Object:** Java has primitives (`int`, `boolean`) and objects. Python *only* has objects. `x = 1` creates an object. Because integers are **immutable** in Python, you can't change the `1` object; you can only rebind the `x` sticky note to a new integer object.
* **JS `...` vs Python `*` and `**`:** JavaScript uses `...` for everything (arrays and objects). Python splits this: `*` unpacks Iterables (lists, tuples) and `**` unpacks Mappings (dictionaries).
* **The Default Argument Trap:** In JS/Java, default arguments are evaluated every time the function is called. **In Python, default arguments are evaluated exactly ONCE**, when the function is defined. If you use a mutable default like `list = []`, *every single call to that function shares the exact same list.*

---

### 1. Resource List

#### Must Learn Now

* **Primary Conceptual Anchor:** [Facts and myths about Python names and values](https://www.google.com/search?q=https://nedbatchelder.com/text/names1.html) (by Ned Batchelder)
* **What to consume:** Read the entire text article (it's a transcript of a famous PyCon talk).
* **Concepts to extract:** The "sticky note" mental model, aliasing, why `is` differs from `==`, and mutability vs. reassignment.
* **Time:** ~30 minutes.


* **Primary Function Signatures:** [Python Official Tutorial - Section 4.7: More on Defining Functions](https://www.google.com/search?q=https://docs.python.org/3/tutorial/controlflow.html%23more-on-defining-functions)
* **What to consume:** Read strictly sections **4.7.2** (Default Argument Values) through **4.7.6** (Unpacking Argument Lists).
* **Concepts to extract:** The mutable default warning, positional-only arguments (`/`), keyword-only arguments (`*`), `*args` and `**kwargs`.
* **Time:** ~25 minutes.



#### Understand Conceptually / Skim

* **Primary Resource:** [Python Official Docs - `copy` module](https://docs.python.org/3/library/copy.html)
* **What to consume:** Just read the first three paragraphs explaining the difference between shallow and deep copies. Look at the code examples for `copy.copy()` and `copy.deepcopy()`.
* **Concepts to extract:** Realize that standard assignments (`a = b`) or list copies (`a = b.copy()`) do NOT duplicate nested mutable objects (like a list of dicts).
* **Time:** ~10 minutes.



#### Skip For Now

* Python's Garbage Collection (`gc` module) and reference counting internals.
* `weakref` (weak references).
* Advanced descriptors and metaclasses (often bundled with OOP memory discussions).
* The `inspect` module (used for dynamically analyzing function signatures).

---

### 2. Targeted Exercises

*Do these in a simple Python script or REPL.*

**Exercise 1: The Mutable Default Trap (10 mins)**
Examine this code for a mock AI request history:

```python
def add_message(role, content, history=[]):
    history.append({"role": role, "content": content})
    return history

user1_chat = add_message("user", "Hello")
user2_chat = add_message("user", "Start new chat")
print(user2_chat)

```

1. Run it mentally: what will `user2_chat` print? (Hint: It's a bug).
2. Rewrite the function using the `None` sentinel pattern (`history=None`) so that `user1_chat` and `user2_chat` get completely separate histories.

**Exercise 2: Reassignment vs. Mutation (10 mins)**
Without running the code, predict the output of `print(my_list)` and `print(my_dict)`. Write down *why* using the "sticky note" metaphor.

```python
def update_data(a_list, a_dict):
    # Reassignment
    a_list = ['new', 'list']
    # Mutation
    a_dict['status'] = 'updated'

my_list = ['old', 'list']
my_dict = {'status': 'pending'}

update_data(my_list, my_dict)
print(my_list)
print(my_dict)

```

**Exercise 3: The API Signature (15 mins)**
Write a function `build_ai_request` that mirrors a strict backend API wrapper. It must:

1. Take `prompt` as a required, standard argument.
2. Take `model` as a positional-only argument (using `/`).
3. Enforce that `temperature` and `max_tokens` are keyword-only arguments (using `*`), defaulting to `0.7` and `None` respectively.
4. Accept any other random configuration parameters via `**kwargs`.
5. Inside the function, merge all these into a single dictionary and return it. (Hint: Use `**kwargs` unpacking inside the dictionary literal: `{**kwargs, "prompt": prompt...}`).

---

### 3. Phase 1 Project: Mock AI Request Router

**The Goal:** Write a small, isolated script (`request_builder.py`) that acts as an intermediate layer between an API route and an LLM provider. This script will form the core logic we package in Phase 2.

**Requirements:**

1. Create a function `create_completion_payload(model, /, prompt, *, temperature=0.7, stream=False, messages=None, **extra_config)`
2. Ensure `messages` safely handles the mutable default trap (if no messages are passed, initialize an empty list).
3. Append a new dict `{"role": "user", "content": prompt}` to `messages`.
4. Create a final payload dictionary. It should contain the model, messages, temperature, stream flag, and anything passed into `extra_config`.
5. Return the payload.
6. Below the function, write a few test executions (e.g., `payload1 = create_completion_payload("gpt-4o", "Hello", temperature=0.5, user="manish", timeout=30)`). Print the results to verify.

**Why this matters:** This perfectly mimics real backend SDK wrappers where you must strictly control how users pass arguments (forcing keywords for boolean flags like `stream`) while collecting arbitrary provider-specific arguments (`user`, `timeout`) via `**kwargs` without modifying the original inputs.

---

### 4. Completion Checklist

Before asking to move to Phase 2, ensure you can:

* [ ] Explain why `x is None` is safer and more idiomatic than `x == None`.
* [ ] Correctly implement the `if arg is None: arg = []` pattern for default arguments.
* [ ] Explain the difference between Python's `**kwargs` in a function signature vs. `{**dict1, **dict2}` in a dictionary literal.
* [ ] Read a function signature like `def get(url, /, params=None, *, timeout=5):` and know exactly which arguments can be passed by name and which cannot.
