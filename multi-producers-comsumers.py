import queue
import threading

q = queue.Queue()
has_data = threading.Semaphore(value=0)


def consumer(id):
    # acquire a semaphore, or sleep until the counter of semaphore is larger than zero
    while has_data.acquire():
        data = q.get()
        print(f"consumer {id}: consume {data}")
        q.task_done()

def producer(id):
    for data in range(10):
        q.put(data)
        print(f"producer {id}: produce {data}")
        # release the semaphore, increment the iternal counter by 1
        has_data.release()

producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]
consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(5)]

[p.start() for p in producers]
[c.start() for c in consumers]

q.join()

[p.join() for p in producers]
[c.join() for c in consumers]
