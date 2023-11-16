import random

class ij:
   i=0
   j=0
   value=0

class Obj:
  index=0
  c_i=0 #Linear coefficient
  c_ij=[] #Quadratic coefficients
  c_ijs_average=0 #not included in the mathematical model
  ev_func=0 #not included in the mathematical model
  weight=0
  packed=0 #packed=1 if the object will be inside the knapsack

def linear_search_first_improvement(Objects, Knapsack_capacity):
    print("linear_search_first_improvement")
    List_of_Obj=Objects.copy()
    old_profit=calculate_profit_given_packed_objects(List_of_Obj)
    objects_excluded=[]
    
    cached_List_of_Obj=List_of_Obj.copy()
    k=0 #counter
    S_=0 #new solution
    while S_<old_profit and k<len(List_of_Obj):
        greatest_weight=0
        index_of_greatest_weight=0
        i=0
        while i<len(cached_List_of_Obj):
            if not A_belongs_to_B(i, objects_excluded) and (cached_List_of_Obj[i].packed==1):
               if not i==0:
                   if (cached_List_of_Obj[i].weight>greatest_weight or (cached_List_of_Obj[i].weight==greatest_weight and cached_List_of_Obj[i].ev_func>cached_List_of_Obj[index_of_greatest_weight].ev_func)):
                        greatest_weight=cached_List_of_Obj[i].weight
                        index_of_greatest_weight=i
               else:
                   greatest_weight=cached_List_of_Obj[i].weight
                   index_of_greatest_weight=i
            i=i+1
        
        if not greatest_weight==0:
            cached_List_of_Obj[index_of_greatest_weight].packed=0
            Knapsack_capacity=Knapsack_capacity+cached_List_of_Obj[index_of_greatest_weight].weight
        
        for i in range(len(cached_List_of_Obj)):
           if cached_List_of_Obj[i].packed==0:
               calc_ev_func(cached_List_of_Obj, i)
        
        while 1:
            Capacity_verif=Knapsack_capacity
            greatest_ev_func=0
            index_of_greatest_ev_func=0
            i=0
            while i<len(cached_List_of_Obj):
                
                if cached_List_of_Obj[i].packed==0 and Capacity_verif-cached_List_of_Obj[i].weight>=0:
                    if not i==0:
                        if (cached_List_of_Obj[i].ev_func>greatest_ev_func or (cached_List_of_Obj[i].ev_func==greatest_ev_func and cached_List_of_Obj[i].weight<cached_List_of_Obj[index_of_greatest_ev_func].weight)):
                            greatest_ev_func=cached_List_of_Obj[i].ev_func
                            index_of_greatest_ev_func=i
                    else:
                        greatest_ev_func=cached_List_of_Obj[i].ev_func
                        index_of_greatest_ev_func=i                    
                
                i=i+1
            
            if not greatest_ev_func==0:
                cached_List_of_Obj[index_of_greatest_ev_func].packed=1
                Knapsack_capacity=Knapsack_capacity-cached_List_of_Obj[index_of_greatest_ev_func].weight
            else:
                break
        
        S_=calculate_profit_given_packed_objects(cached_List_of_Obj)

        if S_>old_profit:
            return cached_List_of_Obj
        else:
            objects_excluded.append(index_of_greatest_weight)
            cached_List_of_Obj=List_of_Obj.copy()
        
        k=k+1
    
    return List_of_Obj

