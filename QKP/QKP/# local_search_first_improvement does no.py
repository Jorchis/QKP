# local_search_first_improvement does not modify the list given in the argument

    #S is the 'old' solution list of items, the packed ones are flagged, from that: Calculate the profil that it'll return and store it in f_S:
    f_S=calculate_profit_given_packed_items(S)
    # Knapsack_capacity is the variable that contains the number that represents the knapsack's total weight capacity
        # Because we will work with the 'S' solution, we must keep a register of the weight already used with that solution,
        # and with that quantity, calculate the knapsack's remaining capacity and store it in Capacity_verif:
    Capacity_verif=Knapsack_capacity-weight_consumed(S)
    #Initialize the new solution S_ap as an empty list:
    S_ap=[]
    #Then, to make the necessary movements to the original solution, it'll be copied to S_ap:
    S_ap=S.copy()

    S_ap_size=len(S_ap) # Variable that will store the size of the item's list S_ap (as a number representing the amount of items in the list),
                        # so that this quantity doesn't have to be calculated every time it is needed

    #f_S_ap is the profit that S_ap would return
    f_S_ap=0

    # excluded_items is a list of indexes 'pointing' to those items that were removed from S (well, S_ap),
    # but that when where removed, the found solution was not better that the older one
    excluded_items=[]
    
    # greatest_weight is the variable that will help to store the current greatest_weight value found some statements later
    greatest_weight=0
    # index_of_greatest_weight is the variable that will help to store the item's index of the current greatest_weight value found
    index_of_greatest_weight=0

    # greatest_ev_func is the variable that will help to store the current greatest_ev_func value found some statements later
    greatest_ev_func=0
    # index_of_greatest_ev_func is the variable that will help to store the item's index of the current greatest_ev_func value found
    index_of_greatest_ev_func=0

    i=0 # 'i' is the iteration variable for the following 'while' loop
    while i<S_ap_size:
        # Find the heaviest PACKED item and remove it from the knapsack, when doing so, keep a record of the item's index and weight value, so that it can be accessed later if necessary
        j=0 #'j' is the iteration variable that will be used in the following while loop
        while j<S_ap_size: #While S_ap is not yet fully traversed
            greatest_weight=0
            if not A_belongs_to_B(j, excluded_items) and (S_ap[j].packed==1): #IF the current item is not an excluded one AND it is packed in S_ap
                if not greatest_weight==0:
                    if (S_ap[j].weight>greatest_weight\
                        or (S_ap[j].weight==greatest_weight\
                            and S_ap[j].ev_func<S_ap[index_of_greatest_weight].ev_func)):
                    # IF the current item's weight is greater than the current greatest weight found
                        # OR (The current item's weight is the same as the current greatest weight found
                        #     AND The current item's ev_func is smaller than the ev_func of the item with the current greatest weight found)
                        #       [because, if 2 or more items with the same weight are found, it is logical to unpack the one with the smallest
                        #        ev_func]
                        greatest_weight=S_ap[j].weight
                        index_of_greatest_weight=j
                else:
                    greatest_weight=S_ap[j].weight
                    index_of_greatest_weight=j
            j=j+1
        if not greatest_weight==0: #IF a greatest_weight value was found
            S_ap[index_of_greatest_weight].packed=0 # Flag the selected item as unpacked
            #Update Capacity_verif, adding to it the weight of the unpacked item, because it's weight is now 'available' to occupy in the knapsack
            Capacity_verif=Capacity_verif+S_ap[index_of_greatest_weight].weight
        
        items_fit=1 #Variable that indicates if more items fit into the knapsack
        while items_fit==1:
            # Calculate the ev_func of every unpacked item in S_ap
            for k in range(S_ap_size):
                if S_ap[k].packed==0:
                    calc_ev_func(S_ap, k)
            #Try to find the best (in terms of its ev_func) unpacked and fitting item
            m=0
            while m<S_ap_size: #While S_ap is not entirely traversed
                if S_ap[m].packed==0 and (Capacity_verif-S_ap[m].weight)>=0: #IF the current item is unpacked and fits:
                    if not greatest_ev_func==0: #IF a value of greatest_ev_func has been found previously:
                        if S_ap[m].ev_func>greatest_ev_func\
                            or (S_ap[m].ev_func==greatest_ev_func\
                                and S_ap[m].weight<S_ap[index_of_greatest_ev_func].weight):
                        #IF the current item's ev_func is greater than greatest_ev_func
                            #OR ((the current item's ev_func is equal to greatest_ev_func)
                                # AND (the current item is lighter than the one previously flagged with the same greatest_ev_func value)):
                            greatest_ev_func=S_ap[m].ev_func
                            index_of_greatest_ev_func=m
                    else: #Execute the following 2 statements only if greatest_ev_func==0
                        greatest_ev_func=S_ap[m].ev_func
                        index_of_greatest_ev_func=m
                m=m+1
            if not greatest_ev_func==0: #IF a valid item is found:
                S_ap[index_of_greatest_ev_func].packed==1 #Flag the item as packed
                Capacity_verif=Capacity_verif-S_ap[index_of_greatest_ev_func].weight #Update Capacity_verif
                #Update greatest_ev_func and index_of_greatest_ev_func
                greatest_ev_func=0
                index_of_greatest_ev_func=0
            else: #if no other item fits:
                items_fit=0 #exit the 'while True' loop
        
        f_S_ap=calculate_profit_given_packed_items(S_ap)

        if f_S_ap>=f_S: #IF S_ap is better than S:
            return S_ap
        else:
            #Add the index of the removed (from S_ap) item to the excluded_items list
            excluded_items.append(index_of_greatest_weight)
            #Set the value of S_ap to S (S_ap=S), because if the solution didn't get better with the movement applied, it won't get better later (as far as I know)
            S_ap=S
        i=i+1

    return S_ap