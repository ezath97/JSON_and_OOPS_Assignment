# Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. 
# You must perform the following operations:
# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.

# Solution.
class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def description(self):
        print ('Dog Name: '+ self.name)
        return ('Age: '+ self.age)
    def get_info(self):
        return('Coat color: '+ self.coat_color)

class JackRussellTerrier(Dog):
    def __init__(self,name,age,coat_color,category,location):
        super().__init__(name,age,coat_color)
        self.category = category
        self.location = location
    def Category(self):
        return('category: '+ self.category)
    def Location(self):
        return('location: '+ self.location)

class Bulldog(Dog):
    def __init__(self,name,age,coat_color,vaccination,food):
        super().__init__(name,age,coat_color)
        self.vaccination = vaccination
        self.food = food
    def Vaccination(self):
        return('Vaccination status: '+ self.vaccination)
    def Food(self):
        return('Food Preference: '+ self.food)
        
print('Dog Class')
D=Dog("Lab","1","Pale Yellow")
print(D.description())
print(D.get_info())

print('***************************************************************')

print('JackRussellTerrier child Class')
D1=JackRussellTerrier("Jimmy","2","white","heavy","Chennai")
print(D1.description())
print(D1.get_info())
print(D1.Category())
print(D1.Location())

print('***************************************************************')

print('Bulldog child Class')
D2=Bulldog("Bruce","1.5","Black","Done","Non veg")
print(D2.description())
print(D2.get_info())
print(D2.Vaccination())
print(D2.Food())
