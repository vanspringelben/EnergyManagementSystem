
import time

class EMS:
    INTERVAL = 1

    minVoltage, maxVoltage = 450, 500 #min and max values need to be fetched
    minCurrent, maxCurrent = 5, 15 #min and max values need to be fetched
    maxTemperature = 75 #max value needs to be fetched

    measurements = {}
    setpoints = {}
    timeout = 5

    def EMS(self):
        while(True):
            self.fetchMeasurements()
            self.updateFailedBatteryChecks()
            
            if self.checkConditions():
                if self.setpoints["power"] > 0: 
                    self.outputCurrent = self.measurements["current"] #battery is charging
                elif self.setpoints["power"] < 0:
                    self.outputCurrent = -abs(self.measurements["current"]) #battery is discharging
                else:                        
                    self.outputCurrent = 0 #battery is idle
            else:
                self.outputCurrent = 0 #Battery limits are not respected or not updated on time...
            
            self.setOutput()
            time.sleep(self.INTERVAL)

    def fetchMeasurements(self):
        """
        This function fetches data from the endpoint: measurements and setpoints
        """
        self.measurements = {
            "voltage": 475,
            "current": 10,
            "temperature": 50,
            "dateUpdated": 1643837764 #unixtimestamp
        }
        self.setpoints = {
            "power": 2000
        }

    def checkBatteryLimits(self):
    
        self.measuredVoltage = self.measurements["voltage"]
        self.measuredCurrent = abs(self.measurements["current"])
        self.measuredTemperature = self.measurements["temperature"]

        if (self.measuredVoltage < self.minVoltage or self.measuredVoltage > self.maxVoltage):
            return False
        elif (self.measuredCurrent < self.minCurrent or self.measuredCurrent > self.maxCurrent):
            return False
        elif (self.measuredTemperature > self.maxTemperature):
            return False
        else:
            return True

    def updateFailedBatteryChecks(self):
        if self.checkBatteryLimits():
            self.failedBatteryChecks = 0
        else: 
            self.failedBatteryChecks =+ 1

    def checkConditions(self):
        if (self.failedBatteryChecks >= 3):
            return False
        elif (int(time.time()) - self.measurements["dateUpdated"] > self.timeout):
            return False
        else:
            return True

    


    def setOutput(self):
        """
        This function returns the output current (in dictionary format: {"current": I})
        """
        print({"current": self.outputCurrent})


myEMS = EMS()
myEMS.EMS()