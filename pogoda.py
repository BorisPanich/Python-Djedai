from pyowm import OWM

''' полученный api-код с https://home.openweathermap.org/users/sign_up '''
owm = OWM('d64ed6ddf61fd80c3053d3b2c417c192')

# выбор города для получение данных о погоде
city = input("Input name City: ")
observation = owm.weather_manager().weather_at_place(city)
w = observation.weather

''' искаемые параметры погоды: '''
temperature = w.temperature('celsius')['temp']
clouds = w.clouds
humidity = w.humidity

print("in City now temperature: " + str(temperature) + " from Celsius, " "\n" + "Clouds: " + str(
    clouds) + ", " "\n" + "Humidity: " + str(humidity))

''' Примеры параметров погоды для использования: '''
# w.detailed_status  # 'clouds'
# w.wind()  # {'speed': 4.6, 'deg': 330}
# w.humidity  # 87
# w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# w.rain  # {}
# w.heat_index  # None
# w.clouds  # 75
