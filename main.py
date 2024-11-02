
class Human:
    name: str
    age: int

    def __init__(self, v_name, v_age):
        self.name = v_name
        self.age = v_age
        print(f'{self.name} {self.age}')

    def see_func(self):
        ...


misha = Human('Misha', 23)
