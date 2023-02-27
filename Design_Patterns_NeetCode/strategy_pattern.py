#Open for extension
#Closed for modification

from abc import ABC, abstractclassmethod

class FilterStrategy(ABC):
    @abstractclassmethod
    def removeValue(self, val):
        pass

class RemoveNegativeStrategy(FilterStrategy):
    def removeValue(self, val):
        return val < 0

class RemoveOddStrategy(FilterStrategy):
    def removeValue(self, val):
        return abs(val)%2


class Values:
    def __init__(self, vals):
        self.vals = vals
    
    def filter(self, strategy):
        res = []
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return res
    
values = Values([-7,-4,-1,0,2,6,9])

print(values.filter(RemoveNegativeStrategy()))
print(values.filter(RemoveOddStrategy()))