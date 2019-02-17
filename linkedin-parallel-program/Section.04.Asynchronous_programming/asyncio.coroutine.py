import asyncio
import time

from random import randint

@asyncio.coroutine
def StartState():
    print("start state called")
    input_value = randint(0, 1)
    time.sleep(1)

    if (input_value == 0):
        result = yield from State2(input_value)
    else:
        result = yield from State1(input_value)
    
    print("Resume of the Transition : \nStart state calling " + result)

@asyncio.coroutine
def State1(transition_value):
    outputValue = "State 1 with transition value = {}\n".format(transition_value)

    input_value = randint(0, 1)
    time.sleep(1)
    print(" .... Evaluating...")
    if (input_value == 0):
        result = yield from State2(input_value)
    else:
        result = yield from EndState(input_value)
    result = "State 1 calling " + result
    return (outputValue + str(result))
    
@asyncio.coroutine
def State2(transition_value):
    outputValue = "State 2 with transition value = {}\n".format(transition_value)

    input_value = randint(0, 1)
    time.sleep(1)
    print(" .... Evaluating...")
    if (input_value == 0):
        result = yield from State2(input_value)
    else:
        result = yield from State1(input_value)
    result = "State 2 calling " + result
    return (outputValue + str(result))
    
@asyncio.coroutine
def EndState(transition_value):
    outputValue = "End State with transition value = {}\n".format(transition_value)

    print(" .... Stop computation...")
    return (outputValue)

if __name__ == "__main__":
    print("Finite state machine simulation with Asyncio Coroutine")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(StartState())