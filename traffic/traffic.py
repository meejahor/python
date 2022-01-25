# # Plot the Collatz conjecture from 1..maxSeed with maxSteps per seed
# #2

# import matplotlib.axes as axes
# import matplotlib.pyplot as plt
# import numpy as np
# import math
# import os

# maxSeed = 50
# maxSteps = 200

# def MakeFilename(filename):
#     return os.getcwd() + "/" + filename

# def IsEven(val):
#     return val % 2 == 0

# def CalcNextValue(val):
#     if IsEven(val):
#         val /= 2
#     else:
#         val *= 3
#         val += 1
#     return val

# for seed in range(1, maxSeed):
#     currentValue = seed

#     # because we're drawing lines instead of plotting points,
#     # the first iteration of the loop covers step 1 and 2, the next does 2 and 3, etc
#     # also note that we're 1-based not 0-based
#     currentStep = 2

#     while currentStep <= maxSteps:
#         nextValue = CalcNextValue(currentValue)
#         x = np.linspace(currentStep-1, currentStep, 2)
#         y = np.linspace(currentValue, nextValue, 2)
#         plt.plot(x, y, 'k')
        
#         if nextValue == 1:
#             # we've reached 1 so the conjecture is proved for this seed
#             break

#         currentValue = nextValue
#         currentStep += 1

# #plt.show()
# # plt.savefig(os.getcwd() + '/collatz.png', dpi=300)

# # print(os.getcwd())

# f = open("test.txt", "a")
# f.write("test")
# f.close()

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


    # for _, line in enumerate(f):
    #     print(line)
    