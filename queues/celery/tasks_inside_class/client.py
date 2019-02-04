from time import sleep, time

# from celery_config import process_two
from package1.tasks import process, reverse

# process_two.delay(2, 3)
# process.delay("Hello")

# ready_asks = 0
# _reverse = reverse.delay("Hello")
# while not _reverse.ready():
#     sleep(0.2)
#     print('...')
#     ready_asks += 1
# print(_reverse.get())
# print(ready_asks)

# Class Task

from class_package.tasks import gen_tasks




gen_tasks.delay()

i = 100
while i > 0:
    time_begin = time()
    sleep(0.5)
    print(f"i={i}, time diff={time() - time_begin}")
    i -= 3
