import httpx
import asyncio
import time
from typing import Callable, Coroutine


async def progress(
    url: str,
    algo: Callable[..., Coroutine],
):
    task = asyncio.create_task(
        algo(url),
        name=url,
    )
    todo.add(task)
    start = time.time()
    while len(todo):
        done, _pending = await asyncio.wait(todo, timeout=0.5)
        todo.difference_update(done)
        urls = (t.get_name() for t in todo)
        print(f'{len(todo)}: ' + ', '.join(sorted(urls))[-75:])
    end = time.time()
    print(f'Took {int(end - start)} seconds')


async def crawl2(
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
            asyncio.create_task(
                crawl2(prefix, line),
                name=line,
            )
    todo.discard(url)

addr = 'https://langa.pl/crawl/'
todo = set()

asyncio.run(progress(addr, crawl2))  # Only took 24 secs instead of 59 secs
