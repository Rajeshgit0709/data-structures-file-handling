"""
Utility functions for data analysis
"""

def calculate_average(numbers):
    """Calculate the average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def format_currency(amount):
    """Format a number as currency"""
    return f"${amount:.2f}"

def validate_positive_number(value):
    """Check if a value is a positive number"""
    try:
        num = float(value)
        return num > 0
    except (ValueError, TypeError):
        return False

def get_grade_letter(score):
    """Convert numeric score to letter grade"""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'