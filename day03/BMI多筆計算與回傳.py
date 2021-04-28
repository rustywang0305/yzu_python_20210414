import math

def getbmi(h, w):
    bmi = w / math.pow(h/100, 2)
    return bmi

def getResult(bmi):
    result = "過輕"
    if 18 < bmi < 23:
        result = "正常"
    elif bmi > 23:
        result = "過重"
    return result

def getBMIAndResult(h, w):
    bmi = getbmi(h, w)
    result = getResult(bmi)
    return bmi, result

bmi1 = getbmi(170, 60)
bmi2 = getbmi(180, 90)
print(bmi1, bmi2)

bmi3, result3 = getBMIAndResult(170, 60)
bmi4, result4 = getBMIAndResult(180, 90)
print(bmi3, result3)
print(bmi4, result4)



















