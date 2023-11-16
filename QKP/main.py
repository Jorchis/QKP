import ctypes as ct
import os
import sys
import string
import time
from Calculate import *

Instances_data=open("Instances data.txt", "r")

Results_file=open("Results.txt", "w")
#Erase the contents of Results_file
Results_file.write("")

Results_file=open("Results.txt", "a")

i=0

"""while not Instances_data.readline()=="EOF":
    if(i%2==0):
        Optimal=Instances_data.readline().replace("\n", "")
        Instance_name=Instances_data.readline().replace("\n", "")
    else:
        Instance_name=Instances_data.readline().replace("\n", "")
        Optimal=Instances_data.readline().replace("\n", "")
    Path=""
    Path="./Instances/" + Instance_name + ".txt"
    Results_file.write(Calculate(Path,Optimal)+"\n")
    i=i+1"""

Path="./Instances/Prueba.txt"
Optimal="9566"
print(Calculate(Path,Optimal),"\n")