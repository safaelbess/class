# # # # # #
# # # # # person = {'name': 'ali', 'age': 33, 'country': 'jordan'}
# # # # # print(person['name'])
# # # # # person['gender'] = 'male'
# # # # # print(person)
# # # # # person['parent'] = {'father': 'ahmad', 'mother': 'sara'}
# # # # # print(person)
# # # # # person['skills'] = {'python', 'java', 'c'}
# # # # # print(person)
# # # # # print('_' * 50)
# # # # # print('name: ' + person['name'])
# # # # # print('age: ' + str(person['age']))
# # # # # print('country: ' + person['country'])
# # # # # print('parent: ', person['parent'])
# # # # # print('skills:', person['skills'])
# # # # # print('gender:' + person['gender'])
# # # # # print('_'*50)

# # # # # #del person['parent']['father']
# # # # # #print(person['parent'])
# # # # # person['parent']['father']='salem'
# # # # # print(person['parent'])
# # # # # for i in person:
# # # # #   print(i ,':', person[i])
# # # # #   for key,value in person.items():
# # # # #     print('key\n : ' ,key)
# # # # #     print('value: ', value)
# # # # # print('_'*50)
# # # # # person2=person.copy()
# # # # # print(person2)
# # # # # person2.clear()
# # # # # print(person2)

# # # # # print('_'*50)
# # # # # print(person.get('name'))
# # # # # print(person.items())
# # # # # print(person.keys())
# # # # # print(person.values())

# # # # # print(person.setdefault('name','sami'))

# # # n = int(input('enter the number of elements:'))

# # # student = {}
# # # for i in range(n):
# # #   key = input('enter the key:')
# # #   value = input('enter the value :')
# # #   student[key] = value

# # # print(student)

# # # for i in (student):
# # #   print(i, ':', student[i])

# # # an_other_student = bool(input('do you want to add an other student?'))
# # # if an_other_student==True:
# # #   n = int(input('enter the number of elements:'))

# # #   student={}
# # #   for i in range(n):
# # #     key =input('enter the key:')
# # #     value = input ('enter the value :')
# # #     student[key] = value
# # # else:
# # #   an_other_student= False

# # # print(student)

# # # student['subjects'] = {'Math': '', 'English': '', 'science': '', 'Arabic': ''}

# # # for j in (student['subjects']):
# # #   student['subjects'][j] = int(input('enter the subjects grade :'))

# # # student['teachers'] = {'Math': '', 'Arabic': '', 'science': '', 'Arabic': ''}

# # # for c in (student['teachers']):
# # #   student['teachers'][c] = input('enter the teachers name :')

# # # print(student)

# # entervalue=True
# # students=[]

# # while entervalue:
# #   student={}
# #   students.append(student)
# #   inserttimes = int(input ('how many elements do you want to have?'))
# #   deckey= input ('enter the key of the student')
# #   valueType =int(input ('enter the type of the value 1 for str 2 for int 3 for list 4 for dict'))
# #   if valueType ==1:
# #     student[deckey]=input ('enter the value')

# #   elif valueType==2:

# #     student[deckey]= int(input('enter the value'))

# #   elif valueType==3:
# #     times = int (input('how many skills do you want to add'))
# #     for j in range(times):
# #       decValue=[]
# #       listValue =input('enter the value ')
# #       decValue.append(listValue)

# #   elif valueType==4:
# #     stdictionary={}
# #     times= int(input('how many dictionary keys do you want to add?'))
# #     for i in (times):
# #       deckey=input('enter the dictinary key :')
# #       decValue =input ("enter the dictionary value")
# #       stdictionary[deckey]=decValue
# #     print(students)

# #   addother=input('do you want to add an other student?')
# #   if addother=='no':
# #     entervalue=False

# #   print(students) :

# class Student:
#   def __init__(self,name,age,grade,spec):
#     self.name=name
#     self.age=age
#     self.grade=grade
#     self.spec=spec

#   def __str__(self):
#     return f'hello my name is {self.name} ,my age is {self.age} , my grade is {self.grade} and my spec is {self.spec} '

# Obj1=Student('ali',22,44,'dev')

# print(Obj1)
# name=input('enter the name')
# age=int(input('enter the  age'))
# grade=int(input('enter the grade'))
# spec=input('enter the spec')

# Obj2=Student(name , age, grade,spec)

# print(Obj2)


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
