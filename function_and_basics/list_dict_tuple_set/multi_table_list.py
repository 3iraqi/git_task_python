from validate import  valid_element

def multi_table_lst(x):
    outer_list=[]

    for i in range(1,x+1):
        inner_list=[]
        for j in range(1,i+1):
            inner_list.append(j*i)
        outer_list.append(inner_list)
    return outer_list
    
print(multi_table_lst(valid_element()))


