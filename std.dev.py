# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 2/8/2022
#
# Write a class called Person that has two private data members - the person's name and age. It should
# have an init method that takes two values and uses them to initialize the data members. It should have a get_age
# method. Write a separate function (not part of the Person class) called std_dev that takes as a parameter a list of
# Person objects and returns the standard deviation of all their ages (the population standard deviation that uses a
# denominator of N, not the sample standard deviation, which uses a different denominator). Here's an example of
# calculating the population standard deviation. To calculate the standard deviation, you'll need to take a square
# root, which you can do by just using an exponent of 0.5. For example, the result of 9 ** 0.5 would be 3.0. Python
# does have a specific sqrt() function, but that involves importing a module, which we haven't covered yet. Here's a
# simple example of how your class and function could be used:
class Person:
    """Takes name and age entered to calculate the standard deviation among entered ages."""

    def __init__(self, name, age):
        """Initializes self and age constants. """
        self.name = name
        self.age = age

    def get_age(self):
        """Returns age."""
        return self.age


def std_dev(person_list):
    """Calculates standard deviation of entered ages."""
    total, mean, sd = 0.0, 0.0, 0.0  # Initializing variables total, mean and sd(standard deviation)
    length = len(person_list)  # Obtaining list length.
    for person in person_list:
        total += person.age  # Adding ages together.

    mean = total / length  # Calculating mean

    for person in person_list:
        """Calculating standard deviation."""
        sd += ((person.age - mean) * (person.age - mean))
    return (sd / length) ** 0.5


"""Testing
p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)
persons_list = [p1, p2, p3]
answer = std_dev(persons_list)
print(answer)
"""
