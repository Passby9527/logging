# logger
This is a basic logging module which will record program's execution status and error messages.

it will build a folder that named "log" initally, and you can find all the log message there.

how to use 
```python=
from logger import logFunc

@logFunc
def foo():    
    # do something
    return
```
