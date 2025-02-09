from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, job=None):
        self.name = name
        self.__age = age
        self.job = job
    
    @abstractmethod
    def introduce(self):
        pass
        
    def _hello(self):
        print("Hello")
        
    def whoami(self):
        print(f"Hello, I'm {self.name}, {self.__age} years old.")
        
    def update_age(self, age):
        if age < 0:
            raise ValueError("Age must be positive.")
        else:
            self.age = age
            print(f"Now, I'm {self.name}, {self.__age} years old.")
        
class Actor(Person):
    def __init__(self, name, age, film):
        super().__init__(name, age, job="Actor")
        self.film = film
    
    def introduce(self):
        super().hello()
        print(f"I'm an actor and I've been working on {self.film}")

if __name__ == "__main__":
    song = Actor("Song", 55, "Parasite")
    song.whoami()
    song.__age = -1 # private이기 때문에 반영이 안됨
    song.whoami()
    song._hello()