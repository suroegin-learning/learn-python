class App:
    def __init__(self):
        self.var = "variable"

    def connect(self):
        print("Connection established")

    def get(self, v):
        print(v)

    def __enter__(self):
        print("__enter__: Hello!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__: Bye bye!")

    def __del__(self):
        print("class deleting...")