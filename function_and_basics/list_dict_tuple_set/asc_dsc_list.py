# Problem 1 lab
from validate import valid_element
            
    
def create_list(x):
    
    list_ = [valid_element('Enter Element') for _ in range(x)]
    return list_ ,sorted(list_), sorted(list_,reverse=True)
    

lists= create_list(valid_element('Enter the size of list you would to create'))

print(f"""
      Your List {lists[0]}
      Your List In ASC Order {lists[1]}
      Your List In DESC Order {lists[2]}
      """)



