List Comprehensions & Generators — Notes & Examples
=================================================

Overview
- Comprehensions provide concise syntax for building lists, sets, dicts, and generators.
- They are readable and often faster than manual loops.

1. List comprehension
```python
squares = [x*x for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

2. Conditional expressions inside comprehensions
```python
labels = ['even' if x%2==0 else 'odd' for x in range(6)]
```

3. Nested comprehensions
```python
matrix = [[i*j for j in range(5)] for i in range(3)]
```

4. Dict and set comprehensions
```python
square_map = {x: x*x for x in range(6)}
unique_lengths = {len(s) for s in ['a','ab','abc']}
```

5. Generator expressions
- Lazily evaluated, use parentheses; useful for streaming and memory efficiency.
```python
gen = (x*x for x in range(1000000))
sum_of_squares = sum(gen)
```

6. When not to use comprehensions
- Avoid very long or nested comprehensions that hurt readability; prefer helper functions or `for` loops.

7. Examples
- Flatten a nested list (one level) with comprehension:
```python
nested = [[1,2],[3,4]]
flat = [x for sub in nested for x in sub]
```

8. Performance tip
- Comprehensions are implemented in C and often faster than equivalent Python loops.

9. Exercises
- Exercise: produce a dict mapping words to their lengths excluding words shorter than 3 chars.
Answer:
```python
words = ['a', 'abc', 'hello']
res = {w: len(w) for w in words if len(w) >= 3}
```

Additional theory — deep dive

- Comprehension scope and name leakage
  - In Python 3, list/dict/set comprehensions have their own implicit scope: loop variables do not leak into the surrounding scope. Generator expressions never created top-level variables in the surrounding scope either.

- Generator vs list comprehension
  - List comprehensions build the entire list in memory. Generator expressions produce values on demand, saving memory for large sequences.

- Readability and complexity
  - Keep comprehensions short and simple. If a comprehension requires multiple nested loops or complex logic, prefer a small helper function or a loop for clarity.

- Alternatives: `map`/`filter` and `itertools`
  - `map` and `filter` can be concise but sometimes less readable with lambdas. `itertools` provides efficient iterator tools for complex operations (`chain`, `islice`, `groupby`).

- Performance tips
  - Use local variables inside comprehensions to avoid global lookups. Use generator expressions when working with streams or when only one pass and low memory overhead is needed.

- Examples
```python
# multiple conditions
res = [x for x in range(100) if x%2==0 and x%3==0]

# enumerate inside comprehension
indexed = [(i, v) for i, v in enumerate(seq)]

# use itertools for flattening deeply nested iterables
from itertools import chain
flat = list(chain.from_iterable(nested))
```

