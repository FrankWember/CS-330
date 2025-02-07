# Understanding Python Decorators

Python decorators are a powerful feature that me to modify the behavior of functions without changing their actual code. They provide an elegant way to apply reusable logic such as logging, authentication, and even performance measurement.

## Using a Decorator

A decorator is a function which takes another function as an argument, enhances or modifies its behavior, and returns a new function. Below is an example of a simple decorator that measures the execution time of a function.

<code> conda env create --file requirements.yaml </code>

### Example Code

Here is a Python decorator that will help to measure the time taken by a function:

```python
import time

def timer_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds.")
    return wrapper

@timer_decorator
def sample_task():
    time.sleep(2)  # Simulates a time-consuming task
    print("Task completed.")

sample_task()
```
### My Favorite Animal

![Baby Golden Retriever](./images/dog.jpg)

This is a picture of a **Golden Retriever**, a friendly and intelligent breed

