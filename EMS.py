
import time

def energyManagementSystem(measurements, setpoints, timeout):

    failedBatteryChecks = 0
    updateFailedBatteryChecks(measurements, failedBatteryChecks=0)

    if (checkNumberOfFailures(failedBatteryChecks) and updatedOnTime(measurements["dateUpdated"], timeout)):
        if setpoints["power"] > 0: 
             setOutput(measurements["current"]) #battery is charging
        elif setpoints["power"] < 0:
             setOutput(-abs(measurements["current"])) #battery is discharging
        else:
            setOutput(0) #battery is idle
    else:
        setOutput(0) #Battery limits are not respected or not updated on time...



def checkBatteryLimits(measurements):

    minVoltage, maxVoltage = 450, 500 #min and max values need to be implemented
    minCurrent, maxCurrent = 5, 15 #min and max values need to be implemented
    maxTemperature = 75 #max value needs to be implemented

    measuredVoltage = measurements["voltage"]
    measuredCurrent = abs(measurements["current"])
    measuredTemperature = measurements["temperature"]

    if (measuredVoltage < minVoltage or measuredVoltage > maxVoltage):
        return False
    elif (measuredCurrent < minCurrent or measuredCurrent > maxCurrent):
        return False
    elif (measuredTemperature > maxTemperature):
        return False
    else:
        return True

def updateFailedBatteryChecks(measurements, failedBatteryChecks):
    if checkBatteryLimits(measurements):
        failedBatteryChecks = 0
    else: 
        failedBatteryChecks =+ 1

def checkNumberOfFailures(failedBatteryChecks):
    if (failedBatteryChecks >= 3):
        return False
    else:
        return True

def updatedOnTime(timeUpdated, timeout):
    timeDifference = int(time.time()) - timeUpdated #unixtimestamp
    if timeDifference < timeout:
        return True
    else:
        return False




def setOutput(outputCurrent):
    """
    This function returns the output current (in dictionary format: {"current": I})
    """
    print({"current": outputCurrent})




measurements = {
    "voltage": 475,
    "current": 10,
    "temperature": 50,
    "dateUpdated": 1
}

setpoints = {
    "power": 2000
}

energyManagementSystem(measurements, setpoints, timeout=5)
