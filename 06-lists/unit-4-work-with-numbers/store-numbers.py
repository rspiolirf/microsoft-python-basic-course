gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 # in Newtons, on Earth

print('On Earth, a double-decker bus weighs', bus_weight, 'N')
print('On Mercury, a double-decker bus weighs', bus_weight * gravity_on_planets[0], 'N')