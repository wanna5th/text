import os
file = r'D:\python\work\0318.txt'
with open(file, 'r', encoding='utf-8') as f:
     alllines = f.readlines()  # list形式返回txt的所有行  ['打力矩\n', '查找箱变漏油处\n',...]
     # print(lines)

with open(file, 'w', encoding='utf-8') as f:
     for eachline in alllines:
         eachline = eachline.replace(r'3410', '3420')
         #eachline = eachline.replace(r'发电机组', '风机')
         f.write(eachline)
         
#111111111111111
