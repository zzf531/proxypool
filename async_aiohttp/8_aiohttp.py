import asyncio
import aiohttp

# 定义异步函数 main()
async def main():
    # 获取 session 对象
    async with aiohttp.ClientSession() as session:
        # get 方式请求 httbin
        async with session.get('https://www.baidu.com/') as response:
            print(response.status)
            print(await response.text())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
