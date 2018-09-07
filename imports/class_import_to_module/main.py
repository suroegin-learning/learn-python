import time

from classfile import App

app = App()

search_engines = ["google", "yandex"]

for i, se in enumerate(search_engines):
    app.get(i)

print("cycle is end")

del app

time.sleep(10)