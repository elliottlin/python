import threading


def func(i):
    print("function called by thread {}".format(i))
    return



threads = []

for i in range(5):
    t = threading.Thread(
        target=func,
        args=(i,)
    )
    threads.append(t)

    t.start()
    t.join()