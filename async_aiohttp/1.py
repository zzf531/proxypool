import asyncio
import time


async def call(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"Started at {time.strftime('%X')}")
    await call(1, 'hello')
    await call(2, 'world')
    print(f"finised at {time.strftime('%X')}")


asyncio.run(main())

