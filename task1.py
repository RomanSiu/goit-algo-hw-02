from queue import Queue
from random import randint
q = Queue()


def generate_request():
    request = {"id": randint(1, 100)}
    q.put(request)


def process_request():
    if not q.empty():
        req = q.get()
        print(f"Processing request {req['id']}")
    else:
        print(f"Queue is empty")


num = 0

while True:
    num += 1
    if num > 100:
        break
    generate_request()
    process_request()