def read_instance(file_name):
    n=0
    Constraint_type=0
    Objects = []
    Knapsack_capacity=0
    weights=0
    
    f=open(file_name, "r")

    Instance_name=f.readline()
    n=int(f.readline())

    #Assignment of the linear coefficients to a list:
    c_is=f.readline().split()

    for i in range(len(c_is)):
        #Add one more object to the Objects list
        Objects.append(Obj())

        #Assignment of the values of the list to each object's linear coefficient
        Objects[len(Objects)-1].c_i=int(c_is[i])
        Objects[len(Objects)-1].index=i

    for i in range(len(Objects)-1):
        #Assignment of the quadratic coefficients to a list, per iteration
        c_ijs=f.readline().split()

        Objects_list_initialized=0

        for j in range(len(c_ijs)):
           if Objects_list_initialized==0:
                Objects[i].c_ij=[]
                Objects_list_initialized=1
           #Assignment of the values of the list to each item of the quadratic coefficients list in each object
           Objects[i].c_ij.append(ij())
        
        for j in range(len(Objects[i].c_ij)):        
           Objects[i].c_ij[j].value=int(c_ijs[j])
           #'Coordinates' of each quadratic coefficient in the list, this is for convenience at the time of evaluating the total profit
           Objects[i].c_ij[j].i=i
           Objects[i].c_ij[j].j=j+i+1

        #print(f"Objects[{(n-1)-i}].c_ij: {Objects[(n-1)-i].c_ij}")

    f.readline()

    Constraint_type=int(f.readline())
    Knapsack_capacity=int(f.readline())

    #Assignment of the weights of the objects to a list
    weights=f.readline().split()
    for i in range(n):
        #Assignment of each item in the list to each object's weight
        Objects[i].weight=int(weights[i])
   
    f.close()
    
    #results[0]= n
    #results[1]= Constraint_type
    #results[2]= Objects
    #results[3]= Knapsack_capacity
    
    results= []
    results.append(n)
    results.append(Constraint_type)
    results.append(Objects)
    results.append(Knapsack_capacity)
    
    return results

def calc_ev_func(List_of_Obj, index):
    quadratic_index=0
    List_of_Obj[index].ev_func=0
    List_of_Obj[index].ev_func=List_of_Obj[index].ev_func+List_of_Obj[index].c_i
    for k in range(len(List_of_Obj[index].c_ij)):
        quadratic_index=List_of_Obj[index].c_ij[k].j
        if List_of_Obj[quadratic_index].packed==1 and not quadratic_index==index:
            List_of_Obj[index].ev_func=List_of_Obj[index].ev_func+List_of_Obj[index].c_ij[k].value
    
def is_solution_feasible(List_of_Obj, Knap_capacity):
    accumulated_weight=0
    
    for i in range(len(List_of_Obj)):
        if List_of_Obj[i].packed==1:
            accumulated_weight=accumulated_weight+List_of_Obj[i].weight
    
    if accumulated_weight<=Knap_capacity:
        return 1
    print("Solution is not feasible")
    return 0

#Sort, with the quicksort algorithm, all the objects from greatest to lowest decision variable (ev_func) value
def quicksort_by_attribute(List_of_Obj, attribute):
    if len(List_of_Obj) <= 1:
        return List_of_Obj

    pivot_idx = len(List_of_Obj) // 2 # Choose pivot as the middle element
    pivot = getattr(List_of_Obj[pivot_idx], attribute)
 
    # Partition the list into two sublists
    smaller = [obj for obj in List_of_Obj if getattr(obj, attribute) < pivot]
    equal = [obj for obj in List_of_Obj if getattr(obj, attribute) == pivot]
    greater = [obj for obj in List_of_Obj if getattr(obj, attribute) > pivot]
    
    if attribute=="ev_func":
        return quicksort_by_attribute(greater, attribute) + equal + quicksort_by_attribute(smaller, attribute)
    if attribute=="weight":
        return quicksort_by_attribute(smaller, attribute) + equal + quicksort_by_attribute(greater, attribute)
    if attribute=="index":
        return quicksort_by_attribute(smaller, attribute) + equal + quicksort_by_attribute(greater, attribute)

def print_Objects(List_of_Obj, n):
   print("List_of_Obj, quad and linear coeffs.:\n")
   for i in range(n-1):
      print(f"{i:5d}", end="")
   print()
   for i in range(n):
      print(f"{i:4d}", end="")      
      for j in range(n-len(List_of_Obj[i].c_ij)-1):
         print(" -  ", end="")      
      print(f"{List_of_Obj[i].c_i:4d}", end="")      
      for j in range(len(List_of_Obj[i].c_ij)):
         print(f"{List_of_Obj[i].c_ij[j].value:4d}", end="")
      print()

def calculate_profit_given_packed_objects(List_of_Obj):
    print("calculate_profit_given_packed_objects")
    Profit=0
    for i in range(len(List_of_Obj)):
        if List_of_Obj[i].packed==1:
            Profit=Profit+List_of_Obj[i].c_i
            for j in range(len(List_of_Obj[i].c_ij)):
                #print(List_of_Obj[i].c_ij[j].value)
                if List_of_Obj[List_of_Obj[i].c_ij[j].j].packed==1:
                    Profit=Profit+List_of_Obj[i].c_ij[j].value
    return Profit

