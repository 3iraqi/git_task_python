class Car:
    
    def __init__(self,name,fuelRate,velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Car name must be a non-empty string.")
        self._name = value
        
    @property
    def fuelRate(self):
        return self._fuelRate
    
    @fuelRate.setter
    def fuelRate(self, value):
        if not (0 <= value <= 100):  # Assuming fuel rate is a percentage (0-100%)
            raise ValueError("Fuel rate must be between 0 and 100.")
        self._fuelRate = value

    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity(self, value):
        if not (0 <= value <= 200):
            raise ValueError("Velocity must be between 0 and 200 km/h")
        self._velocity = value
        
    def run(self,distance,velocity):
        self.velocity = velocity
        fuel_km=0.1
        fuel_needed = distance * fuel_km
        
        if fuel_needed <= self.fuelRate:
            self.fuelRate -= fuel_needed
            print(f"Car reached the destination at {self.velocity} km/h.")
        else:
            max_distance = self.fuelRate / fuel_km
            self.fuelRate = 0
            print(f"{self.name} ran out of fuel after {max_distance:.2f} km.")
            self.stop()
            
    def stop(self):
        self.velocity = 0
        print(f"{self.name} has stopped.")