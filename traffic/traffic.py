from curses.ascii import isdigit
from posixpath import split

class Street:
    def __init__(self, street_info):
        street_info = [int(val) if val.isdigit() else val for val in street_info.split()]
        self.from_intersection, \
        self.to_intersection, \
        self.name, \
        self.time_to_travel \
        = street_info

class Intersection:
    def __init__(self):
        self.outgoing_streets = {}

    def add_outgoing_street(self, street):
        self.outgoing_streets[street.name] = street

class City:
    def __init__(self):
        self.intersections = {}
        self.streets = {}

    def new_intersection(self, id):
        self.intersections[id] = Intersection()

    def add_street(self, street):
        name = street.name
        self.streets[name] = street
        from_intersection = street.from_intersection
        intersection = self.intersections[from_intersection]
        intersection.add_outgoing_street(street)
    
class Car:
    def __init__(self, car_info):
        self.route = car_info.split()
        self.route.pop(0)


# program begins

city = City()

with open('data') as f:
    city_info = f.readline().strip()
    simulation_length, \
    number_of_intersections, \
    number_of_streets, \
    number_of_cars, \
    points_for_reaching_destination \
    = city_info.split()

    for id in range(int(number_of_intersections)):
        city.new_intersection(id)

    for _ in range(int(number_of_streets)):
        street_info = f.readline().strip()
        street = Street(street_info)
        city.add_street(street)

    for _ in number_of_cars:
        car_info = f.readline().strip()
        Car(car_info)
