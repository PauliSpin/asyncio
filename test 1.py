import asyncio

# https://www.youtube.com/watch?v=Mj-Pyg4gsPs

# The following is not really a function
# This is a coroutine that is run by the event loop!
# async and await mark this out as a coroutine and not a normal function


async def mycoro(number):
    print('Starting %d' % number)   # Runs now
    # Wait some time simulating other code being run
    await asyncio.sleep(1)
    print('Finishing %d' % number)  # Runs later
    return str(number)

# coroutines , futures, tasks are things you can wait for
# event loop - runs the features and tasks

# mycoro(3)   # This DOES NOT run the coroutine but creates the object

# The way to run is it to pass it to the event loop

# c = mycoro()
# task = asyncio.create_task(c)

# If you end this script here, you'll get an error message saying:
#   RuntimeError: no running event loop
#   sys:1: RuntimeWarning: coroutine 'mycoro' was never awaited
# This is because you kicked off a task then exited and never waited for the
# task to complete and return

# Run the coroutine
asyncio.run(mycoro(1))
