# 0x02. Python - Async Comprehension

## Overview

This project will immerse you into the intricacies of asynchronous programming in Python, specifically focusing on asynchronous generators, async comprehensions, and type-annotating generators.

## Project Details

- **Author:** Emmanuel Turlay, Staff Software Engineer at Cruise
- **Weight:** 1
- **Start Date:** Jan 16, 2024, 4:00 AM
- **End Date:** Jan 17, 2024, 4:00 AM
- **Checker Released:** Jan 16, 2024, 10:00 AM
- **Auto Review:** Will be launched at the deadline

## Resources

Read or watch:

- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#pep-530-asynchronous-comprehensions)
- [Type-hints for generators](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue)
  
## Learning Objectives

Upon completing this project, you should be able to explain to anyone, without the help of Google:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the `pycodestyle` style (version 2.5.x)
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word; it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Tasks

### Task 0: Async Generator

Write a coroutine named `async_generator` that takes no arguments. The coroutine will loop 10 times, each time asynchronously waiting for 1 second, then yield a random number between 0 and 10 using the `random` module.

### Example

```python
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
```

### Task 1: Async Comprehensions

Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments. The coroutine will collect 10 random numbers using an async comprehension over `async_generator` and then return the 10 random numbers.

### Example

```python
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())
```

### Task 2: Run time for four parallel comprehensions

Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`. The `measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds; explain it to yourself.

### Example

```python
#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
```

