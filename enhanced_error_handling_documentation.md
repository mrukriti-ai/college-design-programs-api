# Enhanced Add Function with Comprehensive Error Handling

## Overview

The `add_function_enhanced.py` module provides a production-ready add function with extensive error handling capabilities. This enhanced version includes custom exception classes, logging, overflow protection, precision limits, and performance monitoring.

## Key Features

### 🔒 **Comprehensive Error Handling**
- Custom exception classes for different error types
- Input validation with detailed error messages
- Overflow protection using Decimal arithmetic
- Precision limit enforcement
- Performance monitoring and warnings

### 📊 **Logging and Monitoring**
- Detailed logging for debugging and monitoring
- Performance tracking with execution time measurement
- Warning system for potential issues
- Configurable logging levels

### 🛡️ **Safety Features**
- Safe addition function that returns None on errors
- Retry mechanism for transient errors
- Input sanitization and validation
- Overflow detection and prevention

## Custom Exception Classes

### `AddFunctionError`
Base exception class for all add function errors.

### `InputValidationError`
Raised when input validation fails:
- None values
- Non-numeric types
- NaN values
- Invalid data types

### `OverflowError`
Raised when addition would cause overflow:
- Extremely large numbers
- Decimal overflow
- Underflow conditions

### `PrecisionError`
Raised when precision limits are exceeded:
- Too many decimal places
- Floating-point precision issues

### `PerformanceWarning`
Warning for performance issues:
- Slow execution times
- Resource-intensive operations

## Functions

### 1. `add_with_enhanced_error_handling()`

The main enhanced addition function with comprehensive error handling.

**Signature:**
```python
def add_with_enhanced_error_handling(
    a: Union[int, float], 
    b: Union[int, float],
    max_precision: int = 15,
    enable_overflow_check: bool = True,
    enable_logging: bool = True
) -> Union[int, float]:
```

**Parameters:**
- `a` (Union[int, float]): First number to add
- `b` (Union[int, float]): Second number to add
- `max_precision` (int): Maximum decimal places allowed (default: 15)
- `enable_overflow_check` (bool): Enable overflow checking (default: True)
- `enable_logging` (bool): Enable logging (default: True)

**Returns:**
- Union[int, float]: The sum of a and b

**Error Handling:**
```python
try:
    result = add_with_enhanced_error_handling(5, 3)
    print(f"Result: {result}")
except InputValidationError as e:
    print(f"Input error: {e}")
except OverflowError as e:
    print(f"Overflow error: {e}")
except PrecisionError as e:
    print(f"Precision error: {e}")
except PerformanceWarning as e:
    print(f"Performance warning: {e}")
```

### 2. `add_multiple_with_error_handling()`

Adds multiple numbers with comprehensive error handling.

**Signature:**
```python
def add_multiple_with_error_handling(
    *args: Union[int, float],
    max_precision: int = 15,
    enable_overflow_check: bool = True,
    enable_logging: bool = True
) -> Union[int, float]:
```

**Usage:**
```python
# Add multiple numbers
result = add_multiple_with_error_handling(1, 2, 3, 4, 5)

# With custom precision
result = add_multiple_with_error_handling(1.123456, 2.234567, max_precision=3)

# Without logging
result = add_multiple_with_error_handling(1, 2, 3, enable_logging=False)
```

### 3. `safe_add()`

Safe addition that returns None on error instead of raising exceptions.

**Signature:**
```python
def safe_add(a: Union[int, float], b: Union[int, float]) -> Optional[Union[int, float]]:
```

**Usage:**
```python
# Safe addition that won't crash
result = safe_add(5, 3)
if result is not None:
    print(f"Result: {result}")
else:
    print("Addition failed")

# With invalid input
result = safe_add("5", 3)  # Returns None
```

### 4. `add_with_retry()`

Adds numbers with retry mechanism for transient errors.

**Signature:**
```python
def add_with_retry(
    a: Union[int, float], 
    b: Union[int, float], 
    max_retries: int = 3,
    delay: float = 0.1
) -> Union[int, float]:
```

