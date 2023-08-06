import asyncio
import typing

def concurrent(n: int):
    def decorator(func: typing.Coroutine[typing.Any, typing.Any, typing.Any], 
                  ) -> typing.Coroutine[typing.Any, typing.Any, typing.Any]:
        sem = asyncio.Semaphore(n)
        async def wrapped_func(*args, **kwargs):
            async with sem:
                return await func(*args, **kwargs)
        return wrapped_func
    return decorator

def wrap_nth_input(nth: int=0):
    def decorator(func: typing.Coroutine[typing.Any, typing.Any, typing.Any], 
                  ) -> typing.Coroutine[typing.Any, typing.Any, typing.Any]:
        async def wrapped_func(*args, **kwargs):
            return args[nth], await func(*args, **kwargs)
        return wrapped_func
    return decorator

class NanoAsyncPool(object):
    def __init__(self, workers) -> None:
        self._workers = workers
    
    async def imap_unordered(self, 
                             func: typing.Coroutine[typing.Any, typing.Any, typing.Any], 
                             iterable: typing.Iterable, 
                             **kwargs,
                             ) -> typing.AsyncGenerator:
        wrapped_func = concurrent(self._workers)(func)
        async_works = [ wrapped_func(param, **kwargs) for param in iterable ]
        for coro in asyncio.as_completed(async_works):
            yield await coro
