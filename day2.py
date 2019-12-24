import pdb
import math

def day2():
    intCode = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,2,9,19,23,1,23,6,27,1,13,27,31,1,31,10,35,1,9,35,39,1,39,9,43,2,6,43,47,1,47,5,51,2,10,51,55,1,6,55,59,2,13,59,63,2,13,63,67,1,6,67,71,1,71,5,75,2,75,6,79,1,5,79,83,1,83,6,87,2,10,87,91,1,9,91,95,1,6,95,99,1,99,6,103,2,103,9,107,2,107,10,111,1,5,111,115,1,115,6,119,2,6,119,123,1,10,123,127,1,127,5,131,1,131,2,135,1,135,5,0,99,2,0,14,0]
    #intCode = [1,9,10,3,2,3,11,0,99,30,40,50]
    opCode = 0
    pos = 0
    while opCode != 99:
        opCode = intCode[pos]
        x = intCode[intCode[pos + 1]]
        y = intCode[intCode[pos + 2]]
        out = intCode[pos + 3]
        result : int = None
        if opCode == 1:
            result = code1(x,y)
        elif opCode == 2:
            result = code2(x,y)

           # pdb.set_trace()
        elif opCode == 99:
            continue
        else:
            print("error pos:" + pos)
            return
        if result != None:
            intCode[out] = result

        pos += 4

    #pdb.set_trace()
    print(intCode[0])




def code1(input1, input2):
    return input1 + input2

def code2(input1, input2):
    return input1 * input2


if __name__ == '__main__':
    day2()