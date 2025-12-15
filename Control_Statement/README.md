Control Statements in Python — Detailed Notes with Examples
=========================================================

**Overview:** Control statements change the flow of execution in a program. Python's main control structures are:
- **Conditionals:** `if`, `elif`, `else` — choose which code runs.
- **Loops:** `for`, `while` — repeat code.
- **Loop control:** `break`, `continue`, `pass` — alter loop behavior.
- **Comprehensions & generator expressions:** concise ways to create sequences (briefly noted here).

These notes include syntax, examples, common patterns, and small exercises with answers.

**1. Conditional Statements**

- **Syntax:**

```python
if condition:
    # executed when condition is True
elif other_condition:
    # executed when other_condition is True
else:
    # executed when all above conditions are False
```

- **Example:** basic if/elif/else

```python
x = 15
if x < 10:
    print('less than 10')
elif x < 20:
    print('between 10 and 19')
else:
    print('20 or more')
# Output: between 10 and 19
```

- **Boolean expressions:** Use `and`, `or`, `not` and comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`).

```python
age = 25
if 18 <= age < 30 and not False:
    print('Young adult')
```

- **Ternary (conditional) expression:** Single-line `if`-`else`.

```python
status = 'even' if x % 2 == 0 else 'odd'
```

- **Nested conditionals:** Keep nesting shallow for readability; consider functions for complex logic.

```python
if a > 0:
    if b > 0:
        print('both positive')
    else:
        print('a positive, b non-positive')
```

**2. `for` Loops**

- **Basic `for` over iterable:**

```python
for item in [1, 2, 3]:
    print(item)
# prints 1 2 3 on separate lines
```

- **Using `range()`**

```python
for i in range(5):      # 0,1,2,3,4
    print(i)

for i in range(2, 6):   # 2,3,4,5
    print(i)

for i in range(10, 0, -2):  # 10,8,6,4,2
    print(i)
```

- **`enumerate()`** — get index and value

```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

- **`zip()`** — iterate multiple iterables in parallel

```python
names = ['a', 'b']
ages = [30, 25]
for name, age in zip(names, ages):
    print(name, age)
```

- **Iterating dictionaries**

```python
d = {'k1': 10, 'k2': 20}
for key in d:            # keys
    print(key, d[key])

for key, value in d.items():
    print(key, value)
```

**3. `while` Loops**

- **Syntax and example:**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

- **Avoid infinite loops:** Make sure loop condition becomes False at some point. Use `break` to exit early if needed.

**4. Loop Control Statements**

- **`break`** — exit the nearest loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
# prints 0..4 then stops
```

- **`continue`** — skip the rest of the current iteration and continue with the next.

```python
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
# prints odd numbers: 1,3,5
```

- **`pass`** — placeholder for empty blocks

```python
if condition:
    pass  # TODO: implement later
```

- **`else` clause on loops:** Executes when the loop completes normally (i.e., no `break`). Useful for search patterns.

```python
def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            print('Found', n)
            break
    else:
        print('No even numbers')

find_first_even([1,3,5])   # prints: No even numbers
```

**5. Examples — small, runnable**

- Example: Check prime (simple, not optimized)

```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

print(is_prime(29))  # True
print(is_prime(30))  # False
```

- Example: Factorial with `for` and `while` implementations

```python
def factorial_for(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def factorial_while(n):
    result = 1
    i = 2
    while i <= n:
        result *= i
        i += 1
    return result

print(factorial_for(5))   # 120
print(factorial_while(5)) # 120
```

- Example: Loop `else` used for search

```python
target = 7
for x in [2,4,6,8]:
    if x == target:
        print('Found')
        break
else:
    print('Target not found')
# prints: Target not found
```

**6. Common patterns & tips**

- Prefer `for` loops for finite iterables; use `while` when the loop condition is not index-based.
- Keep loop bodies short; extract complex logic into functions.
- Use `enumerate()` instead of maintaining a manual index.
- Use comprehensions for simple transformations and filters:

```python
squares = [x*x for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

- Avoid modifying a list while iterating it; iterate over a copy or build a new list.

**7. Exercises (with answers)**

- Exercise 1: Write a function `count_vowels(s)` that returns the number of vowels in string `s`.

Answer:
```python
def count_vowels(s):
    vowels = set('aeiouAEIOU')
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

print(count_vowels('Hello World'))  # 3
```

- Exercise 2: Using a loop with `else`, write `find_index(lst, val)` that returns index of `val` or `-1` if not found.

Answer:
```python
def find_index(lst, val):
    for i, x in enumerate(lst):
        if x == val:
            return i
    else:
        return -1

print(find_index([5,3,7], 7))  # 2
print(find_index([5,3,7], 2))  # -1
```

**8. Quick reference (cheatsheet)**

- `if/elif/else` — branch by conditions
- `for x in iterable` — iterate values
- `for i in range(n)` — iterate indices/numbers
- `while condition` — loop while condition True
- `break` — exit loop
- `continue` — skip to next iteration
- `pass` — no-op placeholder
- `enumerate(iterable, start=0)` — (index, value)
- `zip(a, b, ...)` — iterate multiple iterables

**9. How to run examples**

Save the desired example into a file, e.g., `example.py`, then run:

```bash
python3 example.py
```

**References & further reading:** Python docs — "The Python Language Reference": Control Flow Tools, and tutorials on `for`, `while`, and `if` statements.


