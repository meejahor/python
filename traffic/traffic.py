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

    def get_array_of_neighbours(self):
        neighbours = []
        for _, street in self.outgoing_streets.items():
            neighbours.append(street.to_intersection)
        return neighbours


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
    city_info = [int(val) for val in city_info.split()]
    simulation_length, \
    number_of_intersections, \
    number_of_streets, \
    number_of_cars, \
    points_for_reaching_destination \
    = city_info

    for id in range(number_of_intersections):
        city.new_intersection(id)

    for _ in range(number_of_streets):
        street_info = f.readline().strip()
        street = Street(street_info)
        city.add_street(street)

    for _ in range(number_of_cars):
        car_info = f.readline().strip()
        Car(car_info)

# create adjacency list

adjacency_list = {}

for id, intersection in city.intersections.items():
    neighbours = intersection.get_array_of_neighbours()
    adjacency_list[id] = neighbours

print(adjacency_list)

# directed graph (edges only go one way)
# connected verts are neighbours (must obey direction of edge)
