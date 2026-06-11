class User:
    # this constructor will automatically be called when an instance is created
    def __init__(self, fname, lname, age): 
        self.fname = fname
        self.lname = lname
        self.age = age
        
user1 = User("Munna", "Mohammad", 20)
user2 = User("John", "Doe", 21)

print( user1.fname, user1.lname, user1.age )

# what is encapsulation in oop?
# ans: Encapsulation is a process of designing a programatic class,
# using public and private methods and attributes to implement abstraction.
# ans: Encapsulation is a process of designing a programatic class,
# using public and private methods and attributes to implement abstraction.

# what is abstraction?
# ans: The idea of exposing only "relevant" data in a class interface, hiding
# private attributes and methods (aka the "inner workings") from users.
