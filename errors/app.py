class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __repr__(self):
        return f'<Car {self.name}{self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        # print('This method is a work in progress')
        # isinstance(car -> variable, Car -> instance
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name}` to the garage, '
                                        f'but you can only add `Car` objects')
        self.cars.append(car)


ford = Garage()
new_car = Car('Ford', 'Fiesta')
ford.add_car(new_car)


