
def energyManagementSystem(measurements, setpoints, timeout):

    batteryOperatingLimits(measurements)
    # If batteryOperatingLimits rerurns False three consecutive times -> output: i=0
    updatedOnTime(measurements["dateUpdated"], timeout)
    # If updatedOnTime returns False -> output: i=0

    # Else if the operating conditions of the battery are ok AND the measurements are updated on time:
    # The output current can be set equal to the measured current = battery charging current

    return
    # For the return, we have to return a dictionary with the current (i=measured current OR i=0)


def batteryOperatingLimits(measurements):
    """
    Function to determine whether the input measurements (voltage, current, temperature) are within
    the specified range. Function returns False when either one of the checks is failing i.e. the input 
    measurement is not within the specified range.
    """
    if not voltageCheck(measurements["voltage"]):
        return False
    elif not currentCheck(measurements["current"]):
        return False
    elif not temperatureCheck(measurements["temperature"]):
        return False
    else:
        return True
    

def voltageCheck(voltageMeasurement):
    """
    Function to check whether the voltage measurement is within the specified range.
    """
    maxVoltage = 500 #get by using function getMaxVoltage
    minVoltage = 450 #get by using function getMinVoltage

    if (voltageMeasurement > minVoltage and voltageMeasurement < maxVoltage):
        return True
    else:
        return False

def currentCheck(currentMeasurement):
    """
    Function to check whether the current measurement is within the specified range.
    """
    maxCurrent = 15 #get by using function getMaxCurrent
    minCurrent = 5 #get by using function getMinCurrent

    if (currentMeasurement > minCurrent or currentMeasurement < maxCurrent):
        return True
    else:
        return False

def temperatureCheck(temperatureMeasurement):
    """
    Function to check whether the temperature measurement is below the max temperature.
    """
    maxTemperature = 75 #get by using function getMaxTemperature

    if (temperatureMeasurement < maxTemperature):
        return True
    else:
        return False


def updatedOnTime(lastUpdate, timeout):
    """
    Function to determine whether the measurements are updated within the timeout period. 
    Returns true if the last update is smaller than the timeout.
    """
    return True




measurements = {
    "voltage": 475,
    "current": 10,
    "temperature": 50,
    "dateUpdated": 1
}

setpoints = {
    "power": 5
}

energyManagementSystem(measurements, setpoints, timeout=5)
