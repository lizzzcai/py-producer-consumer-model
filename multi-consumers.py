from threading import Thread
from queue import Queue

q = Queue()
result = []

def producer():
    for i in range(100):
        q.put(i)

def consumer():
    while True:
        data = q.get()
        res = (data, data **2)
        result.append(res)
        q.task_done()

for i in range(5):
    t = Thread(target=consumer, args=())
    t.daemon = True
    t.start()

producer()
q.join()
print(result)