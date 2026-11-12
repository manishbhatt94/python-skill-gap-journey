Your Phase 1 specification makes the right distinction: this is primarily a **mental-model phase**, not a syntax course. The success criterion is being able to reason about object identity, mutation/rebinding, function calls, copying, signatures, and lazy iteration before moving into professional Python/backend tooling. phase-01-complete-prompt

I verified the resources against the current web. As of October 1, 2026, Python 3.14 is the current stable feature series; the material below uses the current Python 3 documentation and avoids version-specific trivia.

# 1. Phase objective

At the end of Phase 1, you should be able to look at ordinary Python code and mentally answer questions such as:

- Did this line mutate an existing object or bind a name to another object?
- Do these two variables currently refer to the same object?
- Can this function modify something visible to its caller?
- Is this function accidentally sharing a mutable default between calls?
- Does this copy still share nested objects with the original?
- Which arguments can be positional, keyword, or keyword-only?
- Is this expression producing a collection now, or values lazily later?
- Can this iterable be traversed again, or has its iterator been consumed?

Those are exactly the kinds of concepts your Phase 1 specification prioritizes. phase-01-complete-prompt

**Target: ~14–16 focused hours including exercises and the mini-project.**

---

# 2. Recommended learning order

| Block | Topic | Time |
|---|---|---:|
| 1 | Fast Python refresh | 1–1.5 h |
| 2 | Names, objects, identity, mutation + function arguments | 2.5–3 h |
| 3 | Mutable defaults + shallow/deep copying | 1.5–2 h |
| 4 | Function signatures: `/`, `*`, `*args`, `**kwargs` | 1.5–2 h |
| 5 | Comprehensions and collection transformations | 1–1.25 h |
| 6 | Iterables, iterators and exhaustion | 1.5–2 h |
| 7 | Generators and lazy pipelines | 2–2.5 h |
| 8 | Phase project | 2.5–3 h |

Do them **in this order**. In particular, do not start generators before you understand iterables versus iterators.

---

# 3. Detailed section-by-section roadmap

## Block 1 — Fast Python syntax refresh

### Must learn now

Refresh, don't study from scratch:

`str`, `int`, `float`, `bool`, `None`; lists, tuples, dicts and sets; indexing/slicing; tuple/unpacking syntax; `if`; `for`; `while`; functions and `return`; basic `try/except`; truthiness; comprehensions at a recognition level; and these built-ins:

`len`, `range`, `enumerate`, `zip`, `sorted`, `sum`, `min`, `max`, `any`, `all`.

