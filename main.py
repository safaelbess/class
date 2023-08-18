# # class Car:

# #   def __init__(self, make, model, year, mileage, enginetype):
# #     self.make = make
# #     self.model = model
# #     self.year = year
# #     self.mileage = mileage
# #     self.enginetype = enginetype

# #   def __str__(self):
# #     return f'the cars make is {self.make}, the cars model is {self.model} , the cars year is {self.year} the cars mileage is {self.mileage}'
 
# #   def getmile_age(mileage):
# #     return f'the cars mileage is {mileage}'

# #   def set_mileage(newmileage):
# #     if newmileage> mileage:
# #       print('the current mileage is', newmileage)
# #     else:
# #       print('add an other mileage')
                            
      
# # make = input('enter make')
# # model = int(input('enter model'))
# # year = int(input('enter the year'))
# # mileage = int(input('enter the mileage'))
# # enginetype = input('enter the type')

# # print('information added successfully')

# # Car1 = Car
# # mile_age = int(input('enter the new mile_age'))
# # print(Car.getmile_age(mile_age))
# # newmileage =int(input ('enter the new mileage'))

# # Car.set_mileage(newmileage)



# # class Rectangle:
# #   def __init__(self,width, height):
# #     self.width=width
# #     self.hieght=height

# #   def __str__(self):
# #     return f'the rectangle width is {self.width} and the hieght is {self.hieght}'

# #   def area(width, hieght):
# #     area = width*hieght
# #     return f'the rectanle area is {area}'


# #   def perimeter (width,hieght):
# #     if width>0 and hieght>0:
# #       perimeter = 2*width +2*hieght
# #       return f'the perimeter of the rectngle is , {perimeter}'
      
# #     else : 
# #         return f'wrong entries , the width and the hieght must be grater than 0  ,please , enter other values '   
# # width1=int(input('enter the width'))
# # hieght1=int(input('enter the hiegt'))

# # Rectangle1=Rectangle(width1,hieght1)
# # print(Rectangle1)

# # print(Rectangle.area(width1,hieght1))
# # print(Rectangle.perimeter(width1,hieght1))




# # class Animal:
# #   def __init__(self , name , species ,age,weight):
# #     self.name =name
# #     self.species =species
# #     self.age = age
# #     self.wieght=wieght

# #   def __str__(self):
# #     return f'the animal name is {self.name} , the animal species is  {self.species}  the animal age is {self.age} and the anilmal weight is {self.wieght}'

# #   def make_sound (sound,mammal):
# #     if is_mammal=='yes'
# #       return f' the sound is different'
# # else: 
# #     return f'the sound is{sound}'

      

# # name=input('enter the animal name:')
# # species=input(' enter the animal species') 
# # age=int(input('enter the animal age'))
# # wieght= int(input('enter the animal wieght'))
# # print('the animal information added successfully')
# # Animal1=Animal(name, species,age,wieght)

# # print(Animal1)
# # sound = input ('enter the sound of the animal')
# # is_mammal=input ('is the animal mammal?')

# # print(Animal1.make_sound(sound,is_mammal))






# class Student:

#   def __init__(self,
#                name='default',
#                age=18,
#                grade=30,
#                city='amman',
#                specialise='dev',
#                password='123456'):
#     self.name = name
#     self.age = age
#     self.grade = grade
#     self.city = city
#     self.specialise = specialise
#     self.password = password

#   def __str__(self):
#     return f'hello my name is {self.name}, my age is {self.age} ,my grade is {self.grade}, my city is {self.city} and my specialise is {self.specialise}'
#     return f'hi my name is {self.name}'

#   def add_course(self, newcourse, password, username):

#     password = input('enter your password')
#     username = input('enter the username')

#     if self.name == username and self.password == password:
#       print('you can add course ')
#       return f'hi {self.name} you have added {newcourse} to your courses'

#   def take_quiz(self,
#                 question1='q1',
#                 question2='q2',
#                 question3='q3',
#                 answer1='f',
#                 answer2='t',
#                 answer3='t',
#                 student_answer='false',
#                 password='3333',
#                 username='ali',
#                 mark=0,
#                 numberofquestions=3):
#     password = input('enter your password')
#     username = input('enter the username')

#     if self.name == username and self.password == password:
#       print('you can begin your quiz')
#       numberofquestions = 3

