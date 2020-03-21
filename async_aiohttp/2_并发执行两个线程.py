import asyncio
import time


async def call(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(call(1, 'hello'))
    task2 = asyncio.create_task(call(2, 'world'))
    print(f"Started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finised at {time.strftime('%X')}")


asyncio.run(main())

