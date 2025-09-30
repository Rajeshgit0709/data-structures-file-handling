# Execution Decorator Examples and Identification Methods

import time
import functools
import inspect
from typing import Callable, Any

# -------------------------------
# 1. BASIC EXECUTION TIME DECORATOR
# -------------------------------
def timer(func):
    """Basic execution time decorator"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️  {func.__name__} executed in {end - start:.6f} seconds")
        return result
    return wrapper

# -------------------------------
# 2. ADVANCED EXECUTION DECORATOR WITH LOGGING
# -------------------------------
def execution_tracker(log_args=False, log_result=False):
    """Advanced decorator with configurable logging"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            
            # Log function call
            print(f"🚀 Starting {func.__name__}")
            
            if log_args:
                print(f"   📥 Args: {args}, Kwargs: {kwargs}")
            
            try:
                result = func(*args, **kwargs)
                end = time.perf_counter()
                
                print(f"✅ {func.__name__} completed in {end - start:.6f}s")
                
                if log_result:
                    print(f"   📤 Result: {result}")
                
                return result
            
            except Exception as e:
                end = time.perf_counter()
                print(f"❌ {func.__name__} failed after {end - start:.6f}s: {e}")
                raise
        
        return wrapper
    return decorator

# -------------------------------
# 3. HOW TO IDENTIFY DECORATORS IN YOUR CODE
# -------------------------------

def identify_decorators():
    """Function to identify decorators applied to functions"""
    
    # Method 1: Check if function has __wrapped__ attribute
    def check_wrapped_attribute(func):
        return hasattr(func, '__wrapped__')
    
    # Method 2: Check function name vs __name__
    def check_function_names(func):
        return func.__name__ != getattr(func, '__name__', func.__name__)
    
    # Method 3: Inspect the function
    def get_decorator_info(func):
        info = {
            'name': func.__name__,
            'qualname': getattr(func, '__qualname__', 'Unknown'),
            'module': getattr(func, '__module__', 'Unknown'),
            'is_decorated': hasattr(func, '__wrapped__'),
            'original_function': getattr(func, '__wrapped__', None)
        }
        return info
    
    return check_wrapped_attribute, check_function_names, get_decorator_info

# -------------------------------
# 4. EXAMPLE FUNCTIONS WITH DIFFERENT DECORATORS
# -------------------------------

@timer
def simple_function(n):
    """Simple function with timer decorator"""
    return sum(range(n))

@execution_tracker(log_args=True, log_result=True)
def complex_function(x, y, operation="add"):
    """Complex function with advanced tracker"""
    if operation == "add":
        return x + y
    elif operation == "multiply":
        return x * y
    else:
        return x - y

def undecorated_function(text):
    """Function without any decorators"""
    return text.upper()

# -------------------------------
# 5. DECORATOR DETECTION UTILITY
# -------------------------------

def analyze_function_decorators(*functions):
    """Analyze multiple functions to detect decorators"""
    print("🔍 DECORATOR ANALYSIS REPORT")
    print("=" * 50)
    
    check_wrapped, check_names, get_info = identify_decorators()
    
    for func in functions:
        info = get_info(func)
        is_decorated = check_wrapped(func)
        
        print(f"\n📋 Function: {info['name']}")
        print(f"   🏷️  Qualified Name: {info['qualname']}")
        print(f"   📦 Module: {info['module']}")
        print(f"   🎭 Is Decorated: {is_decorated}")
        
        if is_decorated:
            print(f"   🔗 Original Function: {info['original_function']}")
            print(f"   📜 Decorator Chain: Yes")
        else:
            print(f"   📜 Decorator Chain: None")
        
        # Try to get source code info
        try:
            source_lines = inspect.getsourcelines(func)
            source_file = inspect.getfile(func)
            print(f"   📁 Source File: {source_file}")
            print(f"   📍 Line Number: {source_lines[1]}")
        except:
            print(f"   📁 Source: Unable to retrieve")

# -------------------------------
# 6. RUNTIME DECORATOR INFORMATION
# -------------------------------

def get_execution_info(func):
    """Get detailed execution information about a function"""
    print(f"\n🔬 EXECUTION INFO for {func.__name__}")
    print("-" * 40)
    
    # Check various attributes that decorators might add
    attributes_to_check = [
        '__name__', '__qualname__', '__doc__', '__module__',
        '__wrapped__', '__annotations__', '__dict__'
    ]
    
    for attr in attributes_to_check:
        value = getattr(func, attr, 'Not Found')
        print(f"{attr:15}: {value}")
    
    # Check if it's a closure (decorated function)
    if hasattr(func, '__closure__') and func.__closure__:
        print(f"{'__closure__':15}: {len(func.__closure__)} cell(s)")
        print("                This function is likely decorated!")
    else:
        print(f"{'__closure__':15}: None (not decorated)")

# -------------------------------
# 7. TEST THE DECORATOR DETECTION
# -------------------------------

if __name__ == "__main__":
    print("🎯 TESTING DECORATOR DETECTION")
    print("=" * 60)
    
    # Test functions
    print("\n1️⃣ Testing functions...")
    simple_function(1000)
    complex_function(5, 3, "multiply")
    result = undecorated_function("hello world")
    print(f"Undecorated result: {result}")
    
    # Analyze decorators
    print("\n2️⃣ Analyzing decorators...")
    analyze_function_decorators(
        simple_function, 
        complex_function, 
        undecorated_function
    )
    
    # Get detailed execution info
    print("\n3️⃣ Detailed execution info...")
    get_execution_info(simple_function)
    get_execution_info(complex_function)
    get_execution_info(undecorated_function)
    
    print("\n✨ Analysis Complete!")