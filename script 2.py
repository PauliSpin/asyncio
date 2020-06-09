import datetime
import asyncio


def print_now():
    print(datetime.datetime.now())


async def keep_printing(name):
    while True:
        print(name, end=" ")
        print_now()
        await asyncio.sleep(0.50)

# Re-dfine main in terms of a clearly define
# instance. The object will not be running at that time;
# the object here is "keep_printing"


async def async_main():
    kp = keep_printing("Hey")
    waiter = asyncio.wait_for(kp, 3)
    try:
        await waiter    # This is where we are actually awaiting the object 'kp'
    except asyncio.TimeoutError:
        print("Timed Out!")

# print(datetime.datetime.now())
asyncio.run(async_main())
# print(datetime.datetime.now())