def A_belongs_to_B(Num, List_of_Num):
    for i in range(len(List_of_Num)):
        if Num==List_of_Num[i]:
            return 1
    return 0

def heuristic(Objects, Knapsack_capacity):
    List_of_Obj=Objects.copy()
    Capacity_verif=Knapsack_capacity

    greatest_value=0
    index_of_greatest_value=0

    for O in range(len(List_of_Obj)):
            
        #Calculate the ev_func of all unpacked List_of_Obj:
        for i in range(len(List_of_Obj)):
            if List_of_Obj[i].packed==0:
                calc_ev_func(List_of_Obj, i)
            #print(f"ev_func of Obj[i]={List_of_Obj[i].ev_func}")
            
        i=0
        while i<len(List_of_Obj) and List_of_Obj[i].packed==0 and (Capacity_verif-List_of_Obj[i].weight)>=0:
            if not i==0:
                if (List_of_Obj[i].ev_func>greatest_value or (List_of_Obj[i].ev_func==greatest_value and List_of_Obj[i].weight<List_of_Obj[index_of_greatest_value].weight)):
                    index_of_greatest_value=i
            else:
                index_of_greatest_value=i
            i=i+1                    

        if not greatest_value==0:
            List_of_Obj[index_of_greatest_value].packed=1
            Capacity_verif=Capacity_verif-List_of_Obj[index_of_greatest_value].weight
            #print(f"Object {List_of_Obj[index_of_greatest_value].weight} packed")
            print(f"Packed object info: EV_FUNC:{List_of_Obj[index_of_greatest_value].ev_func}, WEIGHT={List_of_Obj[index_of_greatest_value].weight}")
                
        greatest_value=0
        index_of_greatest_value=0

        return List_of_Obj

def Randomized_Constructive_Heuristic(List_of_Obj, Knapsack_capacity):
    print("Randomized_Constructive_Heuristic")
    cached_List_of_Obj=List_of_Obj.copy()
    Capacity_verif=Knapsack_capacity
    cached_List_of_Obj_length=len(cached_List_of_Obj)
    k=random.randrange(1, cached_List_of_Obj_length)
    random_index=0
    packed_objects=0
    
    while packed_objects<cached_List_of_Obj_length:
        #print("    while packed_objects<cached_List_of_Obj_length")
        for j in range(cached_List_of_Obj_length):
            calc_ev_func(cached_List_of_Obj, j)
        
        k_greatest=[]

        i=0
        
        while i<k: #Mientras que los objetos seleccionados sean, en cantidad, igual a k
            #print("        while i<k:")
            greatest_ev_func=0
            index_of_greatest_ev_func=0
            j=0
            while j<cached_List_of_Obj_length:
                #print("            while j<cached_List_of_Obj_length:")
                #print("while j<cached_List_of_Obj_length:")
                if cached_List_of_Obj[j].packed==0 and not A_belongs_to_B(j, k_greatest) and Capacity_verif-cached_List_of_Obj[j].weight>=0:
                    #print("                if cached_List_of_Obj[j].packed==0")
                    if not j==0:
                        if (cached_List_of_Obj[j].ev_func>greatest_ev_func or (cached_List_of_Obj[j].ev_func==greatest_ev_func and cached_List_of_Obj[j].weight<cached_List_of_Obj[index_of_greatest_ev_func].weight)):
                            greatest_ev_func=cached_List_of_Obj[j].ev_func
                            index_of_greatest_ev_func=j
                    else:
                        greatest_ev_func=cached_List_of_Obj[j].ev_func
                        index_of_greatest_ev_func=j
                j=j+1            
            if not greatest_ev_func==0:
                k_greatest.append(index_of_greatest_ev_func)
            else:
                break
            i=i+1

        k=len(k_greatest)
        random_index=random.randrange(0, k)

        if cached_List_of_Obj[random_index].packed==0 and (Capacity_verif-cached_List_of_Obj[random_index].weight)>=0:
            cached_List_of_Obj[random_index].packed=1
            Capacity_verif=Capacity_verif-cached_List_of_Obj[random_index].weight
            packed_objects=packed_objects+1
            #print(f"Object {cached_List_of_Obj[random_index].index} packed")


        

    print("Whaddup, return bro?")
    return cached_List_of_Obj


    
        























