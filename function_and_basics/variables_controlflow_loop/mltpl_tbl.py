from validate import  valid_element

def mltply_tbl(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(f"{i}*{j}={i*j}")
            
mltply_tbl(valid_element())
