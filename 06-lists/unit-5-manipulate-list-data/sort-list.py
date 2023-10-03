amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort()
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort(reverse=True)
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

# using sort modifies the current list.