**Usage:**
```python
# With default retry settings
result = add_with_retry(5, 3)

# With custom retry settings
result = add_with_retry(5, 3, max_retries=5, delay=0.5)
```

## Error Handling Examples

### Input Validation Errors

```python
# None values
try:
    add_with_enhanced_error_handling(None, 5)
except InputValidationError as e:
    print(e)  # First argument cannot be None

# Non-numeric types
try:
    add_with_enhanced_error_handling("5", 3)
except InputValidationError as e:
    print(e)  # First argument must be a number (int or float), got str

# NaN values
try:
    add_with_enhanced_error_handling(float('nan'), 5)
except InputValidationError as e:
    print(e)  # First argument cannot be NaN
```

### Overflow Errors

```python
# Extremely large numbers
try:
    add_with_enhanced_error_handling(1e308, 1e308)
except OverflowError as e:
    print(e)  # Addition would result in overflow

# Disable overflow checking
result = add_with_enhanced_error_handling(1e308, 1e308, enable_overflow_check=False)
```

### Precision Errors

```python
# Too many decimal places
try:
    add_with_enhanced_error_handling(1.123456789012345, 2.234567890123456, max_precision=5)
except PrecisionError as e:
    print(e)  # Result has 15 decimal places, maximum allowed is 5
```

### Performance Warnings

```python
# Slow operation (simulated)
import time

def slow_add(a, b):
    time.sleep(0.2)  # Simulate slow operation
    return a + b

# This would trigger a performance warning
try:
    result = add_with_enhanced_error_handling(5, 3)
except PerformanceWarning as e:
    print(e)  # Addition took 0.2000 seconds
```

## Logging Configuration

### Basic Logging Setup

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('add_function.log'),
        logging.StreamHandler()
    ]
)
```

### Custom Logging Levels

```python
# Set different logging levels
logging.getLogger(__name__).setLevel(logging.DEBUG)

# Disable logging for specific operations
result = add_with_enhanced_error_handling(5, 3, enable_logging=False)
```

### Log Output Examples

```
2024-01-15 10:30:15,123 - INFO - Adding numbers: 5 + 3
2024-01-15 10:30:15,124 - INFO - Addition completed: 5 + 3 = 8 (took 0.000123s)
2024-01-15 10:30:15,125 - WARNING - First argument is extremely large: 1e308
2024-01-15 10:30:15,126 - ERROR - Error in addition: First argument cannot be None
```

## Best Practices

### 1. Error Handling Strategy

```python
def robust_addition(a, b):
    """Robust addition with comprehensive error handling"""
    try:
        # Try enhanced addition first
        return add_with_enhanced_error_handling(a, b)
    except InputValidationError:
        # Try to convert inputs
        try:
            a_conv = float(a) if isinstance(a, str) else a
            b_conv = float(b) if isinstance(b, str) else b
            return add_with_enhanced_error_handling(a_conv, b_conv)
        except (ValueError, TypeError):
            return None
    except OverflowError:
        # Use safe addition for overflow cases
        return safe_add(a, b)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return None
```

### 2. Performance Monitoring

```python
def monitored_addition(a, b, threshold=0.1):
    """Addition with performance monitoring"""
    start_time = time.time()
    
    try:
        result = add_with_enhanced_error_handling(a, b, enable_logging=False)
        execution_time = time.time() - start_time
        
        if execution_time > threshold:
            logger.warning(f"Slow addition: {execution_time:.4f}s")
        
        return result
    except Exception as e:
        logger.error(f"Addition failed after {time.time() - start_time:.4f}s: {e}")
        raise
```

### 3. Batch Processing with Error Recovery

```python
def batch_add(numbers_list, max_retries=3):
    """Add multiple lists of numbers with error recovery"""
    results = []
    
    for numbers in numbers_list:
        try:
            result = add_multiple_with_error_handling(*numbers)
            results.append(result)
        except Exception as e:
            logger.warning(f"Batch addition failed: {e}")
            # Try with retry mechanism
            try:
                result = add_with_retry(*numbers, max_retries=max_retries)
                results.append(result)
            except Exception as retry_error:
                logger.error(f"Retry failed: {retry_error}")
                results.append(None)
    
    return results
