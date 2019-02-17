import asyncio


@asyncio.coroutine
def factorial(number):
    f = 1
    for i in range(2, number + 1):
        print("Asyncio.Task: compute factorial({})".format(i))
        yield from asyncio.sleep(1)
        f *= i

    print("Asyncio.Task - factorial({}) = {}".format(number, f))

if __name__ == "__main__":
    tasks = [
        asyncio.Task(factorial(5)),
        asyncio.Task(factorial(10))
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()