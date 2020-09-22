#!/usr/bin/env python3

## create a dictionary
switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

## display parts of the dictionary
print( switch["hostname"] )
print( switch["ip"] )

## request a 'fake' key
# print( switch["lynx"] )  

# request a 'fake' key with .get() method
print( "First test - .get()" )
print( switch.get("lynx") )

print( "Second test - .get()" )
print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )

print( "Third test - .get()" )
print( switch.get("version") )

print( "Fourth test - .keys()" )
print( switch.keys() )

print( "Fifth test - .values()" )
print( switch.values() )

print( "Sixth test - .pop()" )
switch.pop("version") # removes this key (and value) pair
print( switch.keys() )   # notice the value of version is gone
print( switch.values() ) # notice the value 1.2

print( "Seventh test - ADD a new value" )
switch["adminlogin"] = "karl08"
print( switch.keys() )
print( switch.values() )

print( "Eighth test - ADD a new value" )
switch["password"] = "qwerty"
print( switch.keys() )
print( switch.values() )

# creates new dictionaries

easy= ["science", "turbo", ["goggles", "eyes"], "nothing"]


medium= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


hard= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


# easy elements
print(easy[2][1], easy[2][0], easy[3])

# medium elements
print(medium[2]{)
