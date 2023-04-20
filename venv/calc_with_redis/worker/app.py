import redis
import time

r = redis.Redis(host='redis', port=6379, db=0)

while True:
    task = r.rpop("TEST")
    if task:
        print(eval(task))
    time.sleep(1)