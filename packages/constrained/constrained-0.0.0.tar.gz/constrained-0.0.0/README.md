# Constrained

:caution: **Not working; not maintained. Use [annotated-types](https://github.com/annotated-types/annotated-types) instead.** :caution:

A Python library for enforcing type and range constraints.

## Features

- Float and Int types with range constraints
- Regex type for string matching
- CFG type for context-free grammar matching
- enforce_annotation_constraints decorator to enforce constraints

## Installation

```bash
pip install constrained
```

## Usage

First, import the necessary types and the decorator from the `constrained` module:

```python
from constrained import Float, Int, Regex, CFG, enforce_annotation_constraints
```

Then, define your function with type annotations:

```python
@enforce_annotation_constraints
def P(x: Float[0, 'inf']) -> Float[0, 'inf']:
    return x / 2
```

The decorator will enforce the constraints at runtime and raise a ValueError if any argument or the return value does not match the constraints defined in the function's signature.

## Alternatives

- [annotated-types](https://github.com/annotated-types/annotated-types) (much better than `constrained` and up-to-date (08/2023); `pip install annotated-types`)
- [Constrained Types](https://pypi.org/project/constrained_types/)
