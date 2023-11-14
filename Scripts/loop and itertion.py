# XingJieXingjie

import distutils
n = 5
while n>0 : #如果为真 一直循环 同时输出
    print(n)
    n = n-1 # 没有这个就是infinite loop，而iteration迭代就是n的值不断变化
   # break 放到哪都可以随时中断循环
print('hh')
print(n)

while True:
    line = input('>')
    if line[0] == '#':
        continue # skip to the top of the loop 可以用来提醒你错了，重新输入
    if line == 'done':
        break #直接跳出循环
    print(line)
print('ok')


#while True: #创造出一个无限循环
 #   line = input('>')
  #  if line == 'done':
   #     break
    #print(line)
#print('ok')

for i in [5,4,3,2,1]: # the iteration variable iterates through the squence
    # the block of code is executed once for each value in the squence
    # the iteration variable moves through all of the values in the sequence
    print(i)
print('hh')

# find the largest value

