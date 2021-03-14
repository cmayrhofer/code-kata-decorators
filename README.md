# Code Kata Decorators

In this code kata we will discuss `python` decorators in some detail. Besides that we will
use a further way to collaborate on code projects and briefly touch exceptions.

## Useful Material on Decorators

### Websites and Blogs:
* [Python Decorators Introduction @pythonbasics.org](https://pythonbasics.org/decorators/)
* [Decorators in Python [Explained] by Sumeet Singh@askpython.com](https://www.askpython.com/python/examples/decorators-in-python)
* [Primer on Python Decorators by Geir Arne Hjelle@realpython.com](https://realpython.com/primer-on-python-decorators/)
* [PEP 318 -- Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)

### Talks
* [Python Decorators by Jonathan Fernandes@linkedIn Learning](https://www.linkedin.com/learning/python-decorators)
* [Decorators, unwrapped How do they work by Katie Silverio@PyCon 2017](https://youtu.be/UBSyD1RkOX0)
* [Practical decorators by Reuven M. Lerner@PyCon 2019](https://youtu.be/MjHpMCIvwsY)

## What Are Decorators

Decorators are a simple way to extend the behavior of functions or methods without modifying the functions or methods themselves, respectively. To understand how this is done, let us first recall that functions are first-class objects in Python. For instance, they can be used as arguments in functions
and also returned like any other object. Or serve as values in dictionaries, e.g.
```python
import pandas as pd

read_from = {
    "pickle": pd.read_pickle,
    "parquet": pd.read_parquet,
    "csv": pd.read_csv,
}

df = read_from["csv"]("path/to/some/csv/file.csv")
```


## Exercises

In the first exercise you should write a decorator which logs the execution time of a function. The decorator should be called `log_execution_time` and has to be defined within the `exercises/exercises.py` file.

The second decorator should catch the `Exception`, log it to `CRITICAL` and raise the `Exception` again. The name of the decorator has to be `catch_exceptions` and must also be defined in `exercises/exercises.py`

## Test Solutions

To test your implementations of the solutions, please run
```
docker-compose run --rm test
```

## How to "Submit" the Solution

Like the last time, you will have to create a pull requests to hand in your solution. Again you should use the associated review process to discuss each others solution.

However, this time you have to first fork the repository, i.e. make a copy of it under your name space. Then `git clone` from there and work on your solution. When you are done push to your repository and put out a pull request to the `main` branch of the original repo. Since you are working on a fork, `GitHub` will allow you to chose this option when you create the pull request.

