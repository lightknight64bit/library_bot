import requests
import math
import time
distance = 1000
def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftspan = leftMax-leftMin
    rightspan = rightMax-rightMin
    valuescaled = float(value-leftMin)/float(leftspan)
    return rightMin + (valuescaled*rightspan)

for i in range(0, distance+1):
    pwm = 1/math.sqrt(2*3.14*(100000/2))
    pwm *= (math.exp(-1*(i - (distance/2))**2/100000))
    pwm = translate(pwm, 0.00013, 0.0018, 0, 255)
    r = requests.get("http://192.168.4.1/pwm_value?state="+str(pwm))
    
    print(pwm)
    print(str(r.status_code)+"\n")
    

    
