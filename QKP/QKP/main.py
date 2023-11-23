from Functions import *

#Open the file with the instance´s name and optimal value, and assign ´the opened file´ to Instances_data
Instances_data=open("C:/Users/hijod/Desktop/QKP-main/QKP/Instances data.txt", "r")

#Open the file that will contain the results obtained, and assign that ´opened file´ to Results_file
Results_file=open("C:/Users/hijod/Desktop/QKP-main/QKP/Results.txt", "w")
#Erase the contents of Results_file, so we can overwrite its contents with the most recent results
Results_file.write("")
#Close the file
Results_file.close()

#Reopen the file, but now in ´append mode´, so we can just append each new result without overwriting any previous contents
Results_file=open("C:/Users/hijod/Desktop/QKP-main/QKP/Results.txt", "a")

i=0

#while (the next line read in the file with the instances´ data is not equal to "EOF", that stands for "End Of File")
while i<29:

    #IF ELSE that determines what line in the Instances_data file to assign to the Optimal and Instance_name variables,
    #in case that i (the iteration variable) is an even number, the first 
    Instance_name=Instances_data.readline().replace("\n", "")
    Optimal=Instances_data.readline().replace("\n", "")
    
    Path=""
    Path="C:/Users/hijod/Desktop/QKP-main/QKP/Instances/" + Instance_name + ".txt"
    
    #Append the results of the Instance processing in the Results_file file
    Results_file.write(f"{Calculate(Path,Optimal)} \n")
    i=i+1
