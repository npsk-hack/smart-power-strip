import RPi.GPIO as io

class PowerStrip:
    
    def __init__(self, pins):
        self.pins = pins
        self.pinsNum = len(pins) - 1
        self.appliances = {}
        self.States = {"on":io.LOW, "off":io.HIGH, True:io.LOW, False:io.HIGH}
        io.setwarnings(False)
        io.setmode(io.BCM)
        for i in range(0, self.pinsNum):
            io.setup(self.pins[i], io.OUT)
            io.output(self.pins[i], io.HIGH)
            self.appliances[self.pins[i]] = self.pins[i]
        
    def socketNumToPinNum(self, socketNum):
        return pins[int(socketNum) - 1]
        
    def attachAppliance(self, appliance, socketNum):
        socketNum = int(socketNum)
        if appliance not in self.appliances and socketNum not in self.appliances.values():
            self.appliances[appliance] = socketNum
    
    def detachAppliance(self, appliance):
        if appliance in self.appliances:
            del self.appliances[appliance]
    
    def handleIndividualSocket(self, socketNum, socketState):
        io.output(self.appliances[socketNum], self.State[socketState])

    def handleAllSockets(self, socketState):
        for i in range(0, self.pinsNum):
            io.output(self.pins[i], self.States[socketState])
