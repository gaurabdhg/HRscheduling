import csv
import numpy as np
import pyworkforce

class dataClass:
    def __init__(self):
        self.data=False
        self.table1=self.readf1()
        self.table2=self.readf2()
        self.table3=self.readf3()
        self.tablemerge=self.merge()
    
    def readf1(self):
        t1=np.ones((5))
        return t1

    def readf2(self):
        t2 =np.ones((5))
        return t2

    def readf3(self):
        t3  =np.ones((5))
        return t3

    def merge(self):
        tm =np.ones((5))
        return tm

    def schedule(self):

        #call pyworkforce
        #get data in tablenamed data
        #save data to a file
        self.data=True
        return
    
    def outtable(self):
        return