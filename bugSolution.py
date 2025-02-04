def function_with_uncommon_error(x):
    try:
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return 1 / x
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example of usage
print(function_with_uncommon_error(5))
print(function_with_uncommon_error(0))