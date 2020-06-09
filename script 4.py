import asyncio
import datetime
import asyncio

# Gather - run coroutines concurrently


def print_now():
    print(datetime.datetime.now())


async def keep_printing(name):
    while True:
        print(name, end=" ")
        print_now()
        await asyncio.sleep(0.50)


async def async_main():
    await asyncio.gather(
        keep_printing('First'),
        keep_printing('Second'),
        keep_printing('Third')
    )

# Single thread executes multiple coroutines at the same time
asyncio.run(async_main())
# Carries on indefinitely - interrupt via keyboard to stop
