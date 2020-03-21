import asyncio


async def hello(proxy):
    print("Hello world!", proxy)
    r = await asyncio.sleep(0.000000001)
    print("Hello again!")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [hello(i) for i in range(1, 5)]
    print(tasks)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
