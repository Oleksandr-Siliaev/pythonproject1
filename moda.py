import math
number = ''
test = []
import string
with open("input_10.txt") as file:
    int_number = file.readlines()
    for e in range(1,len(int_number)) :
        number = number +int_number[e]
        test.append(int(number))
        number = ''
print (test)
x1 = []
for i in test:
 if i not in x1:
  x1.append(i)
print(x1)

chast = []
sumchast = []
suma = 0
for y in x1:
 h = 0
 for k in test :
  if(y==k):
   h += 1
 chast.append(h)
 suma += h
 sumchast.append(suma)
print(chast)
for y in range(len(x1)):
  print("Chislo = ",x1[y]," Chastota = ",chast[y]," SukupChast = ", sumchast[y])

n = len(test)
c = 0
m = 0

mediana = len(test)/2
mediana = round(mediana)
mediana = mediana - 1
if n %2  == 0 :
    mediana = (test[mediana]+test[mediana + 1]) / 2
    print('медіана = ' + str(mediana))
else :
    print('медіана = ' +str(test[mediana]))

for i in range (n) :
    c = 0
    for j in range(n) :
        if (test[i] == test[j]) :
            c += 1
    if (c>m) :
        m = c
        moda = test[i]
print ('мода = '+ str(moda))

avg = sum(test) / len(test)
disp = sum((x-avg)**2 for x in test) / len(test)
print('дисперсія = ' +str(disp))

inqRange = math.sqrt(disp)
print ('середнє квадратичне відхилення розподілу = ' + str(inqRange))


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.hist(test,bins = len(test)*5)
plt.xlabel('число')
plt.ylabel('частота')
plt.show()

my_file = open("Result_input_"+str(len(test))+".txt", "w+")
my_file.write("Дані з input_"+str(len(test))+".txt")
for y in range(len(x1)):
    my_file.write("\n число = "+ str(x1[y])+" частота = "+str(chast[y])+"сукупчаст = "+str(sumchast[y]))
my_file.write("\nмедіана = "+ str(mediana)+ "\nмода = "+str(moda)+"\nсереднє квадратичне відхилення = " +str(inqRange)+ "\nдисперсія = "+ str(disp) )
my_file.close()

