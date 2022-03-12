# 코루틴 hello world!
# 코루틴 : 다양한 진입점과 다양한 탈출점이 있음  /  async, await로 만듦

# https://docs.python.org/ko/3/library/asyncio-task.html

import asyncio


async def hello_world():
    print("hello world")
    return 123


if __name__ == "__main__":
    asyncio.run(hello_world()) # asyncio.run : 코루틴을 실행하는 것
    
    
# await는 async안에서 실행되어야 한다.
# 다만 asyncio가 있으면 await을 대신할 수 있다.

# asyncio.create_task -> 태스크 예약 // await ~ 똑같음
# asyncio.sleep -> 현재 태스크 일시 중단해서 다른 태스크 실행