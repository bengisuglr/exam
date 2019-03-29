#Bengisu Güler, 2076347, group2
#Business Case for coffee. owner doesn't wan to run out of coffee but wants to keep them fresh. find a constan level q for order.

import pandas as pd
import numpy as np

def process_data_forcost(filename):
    df = pd.read_csv(filename, delim_whitespace=True)
    cost = np.asarray(df["Cost"])
    return cost

def process_data_forpurchase(filename):
    df = pd.read_csv(filename, delim_whitespace=True)
    purchase = np.asarray(df["Bought"])
    return purchase

def process_data_forconsumed(filename):
    df = pd.read_csv(filename, delim_whitespace=True)
    consumed = np.asarray(df["Consumed"])
    return consumed
def total_order(purchase):
    totalorder = 0
    for i in range(0,len(purchase)):
        totalorder = totalorder + purchase[i]
    return totalorder

def current_cost(cost,purchase):
    totalcost = 0
    for i in range(0,len(cost)):
        totalcost = totalcost + cost[i]*purchase[i]
        unitcost = totalcost / (totalorder/len(purchase))
    return unitcost

def Q(consumed):
    totalconsumed = 0
    for i in range(0,len(consumed)):
        totalconsumed = totalconsumed + consumed[i]
    avgconsumed = totalconsumed / len(consumed)
    return avgconsumed

def new_cost(cost,avgconsumed):
    #since we are trying to find q*cost1 + q*cost2 + q*costn;
    #we can write the fuction to find q*(sum of all costs)
    sumofcosts=0
    for i in range(0,len(cost)):
        sumofcosts= sumofcosts + cost[i]
    newcosttotal = avgconsumed*sumofcosts
    newcost = newcosttotal / (avgconsumed)
    return newcost

#total amount ordered and paid now

cost = process_data_forcost("data.txt")
purchase = process_data_forpurchase("data.txt")
print("costs are", cost)
print("purchases are", purchase)
totalorder = total_order(purchase)
print("\n")
print("total order is", totalorder, "coffees")
print("\n")
currentcost = current_cost(cost,purchase)
print("total current cost is", currentcost, "TL")

#order quantity that wont run out.
print("\n")
consumed = process_data_forconsumed("data.txt")
print("consumption of cutomers are", consumed)
avgconsumed = Q(consumed)
print("average order that would be more efficient", int(avgconsumed))

#new total cost
print("\n")
newcost_withQ = new_cost(cost,avgconsumed)
print("new cost with order amount Q is:", newcost_withQ, "TL")