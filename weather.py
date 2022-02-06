import requests


def check_conditions(zipcode):

    if type(zipcode) != int:
        raise Exception

    weather_call = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid=bd85bd1838a37384556ace68c693d987")

    # return [temp, conditions]
    temp = round(
        ((int(dict(weather_call.json())["main"]["temp"]) - 273.15) * 1.8 + 32), 2)
    # cond = int(dict(weather_call.json())["weather"][0]["id"])

    return temp
