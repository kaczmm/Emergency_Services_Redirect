from Hospital import *
import Hospital_Patient_Distribution

class HospitalList:
    '''
        this object represents a list of HospitalStates
        :param self.hList: list of lists of hospitals where the list index is the time of each hospital in that list
        :type self.hList: list of lists of hospitals
    '''
    def __init__(self):
        '''
            the initial hospital capacity is hard coded (100)
            the initial state chance is 1.0 since this is the first state
            the initial time is 0 (start of the day)
        '''
        h = HospitalState(100,1.0,0)
        self.hList = [[h]]
    def createList(self, maxP):
        #TODO: add in user input from table so that each state is updated by ambulance drop offs
        #TODO: add in way for hospital to lose patients (goes from -10 to +10 maybe) with dynamic mean for different times of the day
        #TODO: can be made way more efficient (2 ppl going to hospital then 1 person going is the same as 1 person going then 2 ppl going)
        #TODO: also remember that the states before the hospital is full dont matter (dont need to be stored) BUT they do matter if ambulances dropping people off will make them full
        ## also also, you only need to calculate the chance of the states that happen at the time of ambulance drop off
        
        '''
            this function creates the list of hospital states
            Note: this function creates the list for a 24 hour period

            :param maxP: this is the max amount of patients the will come to the hospital in an hour
            :type maxP: int
        '''
        cTime = 0
        for i in range(14): # loops for 24 cycles (24 hours)
            cList = [] # list of hospitals for current loop
            for k in range(len(self.hList[i])): # need to get all the new states for each hospital from all of the old states
                for j in range(maxP): # in each cycle simulate maxP people
                    #print("j: " + str(j) + " k: " + str(k) + " i: " + str(i))
                    tempH = self.hList[i][k].updateState(j)
                    if tempH.overCapacity() == False: # if after the update the hospital is still under capacity add it to the list
                        cList.append(tempH)
            print(len(cList))
            self.hList.append(cList) #Once all the hospitals from the previous timeslot put their children < maxP into the list cList append that list to the end of hList

    def __str__(self):
        out = ""
        for x in range(len(self.hList)):
            out = out + "timeslot: " + str(x) + "\n"
            for y in range(len(self.hList[x])):
                out= out + str(self.hList[x][y]) + "\n"
        return out
                        
                
                    
                
                
                
    
        
