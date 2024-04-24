import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

closet_num= 5526
mark=""
n = int(input())
if (not n):
    closet_num=0
for i in input().split():    
    t = int(i)
    if abs(t) < abs(closet_num):
        closet_num = t
    elif abs(t) == abs(closet_num) and t > closet_num:
        closet_num=t

print(closet_num)