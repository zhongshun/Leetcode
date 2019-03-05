days = [1,3,7]
costs = [1,4,20]

def OneDayPass(days):
    return days[1:]

def WeekPass(days):
    Initial = days[0]
    Length = len(days)
    for i in range(Length):
        if days[0] <= Initial + 6:
            days = days[1:]
    return days

def MonthPass(days):
    Initial = days[0]
    Length = len(days)
    for i in range(Length):
        if days[0] <= Initial + 29:
            days = days[1:]
    return days

print(OneDayPass(days))
print(WeekPass(days))
print(MonthPass(days))



def Spend(days, costs ,Totoal_cost):
    if days:
        return min(Spend(OneDayPass(days), costs, Totoal_cost + costs[0]),
                   Spend(WeekPass(days), costs, Totoal_cost + costs[1]),
                   Spend(MonthPass(days), costs, Totoal_cost + costs[2]))
    else:
        return Totoal_cost

print(Spend(days,costs,0))
