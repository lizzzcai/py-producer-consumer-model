import random

def consumer():
    print("[CONSUMER] start")
    r = "start from consumer"
    while True:
        n = yield r
        if not n:
            print("[CONSUMER] n is empty")
            continue
        print(f"[CONSUMER] consumer is consuming {n}")
        r = "200 ok"

def producer(c):
    # start the generator
    start_value = c.send(None)
    print(f"[PRODUCER] start the consumer: {start_value}")

    while True:
        n = random.randint(0, 100)
        print(f"[PRODUCER] producer is producing {n}")
        r = c.send(n)
        print(f"[PRODUCER] consumer return: {r}")

        yield
    
    print(f"[PRODUCER] stop the consumer")
    # close the generator
    c.close()



c = consumer()
p = producer(c)

for _ in range(10):
    next(p)
