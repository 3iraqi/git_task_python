from person import Person
# from car import Car

class Employee (Person):
    
    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        
        
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID must be a positive integer.")
        self._id = value

    @property
    def car(self):
        return self._car
    
    @car.setter
    def car(self, value):
        if value is None:
            raise ValueError("Employee must have a car.")
        self._car = value

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format.")
        self._email = value

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value

    @property
    def distanceToWork(self):
        return self._distanceToWork
    
    @distanceToWork.setter
    def distanceToWork(self, value):
        if value < 0:
            raise ValueError("Distance to work cannot be negative.")
        self._distanceToWork = value
    
    def work(self,hours):
        '''
        h = 8  -> Happy
        h > 8  -> Tired
        h < 8  -> Lazy
        '''
        if hours<=0:
            return "invalid input"
        
        if hours == 8:
            self.mood = "Happy"
        elif hours < 8:
            self.mood = "Lazy"    
        elif hours > 8:
            self.mood = "Tired"
        return f"{self.name} worked for {hours} hours and now feels {self.mood}"
    
    def drive(self,distance):
        '''
        call run() method and give it distance and velocity
        '''
        if self.car:
            self.car.run(distance, self.car.velocity)
        else:
            print(f"{self.name} has no car to drive.")
        

    def refuel(self,gasAmount=100):
        '''
        add gas amount to fuelRate
        '''
        if not self.car:
            print("No car assigned to refuel.")
            return
        
        if (self.car.fuelRate + gasAmount)>100:
            self.car.fuelRate  = 100
            print(f"Refueled car by {gasAmount} liters and now has {self.car.fuelRate} liters and you waste {(self.car.fuelRate+gasAmount)-100}")            
        elif self.car.fuelRate==100:
            print("Car is full fueled")
        
        else:
            self.car.fuelRate += gasAmount
            print(f"Refueled car by {gasAmount} liters and now has {self.car.fuelRate} liters")
            
    def __str__():
        ...

    def send_mail(self):
        pass
    
    