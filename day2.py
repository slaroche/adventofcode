
import math


def result():
    pos = 0
    intcode = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,2,9,19,23,1,23,6,27,1,13,27,31,1,31,10,35,1,9,35,39,1,39,9,43,2,6,43,47,1,47,5,51,2,10,51,55,1,6,55,59,2,13,59,63,2,13,63,67,1,6,67,71,1,71,5,75,2,75,6,79,1,5,79,83,1,83,6,87,2,10,87,91,1,9,91,95,1,6,95,99,1,99,6,103,2,103,9,107,2,107,10,111,1,5,111,115,1,115,6,119,2,6,119,123,1,10,123,127,1,127,5,131,1,131,2,135,1,135,5,0,99,2,0,14,0]
    # breakpoint()
    while intcode[pos] != 99:
        opcode = intcode[pos]
        x = intcode[intcode[pos +1]]
        y = intcode[intcode[pos + 2]]
        output = intcode[pos + 3]
        print (intcode[pos: pos + 5])   
        if output == 0:
            print(f"{x} {y}")
        # breakpoint()
        intcode[output] = calculate(
            opcode, 
            [
                x, y
            ],
            pos
        )
        pos += 4
        # current_intcode = get_current_intcode(current_pos, intcode)
    return intcode

def opcode_1(x, y):
    return x + y


def opcode_2(x, y):
    return x * y


def get_current_intcode(current_pos, intcode) -> dict:
    return intcode[current_pos:current_pos+5]


def calculate(opcode: int, input: list, current_pos):
    if opcode == 1:
        return opcode_1(*input)
    elif opcode == 2:
        return opcode_2(*input)
    else:
        raise Exception(f"mmmm that is bad! {opcode}, {current_pos}")

if __name__ == '__main__':
    print(result())