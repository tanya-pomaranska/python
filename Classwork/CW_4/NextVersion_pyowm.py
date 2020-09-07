from pyowm import OWM

owm = OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key

city=input("Enter your city--> ")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather

print(f"Min temperature {w.temperature('celsius')['temp_min']}")
print(f"Max temperature {w.temperature('celsius')['temp_max']}")
print(f"Temperature {w.temperature('celsius')['temp']}")

temperature = w.temperature('celsius')['temp']
print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")

print("In this city is " + w.to_dict().get('detailed_status'))