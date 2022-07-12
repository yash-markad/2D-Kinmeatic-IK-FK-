"""
for 2D ARM 
Base effector of length (L1) and "a" is angle between L1 and X axis
and end effector(L2) and "b" is angle between L2 and imaginary line of L1 

Forward Kinematics (FK)

x1 = L1Cos(a) 
y1 = L1Sin(a)

x2 = L2Cos(a+b)
y2 = L2Sin(a+b)

Resultant:

X = x1 + x2 = L1Cos(a) + L2Cos(a+b)
Y = y1 + y2 = L1Sin(a) + L2Sin(a+b)


"""

import math

def FK(L1,L2,a,b):
    a = a*math.pi/180
    b = b*math.pi/180
    x1 = L1*math.cos(a)
    y1 = L1*math.sin(a)
    x2 = L2*math.cos(a+b)
    y2 = L2*math.sin(a+b)
    X = x1 + x2
    Y = y1 + y2
    return X, Y


if __name__ == "__main__":
    x = FK(400,400,90,90)
    print(x)