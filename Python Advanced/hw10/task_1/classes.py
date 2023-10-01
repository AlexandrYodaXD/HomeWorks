class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec


class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Fish(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec
