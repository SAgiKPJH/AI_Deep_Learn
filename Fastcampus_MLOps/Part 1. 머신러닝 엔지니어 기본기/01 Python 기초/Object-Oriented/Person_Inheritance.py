from Person import Person

class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age, job="Programmer")
        self.language = language
        
    def introduce(self):
        print(f"I'm {self.name}, a {self.job} who knows {self.language}.")
        
if __name__ == "__main__":
    dave = Programmer("Dave", 42, "Python")
    dave.introduce()