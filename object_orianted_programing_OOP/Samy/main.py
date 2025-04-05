from datetime import datetime
from person import Person
from employee import Employee
from office import Office
from car import Car


def main():


    samy_car = Car("Fiat 128", 100,60)  

    samy = Employee(name="Samy",money= 10000, mood="Happy",car= samy_car,email="Samy@gmail.com",salary=5000,id=1,distanceToWork=10,healthRate=90)
    
    iti_office = Office(name="ITI Smart Village")

    iti_office.hire(samy)

    
    
    print(f"{samy.name} is driving to {iti_office.name}  using his {samy.car.name}")
    samy.drive(20)

    
   
    
    
    
    
if __name__ == "__main__":
    main()