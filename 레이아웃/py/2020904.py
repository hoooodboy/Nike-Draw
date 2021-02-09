#2020904_1312

#예외처리
#try, except, finally
try:
    4/0
except:
    print("ERROR Zrodivision!")

try:
    4/0
except ZeroDivisionError as e:
    print(e)

try:
    a=[1,2,3]
    print(a[4])
except IndexError as e:
    print(e)

f=open("test.txt", 'w')
try:
    pass
finally: #에러또는ㅇ 로류의 발생에 무관하게 실행
    f.close()

#  끄레드
import threading #쓰레드 사용

import time
def t1312_task():
    for i in range(5):
        time.sleep(1)
        print("working:%d" %i)
"""
print("F start.")
t1=time.time()
for i in range(5):
    t_1312_task()
t2=time.time()
print("F end", t2-t1)
"""
threads=[]
for i in range(5):
    t=threading.Thread(target=t1304_task)
    threads.append(t)
tt1=time.time()
print("T start!")
for t in thread:
    t.start()
tt2=time.time()
print("T end!", tt2-tt1)