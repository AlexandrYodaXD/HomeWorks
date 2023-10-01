#  Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

from classes import Dog, Cat, Fish


class Fabric:
    def __new__(cls, *args, **kwargs):
        instance = args[0](*args[1:])
        return instance


some_dog = Fabric(Dog, 'Бобик', 4, 'Бегает за хвостом (чужим)')
some_cat = Fabric(Cat, 'Мурзик', 20, 'Офигевает от происходящего по-кошачьи')
some_fish = Fabric(Fish, 'Риэлтор', 1, 'Бесполезно существует')

print(some_dog.get_spec())
print(some_cat.get_spec())
print(some_fish.get_spec())
