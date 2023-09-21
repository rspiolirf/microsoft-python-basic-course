first_planet_input = int(input('Enter the distance from the sun for the first planet in km: '))
second_planet_input = int(input('Entre the distance from the sun for the second planet in km: '))

first_planet_input = int(first_planet_input)
second_planet_input = int(second_planet_input)

distance_km = abs(first_planet_input - second_planet_input)
print(distance_km)