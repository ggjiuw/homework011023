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
    def __init__(self, name: str, year_of_production: int = 2020, producer: str = None, brand: str = None, fuel_consumption: float = 0):
        super().__init__(name, year_of_production, producer, brand, fuel_consumption)
        self.brand = 'GT-R'
        self.fuel_consumption = 100 / 9 # 100km 9l
        self.year_of_production = 2013
        self.producer = 'Nissan Motors'
        self.max_speed: str = '320km/h'
        self.price: str = '78 500$'
        with open('cars_info.csv', mode='a', encoding='utf-8') as file:
            file.write(f'{self.brand};{self.producer}\n')

class Truck(Automobile):
    def __init__(self, name: str, year_of_production: int = 2020, producer: str = None, brand: str = None, fuel_consumption: float = 0):
        super().__init__(name, year_of_production, producer, brand, fuel_consumption)
        self.carrying_capacity: str = '1200kg'
        self.year_of_production = 2007
        self.producer = 'MAN Truck & Bus AG'
        self.brand = 'MAN'
        self.fuel_consumption = 2.5 / 1 # 2.5km 1l
        with open('cars_info.csv', mode='a', encoding='utf-8') as file:
            file.write(f'{self.brand};{self.producer}\n')

sport_car = SportCar('Nissan GT-R')
truck = Truck('MAN TGX')

# print(sport_car)
# print(truck)
