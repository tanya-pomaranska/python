# The creation method must return an array of length 2 containing objects (representing Adam and Eve).
# The first object in the array should be an instance of the class Man.
# The second should be an instance of the class Woman. Both objects have to be subclasses of Human.
# Your job is to implement the Human, Man and Woman classes.
class Human():
    def __init__(self, sex):
        self.sex = sex

class Man(Human):
    def __init__(self, name):
        super().__init__('man')
        self.name = name

class Woman(Human):
    def __init__(self,name):
        super().__init__('woman')
        self.name = name

def God():
    return [Man('Adam'),Woman('Eva')]

#code

paradise = God()
print(isinstance(paradise[0], Man))   # True, "First object are a man")