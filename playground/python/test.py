import sys
import logging


def add(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


logging.basicConfig(level=logging.INFO)

# print(add(2))
# print(add(3))


# def add(item, bucket=[]):
#     bucket.append(item)
#     print("Bucket ID:", id(bucket))
#     return bucket


# add(1)

# add(2)

# add(3)
print(add.__defaults__)
print(id(add.__defaults__))

# print(id(add.__defaults__[0]))
# add(1)
# print(id(add.__defaults__[0]))
