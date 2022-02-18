#!usr/bin/python3
import requests


def getInfo(city):
    """Export data"""
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=00619f8e54d4fbab6229adc88ce63788'

    req = requests.get(url)
    if req.status_code == 200:
        return req.json()
    else:
        return None


def getNews(city):
    """Export News"""
    url = f'https://gnews.io/api/v4/search?q={city}&lang=en&token=f36d6bdff7770c54eae8dc8cbdcfda29'
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return None


def render(DictCity):
    myDict = {}
    myDict = DictCity.copy()
    C = round(float(DictCity['main']['temp'] - 273.15), 1)
    descmin = str(DictCity['weather'][0]['description'])
    descmax = descmin.capitalize()
    myDict['tempC'] = C
    myDict['desc'] = descmax
    return myDict
