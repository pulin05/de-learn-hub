import sys
import logging


def add(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


logging.basicConfig(level=logging.INFO)

print(add(1))
