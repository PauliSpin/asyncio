import asyncio

# https://www.youtube.com/watch?v=Mj-Pyg4gsPs


async def mycoro(number):
    print('Starting %d' % number)
    await asyncio.sleep(1)
    print('Finishing %d' % number)
    return str(number)


async def main():
    await asyncio.gather(
        mycoro(1),
        mycoro(2),
        mycoro(3)
    )

result = main()
asyncio.run(result)