```

### 4. Configuration Management

```python
class AddFunctionConfig:
    """Configuration for add function behavior"""
    
    def __init__(self):
        self.max_precision = 15
        self.enable_overflow_check = True
        self.enable_logging = True
        self.performance_threshold = 0.1
        self.max_retries = 3
        self.retry_delay = 0.1

def configured_add(a, b, config: AddFunctionConfig):
    """Add with custom configuration"""
    return add_with_enhanced_error_handling(
        a, b,
        max_precision=config.max_precision,
        enable_overflow_check=config.enable_overflow_check,
        enable_logging=config.enable_logging
    )
```

## Testing and Validation

### Unit Test Examples

```python
import unittest

class TestEnhancedAddFunction(unittest.TestCase):
    
    def test_basic_addition(self):
        result = add_with_enhanced_error_handling(5, 3)
        self.assertEqual(result, 8)
    
    def test_input_validation(self):
        with self.assertRaises(InputValidationError):
            add_with_enhanced_error_handling(None, 5)
        
        with self.assertRaises(InputValidationError):
            add_with_enhanced_error_handling("5", 3)
    
    def test_overflow_protection(self):
        with self.assertRaises(OverflowError):
            add_with_enhanced_error_handling(1e308, 1e308)
    
    def test_safe_addition(self):
        result = safe_add(5, 3)
        self.assertEqual(result, 8)
        
        result = safe_add("5", 3)
        self.assertIsNone(result)
    
    def test_retry_mechanism(self):
        result = add_with_retry(5, 3, max_retries=2)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()
```

### Integration Testing

```python
def integration_test():
    """Comprehensive integration test"""
    test_cases = [
        # Valid cases
        (5, 3, 8),
        (3.14, 2.86, 6.0),
        (-5, 10, 5),
        (0, 0, 0),
        
        # Edge cases
        (1e15, 1e15, 2e15),
        (float('inf'), 5, float('inf')),
        (-float('inf'), 5, -float('inf')),
    ]
    
    for a, b, expected in test_cases:
        try:
            result = add_with_enhanced_error_handling(a, b)
            assert result == expected, f"Expected {expected}, got {result}"
            print(f"✅ {a} + {b} = {result}")
        except Exception as e:
            print(f"❌ {a} + {b}: {e}")
```

## Performance Considerations

### Optimization Tips

1. **Disable Logging for High-Frequency Operations**
   ```python
   # For performance-critical code
   result = add_with_enhanced_error_handling(a, b, enable_logging=False)
   ```

2. **Use Safe Addition for Non-Critical Operations**
   ```python
   # When errors are acceptable
   result = safe_add(a, b)
   if result is None:
       # Handle error gracefully
       pass
   ```

3. **Batch Operations**
   ```python
   # More efficient than individual calls
   result = add_multiple_with_error_handling(*numbers)
   ```

4. **Configure Precision Limits**
   ```python
   # Reduce precision for better performance
   result = add_with_enhanced_error_handling(a, b, max_precision=5)
   ```

## Troubleshooting

### Common Issues and Solutions

1. **Performance Warnings**
   - Reduce precision limits
   - Disable overflow checking for known-safe ranges
   - Use batch operations

2. **Memory Issues**
   - Avoid extremely large numbers
   - Use safe addition for unknown inputs
   - Implement proper cleanup

3. **Logging Overhead**
   - Disable logging for high-frequency operations
   - Use appropriate log levels
   - Implement log rotation

4. **Precision Errors**
   - Adjust max_precision parameter
   - Use rounding functions
   - Validate input precision

## Conclusion

The enhanced add function provides enterprise-grade error handling with comprehensive logging, performance monitoring, and safety features. It's suitable for both development and production environments, offering flexibility through configuration options while maintaining robust error handling capabilities. 