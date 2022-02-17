import Hospital_Patient_Distribution as hpd
import math
# this is the hospital state class, it has the left over capacity so that we can find out if there is left over space and it has the hospital state chance because we use a poisson distribution to find the percent chance
# that x number of patients will arrive in a period of time we multiple that chance by the stateChance in the given object to find the total chance that the hospital will end up in this state
# to find chance of Y number of code zeros you add up all the stateChances of each hospital state that has Y amount of code zeros (after adding in ambulances)
class HospitalState:
    '''
        this object represents a hospitals state
        
        :param self.leftOverCap: how many more people the hospital can fit
        :param self.stateChance: the chance that the hospital ends up in this state
        :param self.time: the time of the day this state takes place in
        :type self.leftOverCap: int
        :type self.stateChance: float
        :type self.time: int
    '''
    def __init__(self, leftOverCap, stateChance, time):
        self.leftOverCap = leftOverCap
        self.stateChance = stateChance
        self.time = time
    def updateState(self,x):
        '''
            take the current state of hospital and return a new hospital with a new state depending on the amount of patients that entered
            
            :param x: the amount of people that entered
            :type x: int
            :return: returns a new hospitalstate with updated capacity and chance
            :return type: HospitalState
        '''
        chance = self.stateChance * hpd.poisson(x)  # this is to not cause error from storing numbers that are to small
        if chance < 1.0 * math.exp(-99):
            chance = 1.0 * math.exp(-99)
        return HospitalState(self.leftOverCap - x, chance, self.time+1)
    def addPatient(self,x):
        '''
            ONLY USE FOR ADDING AMBULANCE PATIENTS
            this function is for when ambulance drops of its patients you add that into the state (it doesnts change stateChance since
            each state has the same amount of drop off)
            :param x: amount of patients dropped off
            :type x: int
        '''

        self.leftOverCap = self.leftOverCap - x
    def overCapacity(self):
        '''
            this function is used to see if the hospital is over its capacity

            :return: true if it is over capacity false otherwise
            :type return: boolean
        '''

        if self.leftOverCap < 0:
            return True
        else:
            return False
        
    def __str__(self):
        return "left over capacity: " + str(self.leftOverCap) + ", chance of current state: " + str(self.stateChance) + ", at hour: " + str(self.time)
