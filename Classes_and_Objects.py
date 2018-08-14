# Create classes and objects.
# Programmed by Marufur Rahman.

class Students:  # Create a class.
    def introduce_self(self):
        print('My name is ' + self.name)

a1 = Students() # Create an object.
a1.name = 'Kayem'
a1.weight = 55

a2 = Students() # Create another object
a2.name = 'Towhid'
a2.weight = 60

a1.introduce_self()
a2.introduce_self()