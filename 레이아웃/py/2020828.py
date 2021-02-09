#20200828 1312 

import mod0828_1312
print("2020828_1312.py exec:",__name__)

print(mod0828_1312.PI)
m1312=mod0828_1312.Math()
print(m1312.solv(3))

#반지름이 5인 원의 둘레를 구하는 코드를 넣으세요

PI = 3.141592
class Math:
	def solv(self, r):
		return PI * r ** 3
	def dull(self, r):
		return 2 * PI * r

def mul(a, b):
	return a*b

print(__name__)

#instance
print(isinstance(m1312, mod0828_1312.math)) #true
#round : 반올림
print(round(3.141592, 2))#자리수
print(round(3.141592))

#divmod : 몫과 나머지를 반환
print(divmod(8,3))

print(sorted([1,5,4,2]))
print(sorted('agcf'))

#** eval eval(expression)
print(eval('1'+'2'))
#aaabbb =   "박중현"
print(eval('aaa'+'bbb'))
print(eval('chr(65)'))