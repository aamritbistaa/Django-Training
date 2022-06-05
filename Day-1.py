
# name=input("Enter Name ")

# print("hello "+name)


#----------Comment techniques----------
# "Comment"
# 'Comment1'
# '''Comment2'''              //used to write multiple line

# text='''Ram 
# shyam
# hari'''

# print(text)


#-------variable writing techniques--------------
# #camel case
# myVarNew=10
# #pascal
# MyVarNew=10
# #snake
# my_var_name=10


# #camel case
# firstVar=10
# #pascal csae
# SecondVar=16
# #snakecase
# third_var=29

# if (firstVar<SecondVar) and (firstVar<third_var):
#     print(firstVar)
# elif (SecondVar<firstVar) and (SecondVar<third_var):
#     print(SecondVar)
# else:
#     print(third_var)

#----------------------
# x=y=z="Shyam",9,2.5

# print(x)
# print(y)
# print(z)

# a=2.9
# A="sally"

# print(a)
# print(A)

#-----------------List----------------
# Student=["x","y","z"]    #packing
# a,b,c=Student            #unpacking

# print(a)
# print(b)
# print(c)

# print(a,b,c)
# print(a+b+c)

#----------global & local variable----------
# a=10  #global
# def function():
#     print(a)
#     b=15    #local
#     print(b)

# function()

#--------Eval function------
# x=input('Enter a number: ')
# print(x)

#boolean
# x=True
# y=False

# print(x or y)
# print(not x or y)


#---------formating-------
# age = 20
# x='My name is monika, i m {} years old'
# print(x.format(age))


# a=25
# b=100
# c='12x78'
# d="Science"
# e='I need {} book at {} rate {} pie of code {}'

# print(e.format(a,b,c,d))


# a=25
# b=100
# c='12x78'
# d="Science"
# e='I need {} book at {} rate {} pie of code {}'

# print(e.format(a,b,c,d))



# a='12x78'
# b="Science"
# c=25
# d=100
# e='I need {1} book at {3} rate {2} pie of code {0}'

# print(e.format(a,b,c,d))