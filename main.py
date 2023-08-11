class Car:

  def __init__(self, make, model, year, mileage, enginetype):
    self.make = make
    self.model = model
    self.year = year
    self.mileage = mileage
    self.enginetype = enginetype

  def __str__(self):
    return f'the cars make is {self.make}, the cars model is {self.model} , the cars year is {self.year} the cars mileage is {self.mileage}'
 
  def getmile_age(mileage):
    return f'the cars mileage is {mileage}'

  def set_mileage(newmileage):
    if newmileage> mileage:
      print('the current mileage is', newmileage)
    else:
      print('add an other mileage')
                            
      
make = input('enter make')
model = int(input('enter model'))
year = int(input('enter the year'))
mileage = int(input('enter the mileage'))
enginetype = input('enter the type')

print('information added successfully')

Car1 = Car
mile_age = int(input('enter the new mile_age'))
print(Car.getmile_age(mile_age))
newmileage =int(input ('enter the new mileage'))

Car.set_mileage(newmileage)



class Rectangle:
  def __init__(self,width, height):
    self.width=width
    self.hieght=height

  def __str__(self):
    return f'the rectangle width is {self.width} and the hieght is {self.hieght}'

  def area(width, hieght):
    area = width*hieght
    return f'the rectanle area is {area}'


  def perimeter (width,hieght):
    if width>0 and hieght>0:
      perimeter = 2*width +2*hieght
      return f'the perimeter of the rectngle is , {perimeter}'
      
    else : 
        return f'wrong entries , the width and the hieght must be grater than 0  ,please , enter other values '   
width1=int(input('enter the width'))
hieght1=int(input('enter the hiegt'))

Rectangle1=Rectangle(width1,hieght1)
print(Rectangle1)

print(Rectangle.area(width1,hieght1))
print(Rectangle.perimeter(width1,hieght1))




class Animal:
  def __init__(self , name , species ,age,weight):
    self.name =name
    self.species =species
    self.age = age
    self.wieght=wieght

  def __str__(self):
    return f'the animal name is {self.name} , the animal species is  {self.species}  the animal age is {self.age} and the anilmal weight is {self.wieght}'

  def make_sound (sound,mammal):
    if is_mammal=='yes'
      return f' the sound is different'
else: 
    return f'the sound is{sound}'

      

name=input('enter the animal name:')
species=input(' enter the animal species') 
age=int(input('enter the animal age'))
wieght= int(input('enter the animal wieght'))
print('the animal information added successfully')
Animal1=Animal(name, species,age,wieght)

print(Animal1)
sound = input ('enter the sound of the animal')
is_mammal=input ('is the animal mammal?')

print(Animal1.make_sound(sound,is_mammal))
