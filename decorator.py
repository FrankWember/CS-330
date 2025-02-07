import time

def timer_decorator(func):
    """
    A decorator function that measures the execution time of 
    the decorated function and prints the elapsed time.
    """
    def wrapper():
        start_time = time.time()  # Start time recording
        result = func()  # Call the original function
        end_time = time.time()  # End time recording

        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds.")
        return result  # Return the function result

    return wrapper

@timer_decorator
def sample_function():
    """
    Computes the sum of the first 1,000,000 integers.
    """
    total = sum(range(1000000))
    return total

# Execute the function
sample_function()
     