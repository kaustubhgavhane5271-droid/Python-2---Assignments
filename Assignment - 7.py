class Animal:
    def move(self):
        print("Animal moves")
        
class Dog:
    def move(self):
        print("Dog barks")
    
class bird:
    def move(self):
        print("Bird flies in the sky")
        
Animal = [Animal(), Dog(), bird()]

for a in Animal:
    a.move()                    