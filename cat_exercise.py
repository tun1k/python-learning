# instantiate the Cat object with 3 cats.
# create a function that finds the oldest cat.
# print "the oldest cat is x years old".

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Tom', 5)
cat2 = Cat('Kitty', 3)
cat3 = Cat('Jim', 2)


def oldest_cat(*args):
    return max(args)


print(
    f"The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")
