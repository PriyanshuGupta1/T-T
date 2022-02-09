# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:22:25 2022

@author: PRIYANSHU GUPTA
"""

physics=92
chemistry=72 
english=83
maths=65
physics=physics+5
chemistry=chemistry+5
total=physics+chemistry+english+maths
average=total/4
print("The average mark obtained by student is :",average)
if(average>=90):
    print("The Student got O grade.")
elif(average>=80 and average <90):
    print("The Student got E grade.")
elif(average>=70 and average <80):
    print("The Student got A grade.")
elif(average>=60 and average <70):
    print("The Student got B grade.")
elif(average>=50 and average <60):
    print("The Student got C grade.")
elif(average>=40 and average <30):
    print("The Student got D grade.")
else: 
    print("The Student Failed")