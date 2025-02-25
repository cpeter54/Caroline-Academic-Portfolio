#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Caroline Petersen Oct. 25 2023
#This code processes a list of events where free food is given to calculate the number of unique days within these events that free food is offered. 

def get_input():
    num_events = int(input()) #retrieve user input for number of events free food will be offered at
    events = []
    for event_number in range(num_events): #loops through each event to collect start and end days of free food events
        si, ti = input().split(" ") #reads the input and seperates them with a space to differentiate the starting and end event dates
        si, ti = int(si), int(ti) #convert the free food days to integers to prepare for numberical operations 
        for i in range(si, ti+1): #loops through each event to examine all the free food days within a specific event day (+1 to ti to be inclusive of last day)
            events.append(i) #add each day found to offer free food to the list of events
    return events

def calculate(events):
    unique_days = len(set(events)) #remove duplicate days that free food is offered on and find the number of exact days free food is offered across these events
    return unique_days 

if __name__ == "__main__":
    events = get_input()
    free_food = calculate(events)
    print(free_food)

