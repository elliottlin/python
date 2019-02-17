
import asyncio
import datetime
import time

def func_1(end_time, loop):
    print('func_1 called')
    print(end_time)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, func_2, end_time, loop)
    else:
        loop.stop()
    print("func 1 end")

def func_2(end_time, loop):
    print('func_2 called')
    print(end_time)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, func_3, end_time, loop)
    else:
        loop.stop()
    print("func 2 end")

def func_3(end_time, loop):
    print('func_3 called')
    print(end_time)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, func_1, end_time, loop)
    else:
        loop.stop()
    print("func 3 end")

def func_4(end_time, loop):
    print('func_4 called')
    print(end_time)
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, func_4, end_time, loop)
    else:
        loop.stop()

loop = asyncio.get_event_loop()

# schedule the first call to display_date()

end_loop_1 =  loop.time() + 9.0
loop.call_soon(func_1, end_loop_1, loop)
# loop.call_soon(func_4, end_loop_1, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()
