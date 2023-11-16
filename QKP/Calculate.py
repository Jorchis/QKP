import ctypes as ct
import os
import sys
import string
import time
from Functions import *

def Calculate(Instance_Path,optimal):
    n=0
    Constraint_type=0
    Objects = []
    Knapsack_capacity=0
    weights=0
    COMPUTING_TIME=0

    if os.path.exists(Instance_Path)==False: #if file does not exist or argument is not included
        print(f"File does not exist")
    else:        
        COMPUTING_TIME=0
        
        values=[]
        
        #sys.argv[0] is the argument given when calling the program Solver.py from the console:
        #the name of the file is Instance_Path
        #python Solver.py [file_name]
        values = read_instance(Instance_Path)
        
        n=values[0]
        Constraint_type=values[1]
        Objects=values[2]
        Knapsack_capacity=values[3]
        Initial_solution=0
        
        #----------------------------------------------APPLYING A HEURISTIC------------------------------------------------------
            
        start_time = time.time() #TIME COUNT STARTS
                
        S=heuristic(Objects, Knapsack_capacity)
        f_S=calculate_profit_given_packed_objects(S)

        i=0
        while i<10:
            S_ap=[] #S_ap = S'
            S_ast=[] #S_ast = S*

            S_ap=Randomized_Constructive_Heuristic(Objects, Knapsack_capacity)
            S_ast=linear_search_first_improvement(Objects, Knapsack_capacity)
            
            f_S_ap=calculate_profit_given_packed_objects(S_ap)
            f_S_ast=calculate_profit_given_packed_objects(S_ast)

            if f_S_ast>f_S:
                S=S_ast
                f_S=f_S_ast
            
            i=i+1

        COMPUTING_TIME=time.time()-start_time

        if is_solution_feasible(S, Knapsack_capacity):
            Profit=f_S
            Optimal=int(optimal)          
            Instance_Name=""
            Instance_Name=Instance_Path.split("/")[2].split(".")[0]
            results=""
            results=f"{Instance_Name},{Profit},{COMPUTING_TIME},{Optimal},{100-(Profit*100)/Optimal:.4f}"
            return results