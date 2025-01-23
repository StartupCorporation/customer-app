import asyncio
from typing import Any, Callable, Coroutine
from functools import wraps

def async_command(func: Callable[..., Coroutine]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        return asyncio.run(func(*args, **kwargs))

    return wrapper
