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


# async def async_main():
#     await asyncio.gather(
#         keep_printing('First'),
#         keep_printing('Second'),
#         keep_printing('Third')
#     )

# # Single thread executes multiple coroutines at the same time
# asyncio.run(async_main())
# # Carries on indefinitely - interrupt via keyboard to stop

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Now use a timeout within a try/except construct

async def async_main():
    try:
        await asyncio.wait_for(
            asyncio.gather(
                keep_printing('First'),
                keep_printing('Second'),
                keep_printing('Third')
            ),
            5
        )
    except asyncio.TimeoutError:
        print('Timed Out!')

asyncio.run(async_main())

# When this runs, get :
# Timed Out!
# _GatheringFuture exception was never retrieved
# future: <_GatheringFuture finished exception=CancelledError()>
# asyncio.exceptions.CancelledError
# this is because the Timeout cancels the gather and this cancellation
# propagates to the keep_printing coroutines within it.
# We must handel these as well. Cancellations are errored.
