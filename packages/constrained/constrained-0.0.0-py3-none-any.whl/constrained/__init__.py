from functools import wraps
import inspect
import re
from lark import Lark, UnexpectedCharacters

class FloatType(type):
    def __getitem__(cls, item):
        if isinstance(item, tuple) and len(item) == 2:
            min_value, max_value = item
            if min_value == '-inf':
                min_value = float('-inf')
            if max_value == 'inf':
                max_value = float('inf')
            return type('Float', (Float,), {'MIN_VALUE': min_value, 'MAX_VALUE': max_value})
        else:
            return Float

class Float(float, metaclass=FloatType):
    MIN_VALUE = float('-inf')
    MAX_VALUE = float('inf')

    def __new__(cls, value):
        if cls.MIN_VALUE != float('-inf') or cls.MAX_VALUE != float('inf'):
            if not cls.MIN_VALUE <= value <= cls.MAX_VALUE:
                raise ValueError(f"Value must be between {cls.MIN_VALUE} and {cls.MAX_VALUE}")
        return super().__new__(cls, value)

class IntType(type):
    def __getitem__(cls, item):
        if isinstance(item, tuple) and len(item) == 2:
            min_value, max_value = item
            return type('Int', (Int,), {'MIN_VALUE': min_value, 'MAX_VALUE': max_value})
        else:
            return Int

class Int(int, metaclass=IntType):
    MIN_VALUE = float('-inf')
    MAX_VALUE = float('inf')

    def __new__(cls, value):
        if cls.MIN_VALUE != float('-inf') or cls.MAX_VALUE != float('inf'):
            if not cls.MIN_VALUE <= value <= cls.MAX_VALUE:
                raise ValueError(f"Value must be between {cls.MIN_VALUE} and {cls.MAX_VALUE}")
        return super().__new__(cls, value)

class RegexType(type):
    def __getitem__(cls, item):
        if isinstance(item, str):
            return type('Regex', (Regex,), {'PATTERN': item})
        else:
            raise TypeError("RegexType must be subscripted with a string, e.g., RegexType['pattern']")

class Regex(str, metaclass=RegexType):
    PATTERN = None

    def __new__(cls, value):
        if not re.match(cls.PATTERN, value):
            raise ValueError(f"Value must match the pattern {cls.PATTERN}")
        return super().__new__(cls, value)

class CFGType(type):
    def __getitem__(cls, item):
        if isinstance(item, str):
            return type('CFG', (CFG,), {'GRAMMAR': item})
        else:
            raise TypeError("CFGType must be subscripted with a string, e.g., CFGType['grammar']")

class CFG(str, metaclass=CFGType):
    GRAMMAR = None

    def __new__(cls, value):
        parser = Lark(cls.GRAMMAR, start='start')
        try:
            parser.parse(value)
        except UnexpectedCharacters as e:
            raise ValueError(f"Value must match the grammar {cls.GRAMMAR}")
        return super().__new__(cls, value)

def enforce_annotation_constraints(func):
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound_values = sig.bind(*args, **kwargs)
        bound_values.apply_defaults()

        for name, value in bound_values.arguments.items():
            if name in sig.parameters and sig.parameters[name].annotation is not inspect._empty:  # Corrected here
                param_type = sig.parameters[name].annotation
                if param_type in (Float, Int, Regex, CFG):
                    try:
                        param_type(value)
                    except ValueError as ve:
                        raise ValueError(f"Argument {name} does not match the constraint: {ve}")
                else:
                    if not isinstance(value, param_type):
                        raise ValueError(f"Argument {name} does not match the type: {param_type}")

        retval = func(*args, **kwargs)
        if 'return' in sig.annotations:
            return_type = sig.annotations['return']
            if return_type in (Float, Int, Regex, CFG):
                try:
                    return_type(retval)
                except ValueError as ve:
                    raise ValueError(f"Return value does not match the constraint: {ve}")
            else:
                if not isinstance(retval, return_type):
                    raise ValueError(f"Return value does not match the type: {return_type}")

        return retval

    return wrapper
