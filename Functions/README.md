Functions in Python — Notes & Examples
====================================

Overview
- Functions package logic into named blocks. They improve readability, reuse, and testability.

1. Defining functions
```python
def greet(name):
    """Return a greeting for name."""
    return f'Hello, {name}'
```

2. Arguments
- Positional, keyword, default values, variable-length `*args` and `**kwargs`.
```python
def f(a, b=2, *args, **kwargs):
    pass
```

3. Annotations (optional)
```python
def add(a: int, b: int) -> int:
    return a + b
```

4. Lambda (anonymous) functions
```python
square = lambda x: x*x
```

5. Closures and higher-order functions
```python
def make_multiplier(n):
    def mul(x):
        return x * n
    return mul

double = make_multiplier(2)
```

6. Decorators
- Wrap or modify functions; use `functools.wraps` to preserve metadata.
```python
from functools import wraps
def timer(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        import time
        t0 = time.time()
        res = fn(*a, **kw)
        print('elapsed', time.time()-t0)
        return res
    return wrapper

@timer
def work(n):
    return sum(range(n))
```

7. Recursion
- Use for tree-like structures; be mindful of recursion limits and prefer iterative solutions for deep recursion.
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```

8. Docstrings and testing
- Include docstrings and examples; use `doctest` or unit tests to validate behavior.

9. Examples
- Flexible function with `*args`/`**kwargs`:
```python
def info(*args, **kwargs):
    print('positional:', args)
    print('keywords:', kwargs)
```

10. Exercises
- Exercise: write `flatten(lst)` that flattens one level of nested lists.
Answer:
```python
def flatten(lst):
    out = []
    for sub in lst:
        out.extend(sub)
    return out
```

Additional theory — deep dive

- Argument types in detail
  - Positional-only (`/`) and keyword-only (`*`) parameters (Python 3.8+):
    ```python
    def func(a, b, /, c, *, d):
        pass
    # a and b must be positional; d must be keyword
    ```
  - Mutable default argument gotcha: default values are evaluated once at function definition time. Use `None` sentinel for mutable defaults.
    ```python
    def add_to(item, lst=None):
        if lst is None:
            lst = []
        lst.append(item)
        return lst
    ```

- Function tools: `functools`
  - `lru_cache` for memoization: good for expensive pure functions.
  - `partial` to bind arguments and return a new callable.

- Generator functions and `yield`
  - `def gen(): yield x` creates an iterator; use `next()` or iterate in a loop. Generators are memory-efficient.
  - `send()` can be used to push values into a generator; `yield from` delegates to subgenerator.

- Async functions (brief)
  - `async def` defines a coroutine; use `await` to call other coroutines. Requires an event loop (e.g., `asyncio`).

- Closures and scoping
  - Functions capture variables from enclosing scopes. Be careful with late binding in closures inside loops; use default arguments to bind current value.

```python
funcs = [lambda x, n=n: x+n for n in range(3)]
```

- Introspection & `inspect`
  - Use `inspect.signature()` to examine parameters and annotations at runtime.

- Docstrings, typing, and testing
  - Follow PEP 257 for docstrings; include examples for `doctest` where helpful.
  - Use type hints and `typing.Callable`, `typing.Protocol` to document expected callables.

- Examples
  - Memoized Fibonacci with `lru_cache`:
  ```python
  from functools import lru_cache
  @lru_cache(maxsize=None)
  def fib(n):
      if n < 2:
          return n
      return fib(n-1) + fib(n-2)
  ```

