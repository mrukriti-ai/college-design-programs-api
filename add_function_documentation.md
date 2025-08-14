# Add Function Documentation

## Overview

The `add_function.py` module provides a comprehensive set of addition functions with robust error handling, type hints, and extensive documentation. This module is designed to be both educational and production-ready.

## Features

- ✅ **Type Hints**: Full type annotation support for better IDE integration
- ✅ **Error Handling**: Comprehensive error handling for edge cases
- ✅ **Multiple Variants**: Different add functions for various use cases
- ✅ **Documentation**: Extensive docstrings with examples
- ✅ **Edge Case Handling**: Proper handling of NaN, infinity, and special values
- ✅ **Demo Script**: Built-in demonstration of all functions

## Functions

### 1. `add(a, b)`

The core addition function that adds two numbers together.

**Signature:**
```python
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
```

**Parameters:**
- `a` (Union[int, float]): The first number to add
- `b` (Union[int, float]): The second number to add

**Returns:**
- Union[int, float]: The sum of a and b

**Examples:**
```python
>>> add(5, 3)
8
>>> add(3.14, 2.86)
6.0
>>> add(-5, 10)
5
>>> add(0, 0)
0
```

**Error Cases:**
```python
>>> add("5", 3)
TypeError: Both arguments must be numbers (int or float)
>>> add(float('nan'), 5)
ValueError: Cannot add NaN values
```

### 2. `add_multiple(*args)`

Adds multiple numbers together using variable arguments.

**Signature:**
```python
def add_multiple(*args: Union[int, float]) -> Union[int, float]:
```

**Parameters:**
- `*args` (Union[int, float]): Variable number of numbers to add

**Returns:**
- Union[int, float]: The sum of all provided numbers

**Examples:**
```python
>>> add_multiple(1, 2, 3, 4, 5)
15
>>> add_multiple(1.5, 2.5, 3.0)
7.0
>>> add_multiple(10)
10
```

**Error Cases:**
```python
>>> add_multiple()
ValueError: At least one number must be provided
>>> add_multiple(1, "2", 3)
TypeError: All arguments must be numbers, got str
```

### 3. `add_list(numbers)`

Adds all numbers in a list.

**Signature:**
```python
def add_list(numbers: List[Union[int, float]]) -> Union[int, float]:
```

**Parameters:**
- `numbers` (List[Union[int, float]]): List of numbers to add

**Returns:**
- Union[int, float]: The sum of all numbers in the list

**Examples:**
```python
>>> add_list([1, 2, 3, 4, 5])
15
>>> add_list([1.5, 2.5, 3.0])
7.0
```

**Error Cases:**
```python
>>> add_list([])
ValueError: List cannot be empty
>>> add_list([1, "2", 3])
TypeError: All arguments must be numbers, got str
```

### 4. `add_with_rounding(a, b, decimal_places=2)`

Adds two numbers and rounds the result to specified decimal places.

**Signature:**
```python
def add_with_rounding(a: Union[int, float], b: Union[int, float], 
                     decimal_places: int = 2) -> float:
```

**Parameters:**
- `a` (Union[int, float]): The first number to add
- `b` (Union[int, float]): The second number to add
- `decimal_places` (int, optional): Number of decimal places to round to. Defaults to 2.

**Returns:**
- float: The rounded sum of a and b

**Examples:**
```python
>>> add_with_rounding(3.14159, 2.71828)
5.86
>>> add_with_rounding(3.14159, 2.71828, 4)
5.8599
>>> add_with_rounding(5, 3, 0)
8.0
```

**Error Cases:**
```python
>>> add_with_rounding(1, 2, -1)
ValueError: decimal_places cannot be negative
>>> add_with_rounding(1, 2, "2")
TypeError: decimal_places must be an integer
```

## Usage Examples

### Basic Usage

```python
from add_function import add, add_multiple, add_list, add_with_rounding

# Simple addition
result = add(10, 20)  # Returns 30

# Multiple number addition
total = add_multiple(1, 2, 3, 4, 5)  # Returns 15

# List addition
numbers = [1.5, 2.5, 3.0, 4.0]
sum_result = add_list(numbers)  # Returns 11.0

# Addition with rounding
rounded = add_with_rounding(3.14159, 2.71828, 3)  # Returns 5.860
```

