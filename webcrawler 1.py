import httpx
import asyncio
import time
from typing import Callable, Coroutine


async def crawl0(
    prefix: str, url: str = ''
):
    url = url or prefix
    print(f'Crawling {url}')
    client = httpx.AsyncClient()
    try:
        res = await client.get(url)
    finally:
        await client.aclose()
    for line in res.text.splitlines():
        if line.startswith(prefix):
            await crawl0(prefix, line)

addr = 'https://langa.pl/crawl/'

# browsing to addr returns another address
# https://langa.pl/crawl/0
# then this has two further addresses
# https://langa.pl/crawl/00
# https://langa.pl/crawl/01
# etc.

# Frameworks expecting callback functions of specific signatures might be type hinted using Callable[[Arg1Type, Arg2Type], ReturnType].
# https://docs.python.org/3/library/typing.html


async def progress(
    url: str,
    algo: Callable[..., Coroutine],
):
    asyncio.create_task(
        algo(url),
        name=url,
    )
    todo.add(url)
    start = time.time()
    while len(todo):
        print(
            f'{len(todo)}: '
            + ', '.join(
                sorted(todo)
            )[-38:]
        )
        await asyncio.sleep(0.5)
    end = time.time()
    print(f'Took {int(end - start)}'
          + ' seconds')

todo = set()


async def crawl1(
    prefix: str, url: str = ''
):
    url = url or prefix
    client = httpx.AsyncClient()
    try:
        res = await client.get(url)
    finally:
        await client.aclose()
    for line in res.text.splitlines():
        if line.startswith(prefix):
            todo.add(line)
            await crawl1(prefix, line)
        todo.discard(url)

asyncio.run(progress(addr, crawl1))

# This is still slow though : Took 59 seconds!
