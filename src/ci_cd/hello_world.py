class HelloWorld:

    def __init__(self, name):
        self.name = name

    def say_hello(self) -> str:
        return f"Hello {self.name}...?"
