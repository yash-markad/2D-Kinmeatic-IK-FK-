"""
Inverse Kinematics

X and Y is a point in Plane
L1 and L2 is length of Base and end Effector

"a" and "b" is a angle between X axis and imaginary line of Base effector(L1)

b = Cos-1((x^2 + y^2 - L1^2 - L2^2)/(2*L1*L2))

a = Tan-1( (y*(L1 + L2*Cos(b)) - x*L2*Sin(b)) / x*(L1 + L2*Cos(b)) + y*L2*Sin(b)))

"""
import math

def IK(L1, L2, X, Y):

    b = math.acos(((X**2 + Y**2) - (L1**2 + L2**2)) / (2*L1*L2))
    a = math.atan((Y*(L1 + L2*math.cos(b)) - X*L2*math.sin(b)) / (X*(L1 + L2*math.cos(b)) + Y*L2*math.sin(b)))
    a = a*(180/math.pi)
    b = b*(180/math.pi)
    return a, b


if __name__ == "__main__":
    x = IK(5, 5,10,10)
    print(x)