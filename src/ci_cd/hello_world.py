class HelloWorld:

    def __init__(self, name):
        self.name = name

    def say_hello(self) -> str:
        return f"Hello {self.name}!"
    
    def say_bye(self, from_who: str) -> str:
        return f"{from_who} said bye to {self.name}."

    def has_5_dogs(self, number_dogs: int) -> bool:
        if number_dogs == 4:
            return True
        else: False
