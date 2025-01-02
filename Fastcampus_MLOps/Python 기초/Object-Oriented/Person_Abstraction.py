from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job
    
    @abstractmethod
    def introduce(self):
        pass
        
    def hello(self):
        print("Hello")
        
    def whoami(self):
        print(f"Hello, I'm {self.name}, {self.age} years old.")
        
    def update_age(self, age):
        if age < 0:
            raise ValueError("Age must be positive.")
        else:
            self.age = age
            print(f"Now, I'm {self.name}, {self.age} years old.")
        
class Actor(Person):
    def __init__(self, name, age, film):
        super().__init__(name, age, job="Actor")
        self.film = film
    
    def introduce(self):
        super().hello()
        print(f"I'm an actor and I've been working on {self.film}.")
        
class Farmer(Person):
    def __init__(self, name, age, fruit):
        super().__init__(name, age, job="Actor")
        self.fruit = fruit
        
    def introduce(self):
        super().hello()
        print(f"I'm a farmer and I produce {self.fruit}.")

# 추상화 내용 구현 안할 시  
# Traceback (most recent call last):
#   File "d:\Sagi_JJU D\Git_Fork\AI_Deep_Learn\Fastcampus_MLOps\Object-Oriented\Person_Abstraction.py", line 42, in <module>
#     kim = Farmer("Kim", 40, "Apple")
# TypeError: Can't instantiate abstract class Farmer with abstract method introduce
    
if __name__ == "__main__":
    song = Actor("Song", 55, "Parasite")
    song.introduce()
    kim = Farmer("Kim", 40, "Apple")
    kim.introduce()