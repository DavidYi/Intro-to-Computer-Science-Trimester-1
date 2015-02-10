import math
def c_circumference (radius):
    circum=math.pi*2*radius
    return circum
def c_area (radius):
    area=math.pi*radius**2
    return area
def main():
    print("%5s%8s%15s" %("Radius","Area","Circumference"))
    for r in range(2,51,4):
        circum=c_circumference(r)
        area=c_area(r)
        print("%5d%9.1f%15.1f"%(r,area,circum))
main()