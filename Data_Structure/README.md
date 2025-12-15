Data Structures in Python — Notes & Examples
===========================================

Overview
- Built-in core data structures: `list`, `tuple`, `set`, `dict`.
- Other useful structures: `deque` (collections), `namedtuple`, `defaultdict`, `Counter`.
- Choose a structure based on mutability, ordering, and lookup complexity.

1. List
- Mutable ordered sequence. Good for indexed access, append/pop operations.
- Common ops: `append`, `extend`, `insert`, `pop`, `remove`, `index`, `count`, `sort`, `reverse`, slicing.

Example:
```python
lst = [1, 2, 3]
lst.append(4)
sub = lst[1:3]  # [2,3]
for i, v in enumerate(lst):
    print(i, v)
```
Complexities: indexing O(1), append amortized O(1), insert/remove at middle O(n).

2. Tuple
- Immutable ordered sequence. Use for fixed collections and as dictionary keys.

Example:
```python
t = (1, 'a')
# single element tuple: (1,)
```

3. Set
- Unordered collection of unique items. Fast membership tests (avg O(1)).
- Useful for deduplication and set algebra: `union`, `intersection`, `difference`, `symmetric_difference`.

Example:
```python
s = {1, 2, 3}
s.add(4)
common = s & {2, 4, 6}
```

4. Dict (dictionary)
- Key-value mapping. Fast lookup by key (avg O(1)). Keys must be hashable.

Example:
```python
d = {'a': 1, 'b': 2}
d['c'] = 3
for k, v in d.items():
    print(k, v)
```

5. Useful `collections` helpers
- `deque`: fast appends/pops from both ends.
```python
from collections import deque
q = deque([1, 2, 3])
q.appendleft(0)
q.pop()
```
- `defaultdict`: default factory for missing keys.
```python
from collections import defaultdict
dd = defaultdict(list)
dd['x'].append(1)
```
- `namedtuple`: lightweight immutable record with named fields.
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
```
- `Counter`: frequency counts.
```python
from collections import Counter
cnt = Counter(['a', 'b', 'a'])  # Counter({'a':2, 'b':1})
```

6. When to use which
- Use `list` for ordered collections you will mutate.
- Use `tuple` for fixed collections or as dict keys.
- Use `set` for membership and deduplication.
- Use `dict` for mapping and lookups.
- Use `deque` for queues where you need O(1) pops from left.

7. Performance notes
- Prefer list comprehensions over appending in a loop for speed and readability.
- Avoid nested loops on large lists; prefer set/dict lookups.

8. Examples — common patterns
- Intersect two lists efficiently:
```python
def intersect(a, b):
    return list(set(a) & set(b))
```
- Group items by key using `defaultdict`:
```python
from collections import defaultdict
groups = defaultdict(list)
items = [('a', 1), ('b', 2), ('a', 3)]
for k, v in items:
    groups[k].append(v)
```

9. Exercises (answers included)
- Exercise: Remove duplicates while preserving order.
Answer:
```python
def dedupe_preserve(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
```

-- End --

Additional theory — deep dive

- Memory & mutability
  - `list` is mutable; `tuple` is immutable. Immutable objects can be used as dict keys and are safer to share across code.
  - Shallow vs deep copy: `list.copy()` or `copy.copy()` makes a shallow copy — nested mutable objects are still shared. Use `copy.deepcopy()` to fully copy nested structures.

- Slicing and views
  - Slicing a list (`lst[a:b]`) creates a new list (copy). For large datasets this is O(k) where k is slice length.

- Sorting and ordering
  - `list.sort()` sorts in-place; `sorted()` returns a new list.
  - Both accept `key` and `reverse` arguments. The sort is stable (preserves order of equal keys).
  - To sort by multiple criteria, return a tuple from `key`, e.g., `key=lambda x: (x.score, -x.age)`.

- Searching & bisect
  - For sorted lists, use the `bisect` module (`bisect_left`, `bisect_right`) for O(log n) insert/search positions.

- Heaps & priority queues
  - Use `heapq` for an efficient min-heap. `heapq.heappush()` and `heapq.heappop()` are O(log n).

- When to prefer other structures
  - If you need fast ordered mapping: use `collections.OrderedDict` (Py3.7+ regular `dict` preserves insertion order).
  - For memory-sensitive numeric arrays, use `array.array` or `numpy.ndarray` (NumPy) instead of Python lists.

- Example: shallow vs deep copy
```python
import copy
orig = [[1,2], [3,4]]
sh = orig.copy()
dd = copy.deepcopy(orig)
orig[0].append(9)
print(sh)  # inner lists shared -> also shows 9
print(dd)  # unaffected
```

