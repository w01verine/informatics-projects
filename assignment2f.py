
def convertPoundsToKilograms(lbsParm):
    lbsParm = float(lbsParm)
    kilos = lbsParm * 0.453592
    return kilos
    
def convertInchesToMeters(inchesParm):
    inchesParm = float(inchesParm)
    meters = inchesParm * 0.0254
    return meters
    
#function to calculate BMI Body Mass Index.  A BMI of 25 or more is considered overweight
def calculateBMI(poundsParm, heightInchesParm):
    kilos = convertPoundsToKilograms(poundsParm)
    heightInchesParm = float(heightInchesParm)
    meters = convertInchesToMeters(heightInchesParm)
    bmi = kilos/ (meters**2)
    return bmi

