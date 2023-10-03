gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in Newtons, on Earth

print('On Earth, a double-decker bus weighs', bus_weight, 'N')
print('The lightest a bus would be in the solar system is', bus_weight * min(gravity_on_planets), 'N')
print('The heaviest a bus would be in the solar system is', bus_weight * max(gravity_on_planets), 'N')