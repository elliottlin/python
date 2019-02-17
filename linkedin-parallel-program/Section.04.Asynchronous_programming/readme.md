# Asynchronous Programming

### Using concurrent.futures

* ThreadPoolExecutor

```python
with concurrent.futures.ThreadPoolExecutor(max_worker=5) as executor:
    for item in number_list:
        executor.submit(evaluate_item, item)
```

* ProcessPoolExecutor

```python
with concurrent.futures.ProcessPoolExecutor(max_worker=5) as executor:
    for item in number_list:
        executor.submit(evaluate_item, item)
```

#### Uses of Pooling
* The pooling is used in almost all server applications, where there is a need to handle more simultaneous requests from any number of clients

* !! Many other applications, however, require that each task should be performed instantly or you have more control over the thread that executes it. In this case, pooling is not the best choice.



### Event loop management

* The python module Asyncio provides facilities to manage events, coroutings, tasks and threads, and synchronization primitives to write concurrent code

* Its main components and concepts are:
> An event loop - Single event loop per process

> Coroutines - Generalization of the subroutine concept
    
> Futures - Defines the Future object

> Tasks - Subclass of Asyncio




### Handling coroutings with Asyncio

* When a program becomes very long and complex, it is convenient to divide it into subroutines
* The subroutine cannot be executed independently, but only at the request of the main program
* Coroutines are a generalization of the subroutine

#### Important Aspects of Co-routine
* Co-routines allow mulitple entry points that can be yielded multiple times

* Co-routines can transfer the execution to any other co-routines

* The term "yield" is used to describe a co-routine that pauses and passes the control flow to another co-routine

#### Finite State Machine (FSA) or Automaton

* It is a mathematical model that is widely used not only in engineering displines, but also in sciences, such as mathematics and computer science


### Manuplating Task with Asyncio



### Dealing with Asyncio and Futures

* Another key component of the Asyncio module is the Future class. It is adapted in the main mechanism of Asyncio's event loop

* This is very similar to concurrent.futures

* The asyncio.Future class represents a result that is not yet available

* It represents an abstraction of something that yet to be accomplished
