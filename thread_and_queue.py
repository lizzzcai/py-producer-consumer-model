from queue import Queue
from threading import Thread


# Object that signals shutdown
_sentinel = object()

# A thread that produces data
def producer(out_q, n):
    while n > 0:
        # Produce some data
        print("Producer: ", n)
        out_q.put(n)
        n -= 1

    # Put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)

# A thread that consumes data
def consumer(in_q):
    while True:
        data = in_q.get()
        if data is _sentinel:
            # put it back to other consumers threads
            in_q.put(_sentinel)
            print("Consumer: Stop")
            break
        print("Consumer: ", data)


q = Queue() # Queue instances already have all of the required locking
n = 10 # number of data to produce
t1 = Thread(target=producer, args=(q, n))
t2 = Thread(target=consumer, args=(q,))

t1.start()
t2.start()
