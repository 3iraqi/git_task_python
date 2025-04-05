class Office :
    
    def __init__(self, name, ):
        self._name = name
        self._employees = {} 
        
    
    @property
    def name(self):
        return self._name

    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and  len(new_name) > 1: #not new_name.strip() :
            self._name = new_name
        else:
            raise ValueError("Office name must be a valid string with more than one character.")

    # Getter for employees
    @property
    def employees(self):
        return self._employees

    # Prevent employees from being directly set (Optional)
    @employees.setter
    def employees(self, value=None):
        raise AttributeError("Cannot directly assign employees. Use the `hire` method instead.")
     
    
    def get_all_employees(self):
        return self.employees
    
    def get_employee(self,emp_id):
        return self.employees.get(emp_id, "Employee not found")
    
    def hire(self, employee):
        self.employees[employee.id] = employee
    
    def fire(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            
    def check_lateness(self,emp_id, arrival_time):
        if emp_id in self.employees:
            return self.calculate_lateness(9, arrival_time, 0, 0) 
    
    @staticmethod
    def calculate_lateness(targetHour  , moveHour, distance, velocity):
        expected_time = moveHour + (distance / velocity if velocity != 0 else 0)
        return max(0, expected_time - targetHour) 
        
    def deduct(self, emp_id,deduction):
        if emp_id in self.employees:
            self.employees[emp_id].salary -=deduction
    
    def reward(self,emp_id,reward):
        if emp_id in self.employees:
            self.employees[emp_id].salary+=reward
        
        