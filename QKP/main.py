import ctypes as ct
import os
import sys
import string
import time
from Calculate import *

#Open the file with the instance´s name and optimal value, and assign ´the opened file´ to Instances_data
Instances_data=open("Instances data.txt", "r")

#Open the file that will contain the results obtained, and assign that ´opened file´ to Results_file
Results_file=open("Results.txt", "w")
#Erase the contents of Results_file, so we can overwrite its contents with the most recent results
Results_file.write("")
#Close the file
Results_file.close()

#Reopen the file, but now in ´append mode´, so we can just append each new result without overwriting any previous contents
Results_file=open("Results.txt", "a")

i=0

"""
#while (the next line read in the file with the instances´ data is not equal to "EOF", that stands for "End Of File")
while not Instances_data.readline()=="EOF":
    #do
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

#
Path="./Instances/Prueba.txt"
Optimal="9566"
print(Calculate(Path,Optimal),"\n")