The official Python Tutorial is explicitly aimed at programmers who are new to Python rather than people new to programming, which makes it appropriate for your situation. [Python documentation](https://docs.python.org/3.14/tutorial/index.html?utm_source=chatgpt.com)

### Read

[Python Tutorial — An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html?utm_source=chatgpt.com)

Read/skim:

- **3.1.1 Numbers** — skim
- **3.1.2 Text** — skim
- **3.1.3 Lists** — read
- **3.2 First Steps Towards Programming** — skim

Then:

[Python Tutorial — More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html?utm_source=chatgpt.com)

Read/skim:

- **4.1 `if` Statements**
- **4.2 `for` Statements**
- **4.3 `range()`**
- **4.8 Defining Functions**

Do not dwell on beginner examples.

Finally:

[Python Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html?utm_source=chatgpt.com)

Read only **8.3 Handling Exceptions**, stopping once basic `try`/`except` and specific exception types make sense. The docs specifically recommend catching intended exception types rather than indiscriminately swallowing everything. [Python documentation](https://docs.python.org/sv/3.14/tutorial/errors.html?utm_source=chatgpt.com)

### Skim

`break`, `continue`, basic `raise`.

### Skip

`match`, advanced exception chaining, `ExceptionGroup`, custom exception classes, annotations, lambdas, coding-style discussion.

### JavaScript/Java translation

This block should feel mostly familiar. Don't take notes on concepts such as “what is an if statement.” Only note Python-specific syntax or behavior you forgot.

**Time: 60–90 min.**

---

# 4. Names, objects, references, mutation and function arguments

This is the **most important section of Phase 1**.

Your primary resource should not be a generic Python course.

## Primary resource

Ned Batchelder's **Python Names and Values**.

[Read Python Names and Values](https://nedbatchelder.com/text/names1/names1.html?utm_source=chatgpt.com)

Read from the beginning through the sections covering:

- Names refer to values
- Many names can refer to one value
- Assignment never copies data
- Changes are visible through all names
- Mutable aliasing
- Mutable versus immutable
- Rebinding versus mutating
- References inside containers
- Function arguments are assignments
- The `append_twice` examples

Stop once you reach the closing miscellaneous/implementation discussion.

This is an older presentation, but the semantics being explained are fundamental language behavior, not an outdated library API. It directly explains that assignment establishes bindings rather than copying objects, that aliasing exposes mutations through multiple names, and that function parameter binding follows the same assignment model. [Ned Batchelder](https://nedbatchelder.com/text/names1/names1.html)

### The mental model to retain

Think:

**names → objects**

not:

**variables are little storage boxes containing values**.

This applies consistently.

```python
a = [1, 2]
b = a
```

There is one list and two names.

```python
a.append(3)
```

mutates that list.

```python
a = [9]
```

rebinds `a`; it does nothing to `b`.

### `is` versus `==`

Use:

```python
value == other
```

for value equality.

Use:

```python
value is other
```

for object identity.

In everyday backend code, the identity comparison you will use most often is:

```python
value is None
```

The language docs describe every object as having an identity, type, and value, and the Python docs explicitly recommend `is`/`is not` for singletons such as `None`. [Python documentation](https://docs.python.org/3.11/reference/datamodel.html?utm_source=chatgpt.com)

### Java instinct to correct

In Java:

```java
a == b
```

on ordinary objects compares references.

In Python:

```python
a == b
```

normally asks whether the objects are **equal in value**.

Python's:

```python
a is b
```

is closer to Java object-reference `==`.

Do not translate Java `==` mechanically into Python `==`.

### JavaScript instinct to retain—but refine

Python object aliasing will feel similar to JavaScript:

```javascript
const b = a;
```

doesn't clone an object.

But Python's binding model applies uniformly to names referring to all objects. Avoid mentally dividing Python into “primitive assignment” versus “object-reference assignment” as your primary model.

### Function arguments

Think of:

```python
def process(data):
    ...
    
process(events)
```

as creating the local binding conceptually equivalent to:

```python
data = events
```

inside the function's new local namespace.

Therefore:

```python
def f(items):
    items.append(10)
```

can mutate the caller-visible object.

But:

```python
def f(items):
    items = [10]
```

only rebinds the local name.

Batchelder demonstrates exactly this distinction. [Ned Batchelder](https://nedbatchelder.com/text/names1/names1.html)

**Time including exercises: 2.5–3 h.**

---

# 5. Mutable defaults and copying

These are really consequences of the previous mental model.

## Mutable defaults

Read exactly one official FAQ entry:

[Python FAQ — Why are default values shared between objects?](https://docs.python.org/3/faq/programming.html?utm_source=chatgpt.com)

Find **“Why are default values shared between objects?”**

The critical rule is:

**default expressions are evaluated when the function is defined, not each time it is called.**

The official FAQ shows why mutable defaults such as `{}` or `[]` retain changes across calls and recommends a `None` sentinel when fresh state is required. [Python documentation](https://docs.python.org/3/faq/programming.html?utm_source=chatgpt.com)

So:

```python
def add(item, items=[]):
    items.append(item)
    return items
```

is normally wrong.

Use:

```python
def add(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Critical JS difference

This is an especially important JavaScript → Python trap.

A JavaScript default parameter expression is evaluated when the function is called.

A Python default argument is created when the `def` statement executes.

Do not transfer your JavaScript intuition here.

---

## Shallow and deep copying

Read:

[Python `copy` documentation](https://docs.python.org/3/library/copy.html?utm_source=chatgpt.com)

Read only:

- opening explanation
- `copy.copy()`
- `copy.deepcopy()`
- explanation of shallow versus deep copies
- paragraph explaining why `deepcopy()` can copy too much

Stop before custom `__copy__`, `__deepcopy__`, pickle integration, etc.

A shallow copy creates a new outer container while retaining references to nested objects. A deep copy recursively copies nested objects; the docs explicitly warn that deep copying may copy more than you actually want. [Python documentation](https://docs.python.org/3.14/library/copy.html?utm_source=chatgpt.com)

You should know these:

```python
new_list = old_list.copy()
new_dict = old_dict.copy()
new_list = old_list[:]
copy.copy(value)
copy.deepcopy(value)
```

But don't develop the habit of throwing `deepcopy()` at every aliasing concern.

### Useful JS analogy

```javascript
const copy = {...obj}
```

and:

```javascript
const copy = [...array]
```

are also **shallow**.

That intuition transfers well.

**Time: 1.5–2 h.**

---

# 6. Function signatures and argument mechanics

Use only the official tutorial here.

[Python Tutorial — More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html?utm_source=chatgpt.com#more-on-defining-functions)

Read:

- **4.9.1 Default Argument Values**
- **4.9.2 Keyword Arguments**
- **4.9.3 Special parameters**
  - positional-or-keyword
  - positional-only
  - keyword-only
  - examples
  - recap
- **4.9.4 Arbitrary Argument Lists**
- **4.9.5 Unpacking Argument Lists**

The documentation summarizes the three parameter regions with this form:

```python
def f(pos_only, /, pos_or_kw, *, kw_only):
    ...
```

and explains why keyword-only parameters can improve API readability. [Python documentation](https://docs.python.org/bn-in/3.14/tutorial/controlflow.html?utm_source=chatgpt.com)

You need these five meanings completely clear:

```python
def f(*, timeout=10):
```

`*` = everything after here is keyword-only.

```python
def f(*args):
```

`args` = tuple collecting extra positional arguments.

```python
f(*values)
```

unpack iterable into positional arguments.

```python
def f(**kwargs):
```

`kwargs` = dict collecting extra keyword arguments.

```python
f(**options)
```

unpack mapping into keyword arguments.

### `/`

Know what it means:

```python
def f(value, /):
```

`value` must be supplied positionally.

Do **not** spend time designing lots of positional-only APIs yourself yet. You mainly need to understand it when reading Python/library signatures.

### JS comparison

`*args` is somewhat analogous to JS rest:

```javascript
function f(...args)
```

But `**kwargs` has no direct equivalent because Python supports named keyword arguments as a first-class call mechanism.

Likewise Python:

```python
f(**options)
```

may superficially resemble JavaScript object spread, but it is specifically **keyword-argument expansion**.

**Time: 1.5–2 h.**

---

# 7. Comprehensions

Use the Python Tutorial's **Data Structures** chapter.

[Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html?utm_source=chatgpt.com)

Read only the sections on:

- List Comprehensions
- Nested List Comprehensions — **skim examples only**
- Sets
- Dictionaries
- Looping Techniques

Learn:

```python
[x * 2 for x in values]
```

```python
[x for x in values if x > 0]
```

```python
{x.id for x in values}
```

```python
{user["id"]: user for user in users}
```

### Translation from JS

This:

```python
[user["name"] for user in users]
```

maps naturally to:

```javascript
users.map(user => user.name)
```

and:

```python
[user for user in users if user["active"]]
```

combines the role of a JS `filter`.

Don't obsess over compressing everything into one expression.

If a comprehension requires several nested loops, several conditions, side effects, or a comment to decipher, write a normal loop.

**Time: ~1 h.**

---

# 8. Iterables and iterators

Read the official tutorial first:

[Python Tutorial — 9.8 Iterators](https://docs.python.org/3/tutorial/classes.html?utm_source=chatgpt.com#iterators)

The important internal transformation is approximately:

```python
for item in collection:
    ...
```

becoming conceptually:

```python
iterator = iter(collection)

while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
```

The official tutorial explains that `for` calls `iter()`, repeatedly obtains values through `next()`, and terminates when `StopIteration` occurs. [Python documentation](https://docs.python.org/3/tutorial/classes.html?highlight=isinstance\&utm_source=chatgpt.com)

### Must distinguish

A **list** is iterable.

```python
numbers = [1, 2, 3]
```

Repeated calls:

```python
iter(numbers)
```

can produce fresh iterators.

An **iterator** represents traversal state.

```python
it = iter(numbers)
```

Calling:

```python
next(it)
```

advances it.

Once exhausted, that particular iterator stays exhausted.

### Supplement only if this remains fuzzy

Trey Hunner's explanation is unusually clear:

[The Iterator Protocol: How `for` Loops Work in Python](https://treyhunner.com/2016/12/python-iterator-protocol-how-for-loops-work/?utm_source=chatgpt.com)

Read only through the explanation that manually rewrites a `for` loop using `iter()`, `next()` and `StopIteration`. The article shows that the iterator protocol is the common mechanism behind generic iteration. [Trey Hunner](https://treyhunner.com/2016/12/python-iterator-protocol-how-for-loops-work/?utm_source=chatgpt.com)

Do **not** continue into elaborate custom iterator implementations unless you're curious.

**Time: 1.5–2 h.**

---

# 9. Generators and lazy evaluation

Return to the official tutorial:

[Python Tutorial — 9.9 Generators and 9.10 Generator Expressions](https://docs.python.org/3/tutorial/classes.html?utm_source=chatgpt.com#generators)

Read both sections completely.

The key behavior is that `yield` turns the function into a generator function; each `next()` resumes execution where it previously paused, preserving local execution state. The resulting generator is itself an iterator. [Python documentation](https://docs.python.org/3/tutorial/classes.html?highlight=wrapper\&utm_source=chatgpt.com)

Understand this difference instinctively:

```python
[x * 2 for x in numbers]
```

creates the list eagerly.

```python
(x * 2 for x in numbers)
```

creates a lazy generator.

```python
tuple(x * 2 for x in numbers)
```

consumes that generator-like computation into a tuple.

### One optional explanation

If generator expressions still don't click, read only these parts of Trey Hunner's material:

[Generator Expressions — Lazy Looping in Python](https://pycon2019.trey.io/generator-expressions?utm_source=chatgpt.com)

Read:

- Generator Expressions
- Why Generators?
- examples demonstrating laziness
- examples demonstrating one-shot consumption

Skip later advanced material.

His examples emphasize the two ideas you need most: generators are **lazy** and **single-use**. [PyCon 2019](https://pycon2019.trey.io/generator-expressions?utm_source=chatgpt.com)

### `yield from`

Learn only:

```python
def flatten(groups):
    for group in groups:
        yield from group
```

as convenient delegation to another iterable.

No coroutine interpretation yet.

### Backend connection

Generators will later make FastAPI streaming and AI token/event streaming much easier to understand because the fundamental idea is already familiar:

**produce one value → suspend → resume → produce next value.**

**Time: 2–2.5 h.**

---

# 10. Exercises

Don't do algorithm drills. Use these as **prediction tests**.

A useful tool for the object/reference exercises is Python Tutor, which visualizes stack frames, names and objects step-by-step. [Python Tutor](https://pythontutor.com/?utm_source=chatgpt.com)

[Python Tutor visualizer](https://pythontutor.com/visualize.html?utm_source=chatgpt.com)

## A. Names, identity and mutation

Before executing each example, write the expected result.

**Exercise A1**

```python
a = [1, 2]
b = a
a.append(3)
a = [10]

print(a)
print(b)
print(a is b)
```

Explain every line in terms of binding versus mutation.

**Exercise A2**

```python
a = {"config": {"timeout": 10}}
b = a.copy()

b["config"]["timeout"] = 30
```

Predict both dictionaries.

Explain why the result differs from changing:

```python
b["config"] = {"timeout": 30}
```

**Exercise A3**

For ten comparisons using strings, lists and `None`, decide whether `==` or `is` is appropriate before writing the expression.

---

## B. Function arguments and defaults

**Exercise B1**

Predict:

```python
def modify(values):
    values.append(4)
    values = [100]
    return values

original = [1, 2, 3]
result = modify(original)
```

What are `original` and `result`?

**Exercise B2**

Find and repair:

```python
def collect_errors(message, errors=[]):
    errors.append(message)
    return errors
```

Then explain *why* the repaired version works rather than merely memorizing the pattern.

**Exercise B3**

Write two versions of:

```python
add_tag(...)
```

One intentionally mutates the passed dictionary. The other returns a modified copy without changing the caller's outer dictionary.

---

## C. Copying

**Exercise C1**

Create:

```python
request = {
    "model": "x",
    "messages": [
        {"role": "user", "content": "hello"}
    ]
}
```

Compare:

```python
alias = request
shallow = request.copy()
deep = copy.deepcopy(request)
```

Modify nested `messages[0]["content"]` through each and predict which structures change.

**Exercise C2**

Decide whether these situations require no copy, a shallow copy, or a deep copy:

- adding a top-level HTTP header
- editing a nested configuration object
- iterating without modifying
- returning an intentionally immutable/read-only conceptual object

The goal is reasoning, not always choosing `deepcopy`.

---

## D. Function signatures

**Exercise D1**

Design:

```python
send_request(...)
```

with:

- required `prompt`
- optional `model`
- keyword-only `timeout`
- keyword-only `retries`

Make these invalid:

```python
send_request("hello", "gpt", 10, 3)
```

but valid:

```python
send_request("hello", "gpt", timeout=10, retries=3)
```

**Exercise D2**

Given:

```python
args = ["hello", "model-x"]
options = {"timeout": 5, "retries": 2}
```

call your function using `*args` and `**options`.

**Exercise D3**

Write a forwarding wrapper using:

```python
*args, **kwargs
```

Then ask yourself whether flexible forwarding is actually preferable to an explicit signature for an application-level API. Usually it isn't.

---

## E. Comprehensions

Given a list of API-like records:

```python
users = [
    {"id": 1, "name": "A", "active": True},
    {"id": 2, "name": "B", "active": False},
    {"id": 3, "name": "C", "active": True},
]
```

**Exercise E1:** produce names of active users.

**Exercise E2:** produce `{id: name}` for active users.

**Exercise E3:** write one deliberately overcomplicated comprehension, then rewrite it as a normal loop. Decide which you would approve in a code review.

---

## F. Iterators and generators

**Exercise F1**

Predict:

```python
values = [1, 2, 3]
it = iter(values)

print(next(it))
print(list(it))
print(list(it))
print(list(values))
```

Explain why the last line behaves differently.

**Exercise F2**

Write:

```python
def valid_records(records):
    ...
```

as a generator yielding only valid dictionaries.

Manually call `next()` twice before using a loop.

**Exercise F3**

Create the eager and lazy versions:

```python
squares_list = ...
squares_generator = ...
```

Consume the generator twice.

Explain the result.

**Exercise F4**

Write a generator pipeline:

```text
raw records
    ↓
valid records
    ↓
normalized records
    ↓
selected records
```

Do not create intermediate lists.

---

# 11. Phase project — Streaming JSON Event Processor

Your specification asks for a small realistic project using JSON/text-like backend data and generators without introducing FastAPI. phase-01-complete-prompt

Build a tiny **newline-delimited JSON (NDJSON) event processor**.

Example input:

```text
{"type":"login","user_id":12,"metadata":{"source":"web"}}
{"type":"purchase","user_id":12,"amount":499,"metadata":{"source":"app"}}
{"type":"login","user_id":27,"metadata":{"source":"web"}}
```

## Required functions

Implement something approximately like:

```python
def read_events(file_obj):
    ...
```

A generator. Read one line at a time, parse JSON and `yield` one event.

```python
def normalize_event(
    event,
    *,
    remove_fields=None,
    copy_input=True,
):
    ...
```

Use a safe `None` default. Deliberately decide whether the function mutates the original.

```python
def filter_events(
    events,
    *,
    event_type=None,
    user_id=None,
):
    ...
```

Return/yield lazily rather than making an unnecessary list.

```python
def summarize_events(events):
    ...
```

Consume events and return a dictionary such as counts by type.

## Features it must demonstrate

Your implementation should contain:

- one safe optional mutable configuration parameter
- at least two keyword-only arguments
- one comprehension
- one generator expression
- at least two generator functions
- one deliberate shallow-copy decision
- one place where you consciously avoid `deepcopy`
- basic `try/except` around malformed JSON
- `enumerate()` for line numbers
- lazy line processing rather than `readlines()`
- one explicit demonstration that a generator becomes exhausted

Keep it to roughly:

```text
phase1_project/
    event_processor.py
    sample_events.ndjson
```

No packaging. No classes unless they genuinely simplify something. No framework.

## Deliberate bugs to create and then fix

Temporarily introduce these four bugs:

```python
remove_fields=[]
```

Explain why it can be dangerous.

Make a shallow copy, then mutate a nested `metadata` dictionary and observe aliasing.

Try summarizing the same generator twice.

Use:

```python
event_type is "login"
```

and replace it with the correct comparison.

If you can explain *why* each bug occurs, the project is doing its job.

## Done definition

You are finished when you can process a large input conceptually as:

```python
events = read_events(file)
events = filter_events(events, event_type="purchase")
events = (normalize_event(e) for e in events)
summary = summarize_events(events)
```

and accurately explain:

1. when execution actually occurs,
2. which values are generators,
3. which objects can be mutated,
4. which operations create new objects,
5. when the iterator becomes exhausted.

Project time: **2.5–3 h**, not several days.

---

# 12. What to skim and what to skip

### Understand conceptually / skim

Know that these exist, but don't study them:

- garbage collection
- reference counting
- object interning
- custom iterator classes
- generator `send()`, `throw()`, `close()`
- internal generator/coroutine machinery
- Python descriptors

### Explicitly skip

Do **not** branch into:

- decorators
- dataclasses
- advanced OOP
- type hints/mypy/Pyright
- Pydantic
- context managers beyond recognizing `with`
- modules/package architecture
- `venv`, `uv`, packaging
- pytest
- FastAPI
- SQLAlchemy
- `asyncio`
- threads/processes
- AI SDKs
- metaclasses
- CPython internals

Your own specification explicitly postpones these topics. phase-01-complete-prompt

---

# 13. Completion checklist

Move to Phase 2 when you can answer **yes** to these without looking everything up:

- I can explain Python as names bound to objects.
- I can distinguish rebinding from mutation.
- I understand aliasing.
- I know the practical mutable and immutable built-in types.
- I use `==` for equality and `is` mainly for identity/singletons such as `None`.
- I can predict caller-visible effects when passing mutable objects into functions.
- I understand why mutable default arguments share state.
- I can explain shallow versus deep copying with a nested dictionary example.
- I understand positional, keyword and keyword-only arguments.
- I can read `/` and `*` in a function signature.
- I understand `*args`, `**kwargs`, `*iterable`, and `**mapping`.
- I can write readable list/dict/set comprehensions.
- I know when an ordinary loop is clearer.
- I can explain iterable versus iterator.
- I understand `iter()`, `next()` and `StopIteration`.
- I understand why a list is restartable but a particular iterator may be exhausted.
- I can write a generator function with `yield`.
- I understand generator expressions.
- I can explain eager versus lazy evaluation.
- I understand why a consumed generator doesn't magically restart.
- I can build the event-processing project without copying code blindly.

Don't demand perfect recall of syntax. Your Phase 1 completion criterion is **correct reasoning about normal Python code**, exactly as your authoritative prompt specifies. phase-01-complete-prompt

## Total commitment

A realistic focused allocation is **14–16 hours**:

**~10–12 hours learning + targeted exercises, ~3 hours project, ~1 hour revisiting anything you predicted incorrectly.**

The highest-value resources are therefore only **five real study sources**: the selected Python Tutorial sections, Batchelder's *Names and Values*, the Python mutable-default FAQ entry, the `copy` documentation, and the iterator/generator sections of the Python Tutorial. Trey Hunner is a **fallback explanation**, not additional mandatory coursework. That is the resource discipline I would maintain for the later phases too.
