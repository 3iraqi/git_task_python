from validate import  valid_element

def draw_pyramid(hight):
    step = []
    for i in range(hight):
        step.append(' ')
        
    for j in range(len(step)):
        step.append('*')
        step.pop(0)
        print(step)
    
  
    
hight= valid_element("enter height:  ")

draw_pyramid(hight)
