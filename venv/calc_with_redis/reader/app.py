import redis

r = redis.Redis(host='redis', port=6379, db=0)

s = input("Input math expression: ")
while s.lower() != 'stop':
    r.lpush("TEST", s)
    s = input("Input math expression: ")
