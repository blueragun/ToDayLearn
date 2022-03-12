import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)  # await : 함수를 처리할때 사용하는 것
    # asyncio 앞에 await이 올수 있는 이유는 .sleep이 붙어 있으면 함수가 되기 때문에(time.sleep 역할)
    print(f"{name} 식사 완료, {mealtime}시간 소요...")
    print(f"{name} 그릇 수거 완료")
    return mealtime


async def main():

    result = await asyncio.gather(   # 동기적 실행시 문구 삭제
        delivery("A", 10),   # 동기적 진행시 await delivery("A", 10)
        delivery("B", 3),    # 동기적 진행시 await delivery("B", 3)
        delivery("C", 5),    # 동기적 진행시 await delivery("C", 5)
    )    # return 이 생략되어 있음

    print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
    
    
    # 서브루틴 : 하나의 진입점(def main())과 하나의 탈출점(return)이 있음
    # 코루틴 : 다양한 진입점과 다양한 탈출점이 있음  /  async, await로 만듦