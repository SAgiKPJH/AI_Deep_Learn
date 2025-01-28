class Person:
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job
        
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
        
if __name__ == '__main__':
    man = Person("John", 31)
    man.hello()
    man.whoami()
    man.update_age(25)