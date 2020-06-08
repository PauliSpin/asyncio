import datetime
import asyncio


def print_now():
    print(datetime.datetime.now())


async def keep_printing(name):
    while True:
        print(name, end=" ")
        print_now()
        await asyncio.sleep(0.50)


async def async_main():
    try:
        await asyncio.wait_for(keep_printing("Hey"), 10)    # Wait for 10 secs
    except asyncio.TimeoutError:
        print("Times up!")

print(datetime.datetime.now())
asyncio.run(async_main())
print(datetime.datetime.now())
