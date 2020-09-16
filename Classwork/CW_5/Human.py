#Create a class Human, everyone has a name, create a method in the class
# that displays a welcome message to a each person.
# Create a class method in the class that returns information
# that it is a species of "Homosapiens".
# And also in the class create a static method that returns an arbitrary message.

class Human:

    def __init__(self,name):
        self.name = name

    def welcome_message(self):
        print(f"Hello {self.name}!")

    def what_species(self):
        return 'You are species of \"Homosapiens\"'

    @staticmethod
    def arbitrary_message():
        return 'You are the best Person!!!!'


Man = Human('Ivan')
Man.welcome_message()
print(Man.what_species())
print(Human.arbitrary_message())
