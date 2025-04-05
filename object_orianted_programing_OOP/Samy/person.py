class Person:
    
    def __init__(self, name, money, mood, healthRate):
        self._name = name
        self._money = money
        self._mood = mood
        self._healthRate = healthRate
        
    @property # name Getter
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            """ This check if is a valid name or not """
            raise ValueError("Name must be a non-empty string.")
        self._name = value
    
    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, value):
        if value < 0:
            raise ValueError("Money cannot be negative.")
        self._money = value

    @property
    def mood(self):
        return self._mood
    
    @mood.setter
    def mood(self, value):
        if value not in ["Happy", "Tired", "Lazy"]:
            raise ValueError("Mood must be 'Happy', 'Tired', or 'Lazy'.")
        self._mood = value

    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def healthRate(self, value):
        """Setter for healthRate with validation"""
        if not (0 <= value <= 100):
            raise ValueError("Health rate must be between 0 and 100.")
        self._healthRate = value

    def sleep(self, hours):
        """ 
        h=7 -> happy,  
        h<7 -> tired 
        h>7 -> Lazy
        h <= 0 -> invalid input
        """
        if hours<=0:
            return "invalid input"
        elif hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        elif hours > 7:
            self.mood = "Lazy"    
        return f"{self.name} slept for {hours} hours and now feels {self.mood}"
        
    def eat(self, meals):
        
        '''
        3 meals -> 100 hth
        2 meals -> 75 hth
        1 meals -> 50 hth
        '''
        if meals < 1:
            return "Invalid input: Meals must be at least 1."
        elif meals == 1:
            self.healthRate = 50
        elif meals == 2:
            self.healthRate = 75
        elif meals == 3:
            self.healthRate = 100
        else:
            extra_meals = meals - 3
            self.healthRate = min(100, self.healthRate + (extra_meals * 5)) 
            # if health rate is greater than 100 then equal to 100.
        return f"{self.name} ate {meals} meal(s) and now has {self.healthRate}% health."
    
    def buy(self, items):
        '''
        1 {item} decrease money 10L.E
        '''
        if not isinstance(items, list):
            """ this check the type of items """
            raise TypeError("Items should be a list of item names")
        
        price = 10*len(items)
        
        if self.money < price:
            print(f"You can't buy {items} because you only have {self.money} L.E.")
        else:
            self.money -= price
            print(f"you bought {items} and now you have {self.money} L.E")
        