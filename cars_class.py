from abc import ABC, abstractmethod


class Automobile(ABC):
    @abstractmethod
    def __init__(self, name: str, year_of_production: int = 2020, producer: str = None, 
                brand: str = None,
                fuel_consumption: float = 0.0):
        self.name = name
        self.year_of_production = year_of_production
        self.producer = producer
        self.brand = brand
        self.mileage: float = 0.0
        self.fuel_consumption = fuel_consumption
    
    @property
    def save_data(self):
        if self.brand != None and self.producer != None:
            with open('cars_info.csv', mode='a', encoding='utf-8') as file:
                file.write(f'{self.brand};{self.producer}\n')


    def __str__(self):
        if self.brand == None:
            raise NameError('The car has no brand!')
        if self.producer == None:
            raise NameError('The car has no probucer!')
        return f'\nProducer: {self.producer}\nCar name: {self.name}\nCar Brand: {self.brand}'
    
    __repr__ = __str__


class SportCar(Automobile):
    def __init__(self, name: str, year_of_production: int = 2020, producer: str = None, brand: str = None, fuel_consumption: float = 0, max_speed: float = 0, price: str = None):
        super().__init__(name, year_of_production, producer, brand, fuel_consumption)
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.year_of_production = year_of_production
        self.producer = producer
        self.max_speed: str = max_speed
        self.price = price

class Truck(Automobile):
    def __init__(self, name: str, year_of_production: int = 2020, producer: str = None, brand: str = None, fuel_consumption: float = 0, carrying_capacity: str = None):
        super().__init__(name, year_of_production, producer, brand, fuel_consumption)
        self.carrying_capacity: str = carrying_capacity
        self.year_of_production = year_of_production
        self.producer = producer
        self.brand = brand
        self.fuel_consumption = fuel_consumption

sport_car = SportCar('Nissan GT-R')
truck = Truck('MAN TGX')

sport_car.producer = 'Nissan Motors'
truck.producer = 'MAN Truck & Bus AG'

sport_car.brand = 'GT-R'
truck.brand = 'MAN'

sport_car.year_of_production = 2013
truck.year_of_production = 2007

sport_car.fuel_consumption = 100 / 9
truck.fuel_consumption = 2.5 / 1 # km / l

sport_car.max_speed = '320km/h'
sport_car.price = '78 500$'

truck.carrying_capacity = '1200kg'

sport_car.save_data
truck.save_data

# print(sport_car)
# print(truck)
