from Person_Inheritance import Programmer
from Person_Abstraction import Person, Actor, Farmer

people = [
    Programmer("Dave", 42, "Python"),
    Actor("Bruce", 35, "Parasutils"),
    Farmer("Jane", 50, "Corn")    
]

for person in people:
    person.introduce()
