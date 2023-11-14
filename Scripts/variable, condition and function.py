# XingJieXingjie
# the try/except structure
# you surround a dangerous section of code with try and except
# if the code in the try works, the except is skipped
# if the code in the try fails, it jumps to the except section
##astr = 'hello'
##try:
  ##  istr = int(astr)  #这里出现问题后代码就不会继续往下运行了，加入一个try except机制
##except:
   ## istr = -1
##print('first', istr)
##astr = '123'
##try:
  ##  istr = int(astr)
##except:
   ## istr = -1
##print('second', istr)##
##print(type(astr))
##print(type(istr))

# 如果有几行代码，我将不断重复使用，我可以直接定义function，这样出现错误时不用不断去寻找错误
def thing(): # mean nothing 但是记住了thing这个函数 reusable code
    print('hi')
    print('sb')
thing()
print('kiki')

big = max('hello world')  # 可以视为python内部的函数，事先定义好了
print(big)
tiny = min('hello world')
print(tiny)
print(float(99)/100)
## we create a new function using the  def  keyword followed by optional parameters in parentheses
## define the function but does not execute the body of the funcion
## An argument is a value that you pass into a function to be used as input.Such as the hi in print('hi')

## Parameters: a paremeter is a variable which we use in the function definition.It allows the code to access the arguments
## argument for the value, parameter fot the definition
def greet(lang):
    if lang == 'es':
        print('Hola') # 也可以改成 return 'Hola'
    elif lang == 'fr':
        print('BJ')
    else:
        print('hello')
greet('en')
greet('es')
greet('fr') #lang是任何第一个参数的别名

def daji():
    return "hello"  # return statment decides residual value
print(daji(), "hh")


def addtwo(a,b):
    added = a+b
    return added
print(addtwo(2,4))  #add 函数








