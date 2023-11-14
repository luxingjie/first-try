# XingJieXingjie
# find the largest value
largest_so_far = -1  # flag value 但取值存在风险，要求最大值结果取的值大于样本所有值
print('before',largest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num > largest_so_far:  # if the current is larger, it is the largest so far
        largest_so_far= the_num
    print(largest_so_far , the_num)

print('After', largest_so_far)

# count the numbers of the loop
zork =0
print('before', zork)
for thing in [9,41,12,3,74,15] :
    zork =zork+1
    print(zork,thing)
print('aa',zork)

# count the total and average
total = 0
sa = 0
print('before', total)
for sb in [9,41,12,3,74,15] :
    total= total + sb
    sa = sa + 1
    print(total, sb)
print(total, sa, total/sa)

# filtering in the loop
print('before')
for value  in [9,41,12,3,74,15] :
    if value >20:
        print('large', value)
      #  break # 一旦满足if 就再也不进入if循环了
     #break  随时跳出for循环
print('after')


# boolean variable 不需要输出结果 只需要有没有
found = False
print('before', found)
for  value_1  in [9,41,12,3,74,15] :
    if value_1 == 3:
        found = True
        print(found, value_1)
        break
   # break 只运行到第一个数字
print(value_1)

# flag value取值存在风险
# 取数组的第一个值作为flag value

## 引入none type
# find the smallest value
smallest = None
print('before', smallest)
for  value_2  in [9,41,12,3,74,15] :
    if smallest is  None:   #相当于把数组第一个数字赋值进去 其中is相当于强等于 logic operator
        smallest = value_2
    elif value_2 < smallest: # 这里才正式开始
        smallest = value_2
    print(smallest, value_2)
print('after',smallest)


sh = input('hh')
sr = input('aa')
sh = int(sh)
sr = float(sr)
sssss = sh*sr
print(sssss)

