


### 01 Major Componets of Threading Module

* thread
* Lock
* RLock
* semaphore
* condition
* event


`
class threading.Thread(
    group=None,
    target=None,
    name=None,
    args=(),
    kwargs={}
)
`

### 03 Implement a New Thread Using the Thread Module

* Define a new subclass of Thread class
* Override the __init__ method to add addtional args
* Override the run(self [, args]) method to implement what the thread should do when it started


### 04 Thread synchronization with lock

* acquire
* release

### 05 RLock
similar to lock

* acquire
* release

### 05 Semaphore
複數鎖🔒

* acquire when semaphore > 0

>> A particular use of semaphores is the mutex which is nothing but a semaphore with an internal variable initialized to the value 1
>> It allows the realization of mutual exclusion in access to data and resources
>> Semaphores are still commonly used in programming languages that are multithreaded


### 06 Condition

A condtion identifies a change of state in the application

* Consumer/Producer Problem

### 07 Event

* Events are objects that are used for communication between threads
* An event object manages an internal flag that can be set to true with the set() method and reset to false with the clear() method

### 08 Queue

Communication between thread

>> If optional args block is true and timeout is None - Block until a free slot is available
>> If the block is false - Put an item in the queue if a free slot is immediately available or raise the full exception


## Evaluatin the performance of multithread applications

GIL

* It prevents the programmer from improving the performance by executing threads in parallel
* If we remove the GIL from the CPythoninterpreter, the threads would be executed in parallel
* The GIL does not prevent a process from running on a different processor, it simply allows only one thread at a atime to turn inside the interpreter

### Result of the Preceding Code

- Multithreading execution becomes faster than the single-threaded execution
- GIL does not prevent a programmer from creating a multithreading work that concurrently increases the speed of execution
- while threads are a language construct, the CPython interpreter is the bridge between the threads and operating system 