import asyncio
import sys

@asyncio.coroutine
def first_coroutine(future, N):
    count = 0
    for i in range(1, N+1):
        count += i
    yield from asyncio.sleep(4)
    future.set_result("first coroutine (sum of N integers) result = " + str(count))

@asyncio.coroutine
def second_coroutine(future, N):
    count = 0
    for i in range(1, N+1):
        count += i
    yield from asyncio.sleep(6)
    future.set_result("second coroutine (sum of N integers) result = " + str(count))


def got_result(future):
    print(future.result())

if __name__ == "__main__":
    N1 = 20
    N2 = 10

    loop = asyncio.get_event_loop()
    f1 = asyncio.Future()
    f2 = asyncio.Future()

    tasks = [
        first_coroutine(f1, N1),
        second_coroutine(f2, N2)
    ]

    f1.add_done_callback(got_result)
    f2.add_done_callback(got_result)
    
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()