from tkinter import *
from colors import *
from itertools import combinations
from displayResult import getResult


class elements:
    def __init__(self,root,retrieveSet,type):
        super().__init__()
        self.root = root

        if type == 1:
            self.showElements(retrieveSet)
        elif type == 3:
            self.powerSet(retrieveSet)
        elif type == 4:
            self.rosterMethod(retrieveSet)
        


    def showElements(self, getSets):
        result = None
        if len(getSets) == 0:
            result = "∅"
        else:
            result =  str(set(getSets.split(','))).replace("{","").replace("}","").replace("'","")
        
        lenofset = len(set(getSets.split(",")))
        getResult(self.root, result,lenofset, "Cardinality")
         
    
    def powerSet(self, getSets):
        if len(getSets) == 0:
            result = "{{}}"
            getResult(self.root, result, 1, "Power Set")


        else:        
            listsub = list(set(getSets.split(',')))
            subsets = []
            for i in range(2**len(listsub)):
                subset = []
                for k in range(len(listsub)):            
                    if i & 1<<k:
                        subset.append(listsub[k])
                subsets.append(subset)        
            lenofset = len(subsets)
            result = str(subsets).replace("[","{").replace("]","}").replace("'","")
            getResult(self.root, result, lenofset,"Power Set")

    
    def rosterMethod(self,getSets):
        result = None
        if len(getSets) == 0:
            result = "∅"
        else:
            result =  str(set(getSets.split(','))).replace("'","")
        
        lenofset = ""
        getResult(self.root, result,lenofset, "")
       
