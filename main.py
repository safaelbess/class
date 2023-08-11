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
