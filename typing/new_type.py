from typing import NewType, List

UserId = NewType("UserId", int)
some_id = UserId(2423432)
print(some_id)
print(type(some_id))

print(some_id + 3423324423)