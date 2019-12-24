import pdb
import math


def test():

    modules = [int(line.rstrip('\n')) for line in open('day1Input.txt')]
    totFuel = 0
    for module in modules:
        fuel = calculateFuel(module)
        tempTot = fuel
        while fuel > 0 :
            fuel = calculateFuel(fuel)
            tempTot += fuel
        totFuel += tempTot
    print(totFuel)

def calculateFuel(mass):
    fuel = math.floor(mass/3) - 2
    if fuel > 0:
        return fuel
    else: 
        return 0

        
        


if __name__ == '__main__':
    test()