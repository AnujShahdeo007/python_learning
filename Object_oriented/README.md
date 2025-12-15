Object-Oriented Programming in Python — Notes & Examples
======================================================

Overview
- Python supports object-oriented programming (OOP) with classes and objects.
- Key concepts: encapsulation, inheritance, polymorphism, composition.

1. Defining a class
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hello, {self.name}'
```

2. Instance vs class attributes
```python
class C:
    kind = 'example'  # class attribute
    def __init__(self, v):
        self.v = v      # instance attribute
```

3. Inheritance and `super()`
```python
class Employee(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role
```

4. Method types
- Instance methods: use `self`.
- Class methods: use `@classmethod` and `cls`.
- Static methods: use `@staticmethod` for utility functions.

5. Properties
- Use `@property` to create managed attributes.
```python
class Circle:
    def __init__(self, r):
        self._r = r
    @property
    def radius(self):
        return self._r
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError
        self._r = value
```

6. Dunder methods (special methods)
- `__repr__`, `__str__`, `__eq__`, `__len__`, `__iter__` — implement behaviour for built-ins.
```python
class V:
    def __repr__(self):
        return '<V>'
```

7. Composition over inheritance
- Prefer composing small objects rather than deep inheritance hierarchies.

8. Dataclasses (Python 3.7+)
```python
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
```

9. Examples
- Simple polymorphism:
```python
class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return 'woof'

class Cat(Animal):
    def speak(self):
        return 'meow'

for a in (Dog(), Cat()):
    print(a.speak())
```

10. Exercises
- Exercise: implement a `Stack` class (LIFO) with `push`, `pop`, `peek`, and length support.
Answer (simple):
```python
class Stack:
    def __init__(self):
        self._items = []
    def push(self, x):
        self._items.append(x)
    def pop(self):
        return self._items.pop()
    def peek(self):
        return self._items[-1]
    def __len__(self):
        return len(self._items)
```

Additional theory — deep dive

- Encapsulation and name mangling
  - Python does not enforce strict private attributes; prefixing with `_` signals internal use. Double-underscore attributes (`__name`) are name-mangled to `_ClassName__name` to avoid accidental overrides.

- Method Resolution Order (MRO) and multiple inheritance
  - Python uses C3 linearization to determine MRO. `super()` follows the MRO chain, so use `super()` consistently in cooperative multiple inheritance.
  - Beware the diamond problem — design classes carefully and prefer composition when appropriate.

- Abstract base classes and protocols
  - Use `abc.ABC` and `@abstractmethod` to define abstract interfaces.
  - In typing, `Protocol` (PEP 544) allows structural subtyping (duck typing with type checking).

- Descriptors and properties
  - Properties are a user-friendly descriptor. Descriptors (with `__get__`, `__set__`) let you build reusable attribute behavior.

- `__slots__` for memory optimization
  - Defining `__slots__` prevents creation of `__dict__` per instance and reduces memory overhead, but restricts dynamic attribute assignment.

- Object equality and hashing
  - Implement `__eq__` and `__hash__` carefully. If instances compare equal, their hashes must match for use in sets/dicts. Immutable types are suitable for hashing.

- Dataclasses advanced
  - `@dataclass` supports `frozen=True` for immutability, `order=True` to generate ordering methods, `field(default_factory=...)` for mutable defaults.

- Metaclasses (overview)
  - Metaclasses customize class creation. They are advanced — prefer simpler patterns unless you need to modify class construction.

- Example: abstract base class and dataclass
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

@dataclass(frozen=True)
class Square(Shape):
    side: float
    def area(self):
        return self.side * self.side
```

-- End Expanded OOP --
