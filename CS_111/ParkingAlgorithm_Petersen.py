#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Caroline Petersen November 6 2023
# This code calculates the total cost of parking for 3 trucks (t1, t2, t3) in given time intervals based on the provided cost values (a, b, c)

def get_input():
    a, b, c = input().split(" ") #establishing the cost for each parking scenario
    s1, e1 = input().split(" ") #for s1, e1-s3, e3: user enter start and end parking times for truck 1, truck 2, truck 3
    s2, e2 = input().split(" ") 
    s3, e3 = input().split(" ") 
    a = int(a) #change money amount into integers to use the calculate function later
    b = int(b)
    c = int(c)
    t1 = (int(s1), int(e1)) #creating one variable for each truck to organize its specific start/end time in paris
    t2 = (int(s2), int(e2)) #also put in integers in order to use calculate function
    t3 = (int(s3), int(e3))
    return a, b, c, t1, t2, t3

def calculate(a, b, c, t1, t2, t3):
    truck1 = range(t1[0], t1[1]+1) #for truck1-truck3, finding the range of the span between start and end of parking times to identify time periods for each truck
    truck2 = range(t2[0], t2[1]+1)
    truck3 = range(t3[0], t3[1]+1)
    start_time = min(t1[0], t2[0], t3[0]) #locates the beginning time each truck arrived 
    end_time = max(t1[1], t2[1], t3[1]) #locates when each truck left
    total_cost = 0 #initializing beginning parking cost as $0 before finding accumulated cost
    
    for tm in range(start_time, end_time + 1):
        trucks = 0 #initialize no trucks parked at the beginning
        if tm in truck1: #if statements for trucks1-trucks3: checks to see if there are any currently parked trucks at time tm, adjusts variable trucks depending on current number of trucks parked at a given time
            trucks += 1
        if tm in truck2:
            trucks += 1
        if tm in truck3: 
            trucks += 1
        if trucks == 1: 
            total_cost += a * trucks #if only one truck is parked, we add the input $ value to our total cost repeated for however many trucks ocupy the spaces, adjustinting the cost depending on current number of trucks parked at a given time
        elif trucks == 2: 
            total_cost += b * trucks #if two trucks are parked, we add the input $ value to our total cost and repeat this for however many trucks occupy the spaces (multiply by number of trucks)
        else: 
            total_cost += c * trucks #if there is not one or two trucks, then there will be three trucks and we add the input $ value representative of this to our total coast and repeat for however many trucks occupy the spaces
    return total_cost 

if __name__ == "__main__":
    a, b, c, t1, t2, t3 = get_input()
    total_cost = calculate(a, b, c, t1, t2, t3)
    print(total_cost)

