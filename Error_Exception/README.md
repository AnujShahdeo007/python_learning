Error & Exception Handling in Python — Notes & Examples
======================================================

Overview
- Exceptions are runtime errors represented by classes derived from `BaseException` (commonly `Exception`).
- Use `try`/`except` to handle expected error conditions and keep the program robust.

1. Basic `try`/`except`
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')
```

2. Catch multiple exceptions
```python
try:
    ...
except (ValueError, TypeError) as e:
    print('Bad input:', e)
```

3. `else` and `finally`
- `else` runs when no exception occurs. `finally` always runs (for cleanup).
```python
try:
    val = int(user_input)
except ValueError:
    print('invalid')
else:
    print('valid integer', val)
finally:
    print('cleanup actions')
```

4. Raising exceptions
```python
def positive(n):
    if n < 0:
        raise ValueError('n must be non-negative')
```

5. Custom exceptions
```python
class MyError(Exception):
    pass
raise MyError('something bad')
```

6. Best practices
- Catch the most specific exception possible.
- Avoid bare `except:`; prefer `except Exception:` if you must.
- Use `finally` or context managers to release resources.
- Use exceptions for exceptional conditions, not normal control flow.

7. Context managers for safety (`with`)
```python
with open('file.txt', 'r') as f:
    data = f.read()
```
This ensures file is closed even on error.

8. Logging and debugging
- Use the `logging` module instead of `print` in production.
- Use `traceback` or `logging.exception()` to capture stack traces.

9. Examples
- Retrying on failure:
```python
import time
for attempt in range(3):
    try:
        do_network_call()
        break
    except NetworkError:
        time.sleep(1)
else:
    raise RuntimeError('All retries failed')
```

10. Exercises
- Exercise: write `safe_int(s, default=None)` that returns `int(s)` or `default` without raising.
Answer:
```python
def safe_int(s, default=None):
    try:
        return int(s)
    except (TypeError, ValueError):
        return default
```

Additional theory — deep dive

- Exception hierarchy and important built-ins
  - `BaseException` is the root; most user-level exceptions inherit from `Exception`.
  - `SystemExit`, `KeyboardInterrupt`, and `GeneratorExit` inherit directly from `BaseException` — avoid catching `BaseException` unless you really mean to handle these signals.

- Exception chaining and context
  - Use `raise NewExc(...) from original_exc` to chain exceptions and preserve context.
  - Python automatically sets `__context__` when an exception is raised during handling of another exception.

```python
try:
    1 / 0
except ZeroDivisionError as e:
    raise ValueError('bad input') from e
```

- Re-raising exceptions
  - Use `raise` inside an `except` block to re-raise the same exception and preserve the original traceback.

- Suppressing exceptions intentionally
  - `contextlib.suppress(*exceptions)` can be used to ignore expected exceptions concisely.

```python
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove('maybe_missing.txt')
```

- Assertions vs exceptions
  - `assert` is a debugging aid; it can be disabled with Python optimizations (`-O`). Do not rely on it for runtime validation in production.

- Exception messages and debugging
  - Include useful information in exception messages (values, identifiers) but avoid exposing secrets.
  - Use `logging.exception()` in `except` blocks to log stack traces.

- Designing custom exceptions
  - Derive from a meaningful base (e.g., `MyLibError(Exception)`); keep exception classes small and focused.

- Example: preserving traceback while adding context
```python
try:
    data = json.loads(s)
except json.JSONDecodeError as e:
    raise ValueError('invalid configuration data') from e
```


