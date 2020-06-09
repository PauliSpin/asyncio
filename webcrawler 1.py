import httpx
import asyncio


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

asyncio.run(crawl0(
    'https://langa.pl/crawl/'
))
#
# Not so good doing it this way because:
# Takes a long while - downloads happening slowly.
#   1) Back-end activities also responsible for reporting their status; reporting progress from the same task - not good
#   await in crawl is within the crawl0 so this is recursive waits - not good
#   Also, not using concurrencies since we are aawiting crawl0
#   Should use context manager to call awaits rather than direct code.
