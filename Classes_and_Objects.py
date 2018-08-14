# Create classes and objects.
# Programmed by Marufur Rahman.

class Students:  # Create class.
	def __init__(self, name, skill, weight): 
		# Method of this class
		self.name = name
		self.skill = skill
		self.weight = weight
	def introduce_self(self):  
		# Another method of this class
		print("My name is " + self.name)

s1 = Students('Kayem', 'Python', 55) # Create an object
s2 = Students('Kamal', 'PHP', 67) # Create another object

s1.introduce_self()
s2.introduce_self()