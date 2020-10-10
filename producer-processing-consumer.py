def producer():
    for item in range(10):
        print("produce ", item)
        yield item


def consumer(s):
    for item in s:
        print("consume ", item)

def processing(s):
    for item in s:
        print("process ", item)
        newitem = item ** 2
        yield newitem

a = producer()
b = processing(a)
c = consumer(b)