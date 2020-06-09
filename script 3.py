import asyncio
import datetime


def print_now():
    print(datetime.datetime.now())

# Define an async function


async def print3times():
    for _ in range(3):
        print_now()
        await asyncio.sleep(0.1)

print(type(print3times))    # Returns <class 'function'>
# Cannot directly run print3times as it is not
# an ordinary function!

# Calling print3times makes it a coroutine
coro1 = print3times()       # Returns <class 'coroutine'>, a coroutine is a awaitable
coro2 = print3times()       # Returns <class 'coroutine'>, a coroutine is a awaitable

print(type(coro1))
print(type(coro2))

asyncio.run(coro1)
asyncio.run(coro2)
