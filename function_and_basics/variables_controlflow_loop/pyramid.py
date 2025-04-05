# Problem 4 Lab 1
from validate import  valid_element
def draw_pyramid(x):
    for i in range(x+1,1,-1):
        print(i*" ",((x+2)-i)*"*")

draw_pyramid(valid_element('Enter Height '))
