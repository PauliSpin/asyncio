import asyncio
import random
from colorama import Fore
from colorama import Style
from colorama import init, Fore, Style
from termcolor import colored

init()

c = (
    'cyan',
    'red',
    'magenta'
)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# RUN THIS IN A TERMINAL WINDOW NOT THE OUTPUT WINDOW #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

async def makerandom(idx: int, threshold: int = 6) -> int:
    print(colored(f"Initiated makerandom({idx}).", c[idx]))
    i = random.randint(0, 10)
    while i <= threshold:
        print(
            colored(f"makerandom({idx}) == {i} too low; retrying.", c[idx]))
        await asyncio.sleep(idx)
        i = random.randint(0, 10)
    print(colored(f"---> Finished: makerandom({idx}) == {i}", c[idx]))
    return i


async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
