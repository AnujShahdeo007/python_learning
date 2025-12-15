File Handling in Python — Notes & Examples
=========================================

Overview
- Reading and writing files is common; use built-in `open()` or `pathlib.Path` for higher-level operations.
- Always close files; prefer the `with` statement (context manager).

1. Opening files
- Modes: `'r'` (read), `'w'` (write, truncate), `'a'` (append), `'x'` (create), and `'b'` (binary), `'t'` (text).
```python
f = open('file.txt', 'r', encoding='utf-8')
f.close()
```

2. Recommended pattern: `with`
```python
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write('hello')
```

3. Reading methods
- `read()` reads whole file, `readline()` reads single line, `readlines()` returns list of lines, iterating `for line in f:` is memory-efficient.

4. Writing methods
- `write()` and `writelines()`; remember to add newlines when needed.

5. Binary files
- Use `'rb'`/`'wb'` for images, pickles, etc. Do not specify encoding for binary.

6. CSV and JSON
- CSV: use `csv` module for proper quoting and parsing.
```python
import csv
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
```
- JSON: use `json` module.
```python
import json
data = {'a': 1}
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
```

7. Pathlib (recommended modern API)
```python
from pathlib import Path
p = Path('some/file.txt')
text = p.read_text(encoding='utf-8')
p.write_text('hello', encoding='utf-8')
```

8. Safely creating directories
```python
from pathlib import Path
Path('out/dir').mkdir(parents=True, exist_ok=True)
```

9. File permissions and os module
- Use `os.remove()`, `os.rename()`, `os.replace()` for file operations; check `os.stat()` for metadata.

10. Examples
- Read large file line-by-line and process streaming:
```python
def process(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            do_work(line)
```

11. Exercises
- Exercise: Count lines in a file without loading entire file into memory.
Answer:
```python
def count_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)
```

Additional theory — deep dive

- File encodings & newline handling
  - Always specify `encoding='utf-8'` when working with text to avoid platform differences.
  - Python supports universal newlines by default in text mode; you can control newline translation with the `newline` parameter.

- Buffering & performance
  - `open()` has a `buffering` parameter; text files are buffered by default. For large binary reads consider `mmap` or reading in chunks.

- Seek & tell
  - `f.seek(offset, whence)` moves the file cursor; `f.tell()` returns the current position. Useful for random access in binary files.

- Atomic writes & safety
  - To avoid corrupting files, write to a temporary file and `os.replace()` (atomic on many OSes) to move into place.

- Pickle & binary serialization
  - `pickle` serializes Python objects but is not secure with untrusted data. Prefer JSON or specialized formats for interoperability.

- Temporary files and directories
  - Use `tempfile.TemporaryDirectory()` and `tempfile.NamedTemporaryFile()` for safe temp work.

- Working with compressed files
  - Use `gzip.open()`, `bz2.open()`, or `zipfile` to read/write compressed data transparently.

- Memory-mapped files
  - `mmap` module lets you access file contents like a bytearray without reading it wholly into memory.

- File locking and concurrency
  - Python has no cross-platform builtin file lock; use `fcntl` on Unix or `msvcrt` on Windows, or a third-party library (e.g., `filelock`) for portability.

- shutil utilities
  - `shutil.copy`, `shutil.copytree`, `shutil.move`, and `shutil.rmtree` are higher-level helpers for filesystem operations.

- Example: atomic write
```python
from pathlib import Path
import tempfile
def atomic_write(path: Path, data: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile('w', delete=False, dir=path.parent, encoding='utf-8') as tmp:
        tmp.write(data)
    tmp_path = Path(tmp.name)
    tmp_path.replace(path)
```

-- End Expanded File Handling --