#       question1 = 'python is a compiling language'
#       answer1 = 'false'
#       question2 = 'anyone can access the public rpository '
#       answer2 = 'true'
#       question3 = 'you cant convert the variable type from integer to string'
#       answer3 = 'false'
#       while True:
#         print(question1)

#         student_answer = (input('enter your answer'))
#         if student_answer == answer1:
#           # print ('right answer')
#           mark += 1
#         print(question2)

#         student_answer = (input('enter your answer'))
#         if student_answer == answer2:
#           # print ('right answer')
#           mark += 1
#         print(question3)

#         student_answer = (input('enter your answer'))
#         if student_answer == answer3:
#           # print ('right answer')
#           mark += 1
#           return f'your mark is {mark}'

#   def showgrade(self, password, username):
#     password = input('enter your password')
#     username = input('enter the username')

#     if self.name == username and self.password == password:

#       return f' hello {self.name} your grade is {self.grade}'


# students = []
# while True:
#   print('welcome to our program ')
#   print('1-login')
#   print('2-register')
#   print('3-exit')
#   userchoice = int(input('enter your choice'))
#   if userchoice == 1:
#     print('welcome to login')
#     while True:
#       password = input('enter your password')
#       username = input('enter the username')
#       for student in students:
#         if student.name == username and student.password == password:
#           print('you have logged in successfully')

#           print('1-add course')
#           print('2-take quiz')
#           print('3-view my grades')
#           print('4-exit')
#           studentchoice = int(input('enter your choice in login page'))
#           while True:
#             if studentchoice == 1:
#               student.addcourse(input('enter the course name'))
#             elif studentchoice == 2:
#               print(
#                   student.take_quiz('q1',
#                                     'q2',
#                                     'q3',
#                                     'a1',
#                                     'a2',
#                                     'a3',
#                                     'sa',
#                                     mark=0))

#             elif studentchoice == 3:

#               print(student.showgrade(password, username))

#             elif studentchoice == 4:
#               break

#           print(student)
#           break

#         else:
#           print('wrong name or password')

#   elif userchoice == 2:
#     name = input('enter your name')
#     age = int(input('enter your age'))
#     grade = int(input('enter your grade'))
#     city = input('enter your city')
#     specialise = input('enter your specialise')
#     password = input('enter your password')
#     student1 = Student(name, age, grade, city, specialise, password)
#     print('you have added information successfully')
#     print(student1)
#     students.append(student1)

#   elif userchoice == 3:
#     break





class Father:

  def __init__(self, name, age):
    self.fathername = name
    self.fatherage = age

  # def __str__(self):
  #   return f'fathers name is {self.fathername} and fathers age is {self.fatherage} '


father1 = Father('ali', 50)
#print(father1)


class Son(Father):

  def __init__(self, name, age, fathername, fatherage):
    super().__init__(fathername, fatherage)
    self.name = name
    self.age = age

  def __str_(self):
    return f'father name is {self.fathername} and  father age is {self.fatherage}'


father1 = Father('ahmed', 50)
son1 = Son('ali', 30, 'ahmed', 50)
print(son1)
#print(father1)


class Mum:

  def __init__(self, name, age, eyecolor):
    self.mumname = name
    self.mumage = age
    self.eyecolor = eyecolor

  def __str_(self):
    return f' mum age is {self.mumage} and mum eyecolor is {self.eyecolor}'


class Dauter(Mum):

  def __init__(self, name, age, mumname, eyecolor):
    super().__init__(mumname, eyecolor)
    self.name = name
    self.age = age

  def __str__(self):
    return f'dauter name is {self.name} dauter age is {self.age} mother name is {self.mumname} and eyecolor is {self.eyecolor} '


Dauter1 = Dauter('sara', 30, 'maha', 'blue')
print(Dauter1)


class Teacher:

  def init__(self, name, age, coursename):
    self.teachername = name
    self.age = age
    self.corsename = coursename

  def __str__(self):
    return f'teacher name is {self.teachername} teacher age is {self.age} corse name is {self.corsename}'


class Student(Teacher):

  def __init__(self, name, age, teachername, corsename):
    super().__init__(teachername, corsename)
    self.name = name
    self.age = age

  def __str__(self):
    return f'student name is {self.name} age is {self.age} teacher name is {self.teachername} and corse name is {self.corsename}'


student1 = Student('ali', 20, 'Dr.ahmed', 'python')

print(student1)