### Error Handling

```python
try:
    result = add("5", 3)
except TypeError as e:
    print(f"Error: {e}")  # Error: Both arguments must be numbers (int or float)

try:
    result = add_multiple()
except ValueError as e:
    print(f"Error: {e}")  # Error: At least one number must be provided

try:
    result = add_list([])
except ValueError as e:
    print(f"Error: {e}")  # Error: List cannot be empty
```

### Advanced Usage

```python
# Working with different numeric types
int_result = add(5, 3)  # Returns int: 8
float_result = add(3.14, 2.86)  # Returns float: 6.0
mixed_result = add(5, 3.5)  # Returns float: 8.5

# Handling edge cases
zero_result = add(0, 0)  # Returns 0
negative_result = add(-5, 10)  # Returns 5

# Multiple operations
numbers = [1, 2, 3, 4, 5]
total = add_list(numbers)  # Returns 15
rounded_total = add_with_rounding(total, 0.5, 1)  # Returns 15.5
```

## Edge Cases and Special Values

### Infinity Handling

```python
import math

# Adding infinity
inf_result = add(math.inf, 5)  # Returns inf
neg_inf_result = add(-math.inf, 5)  # Returns -inf

# Adding positive and negative infinity
try:
    result = add(math.inf, -math.inf)
except ValueError as e:
    print(f"Error: {e}")  # Error: Cannot add positive and negative infinity
```

### NaN Handling

```python
import math

# Adding NaN
try:
    result = add(math.nan, 5)
except ValueError as e:
    print(f"Error: {e}")  # Error: Cannot add NaN values
```

### Type Conversion

```python
# Integer results for whole numbers
result = add(5.0, 3.0)  # Returns int: 8

# Float results for decimal numbers
result = add(5.5, 3.5)  # Returns float: 9.0
```

## Best Practices

### 1. Type Checking

Always use type hints when calling the functions:

```python
from typing import Union

def my_function(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return add(a, b)
```

### 2. Error Handling

Always wrap function calls in try-except blocks for production code:

```python
def safe_add(a, b):
    try:
        return add(a, b)
    except (TypeError, ValueError) as e:
        print(f"Addition failed: {e}")
        return None
```

### 3. Input Validation

Validate inputs before calling the functions:

```python
def validate_and_add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return add(a, b)
```

### 4. Performance Considerations

- For large lists, `add_list()` is more efficient than `add_multiple(*list)`
- The functions are optimized for common use cases
- Type checking adds minimal overhead

## Testing

The module includes built-in demonstration code. To run the demo:

```bash
python add_function.py
```

Expected output:
```
🧮 Add Function Demonstration
========================================
Basic Addition:
add(5, 3) = 8
add(3.14, 2.86) = 6.0
add(-5, 10) = 5
add(0, 0) = 0

Multiple Number Addition:
add_multiple(1, 2, 3, 4, 5) = 15
add_multiple(1.5, 2.5, 3.0) = 7.0

List Addition:
add_list([1, 2, 3, 4, 5]) = 15
add_list([1.5, 2.5, 3.0]) = 7.0

Addition with Rounding:
add_with_rounding(3.14159, 2.71828) = 5.86
add_with_rounding(3.14159, 2.71828, 4) = 5.8599

Error Handling Examples:
TypeError caught: Both arguments must be numbers (int or float)
ValueError caught: At least one number must be provided
ValueError caught: List cannot be empty

✅ Add function demonstration completed!
```

## Dependencies

The module requires Python 3.6+ and uses only standard library modules:

- `typing`: For type hints
- `math`: For mathematical operations and special value checking

## License

This code is provided as-is for educational and development purposes.

## Contributing

To extend this module:

1. Add new functions following the same documentation pattern
2. Include type hints for all parameters and return values
3. Add comprehensive error handling
4. Include docstring examples
5. Update this documentation file
6. Test with the demo script

## Version History

- **v1.0**: Initial release with core add functions
  - Basic addition with type hints
  - Multiple number addition
  - List addition
  - Addition with rounding
  - Comprehensive error handling
  - Full documentation 