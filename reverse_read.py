#!/usr/bin/env python3

import redis
import time

SOURCE_HOST = "redis-19084.re-cluster1.ps-redislabs.org"
SOURCE_PORT = 19084

REPLICA_HOST = "redis-14000.re-cluster1.ps-redislabs.org"
REPLICA_PORT = 14000

LIST_NAME = "numbers"

source = redis.Redis(
    host=SOURCE_HOST,
    port=SOURCE_PORT,
    decode_responses=True
)

replica = redis.Redis(
    host=REPLICA_HOST,
    port=REPLICA_PORT,
    decode_responses=True
)

source.delete(LIST_NAME)

for i in range(1, 101):
    source.rpush(LIST_NAME, i)

print("Inserted values 1-100 into source-db")

time.sleep(2)

values = replica.lrange(LIST_NAME, 0, -1)

print("\nValues read from replica-db in reverse order:\n")

for value in reversed(values):
    print(value)