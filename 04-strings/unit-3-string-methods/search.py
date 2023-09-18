print('Moon' in 'This text will describe facts and challenges with space travel')

print('Moon' in 'This text will describe facts about the Moon')

temperatures = 'Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'
print(temperatures.find('Moon'))

temperatures = 'Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'
print(temperatures.find("Mars"))

temperatures = 'Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'
print(temperatures.count('Mars'))
print(temperatures.count('Moon'))

# strings in Phyton are case sensitive
print('The Moon And The Earth'.lower())
print('The Moon And The Earth'.upper())

temperatures = 'Mars Average Temperature: -60 C'
parts = temperatures.split(':')
print(parts)
print(parts[-1].strip())

mars_temperature = 'The highest temperature on Mars is about 30 C'
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

print('-60'.startswith('-'))

if '30 C'.endswith('C'):
    print('This temperature is in Celsius')