#클래스 변수
class a1312:
    c_name = ""
a=a1312()
a.c_name="박"
b=a1312()
b.c_name="현"
print(id(a.c_name))
print(id(b.c_name))
a=a1312()
b=a1312()
print(id(a.c_name))
print(id(b.c_name))

#모듈

#first
import mod1312
print(mod1312.add(13,12))
print(mod1312.sub(13,12))

#second
from mod1312 import *
print(add(13,12))
print(sub(13,12))

print(mod1312.PI)
c1312=mod1312.Math()
print(c1312.solv(2))

#내장함수

print(all([1,2,3,4,5]))
print(all([0,1,2,3,4,5]))
print(all(['a','b','','c']))
print(any([1,2,3,4,5]))
print(any([0,1,2,3,4,5]))
print(any([]))

print(chr(99))
print(ord('A'))

for i, name in enumerate(['eb','dc','wp','hd']):
    print(i,name)

print(eval('1+2'))
print(eval("1"+"2"))
print(eval('chr(97)'))


def t_times(x):
    return x*2
print(list(map(t_times,[1,2,3,4])))

print(list(map(lambda b:b*2, [1,2,3,4])))