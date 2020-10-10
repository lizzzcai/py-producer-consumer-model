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

    n = 0
    while n < 10:
        n += 1
        print(f"[PRODUCER] producer is producing {n}")
        r = c.send(n)
        print(f"[PRODUCER] consumer return: {r}")
    
    print(f"[PRODUCER] stop the consumer")
    # close the generator
    c.close()



c = consumer()
producer(c)