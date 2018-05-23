import time
import requests
weather_predictions = None
# Gets weather predictions then caches them to save on API calls. 
def get_weather_predictions():
    global weather_predictions
    if weather_predictions is None:
        # make a call
        url = 'http://api.openweathermap.org/data/2.5/forecast?q=south%20haven,US&appid=500054628f30fd9891b167999db911f8'
        r = requests.get(url)
        r = r.json()
        full_predictions = r['list']
        # Map to predicted rain in mm, predicted temp_max in fahrenheit, and date
        useful_predictions = list(map(lambda entry: [entry['rain']['3h'] if 'rain' in entry else 0, convert_kelvin_to_fahrenheit(entry['main']['temp_max']), convert_epoch_day_to_excel_day(entry['dt']),get_day(entry['dt'])],full_predictions))
        #Every fifth prediction is the middle of the day
        weather_predictions = useful_predictions[4::8]
    print(weather_predictions)
    return weather_predictions

        

def convert_kelvin_to_fahrenheit(num):
    return (9*num)/5 - 459.67
def convert_epoch_day_to_excel_day(tm):
    tm = time.gmtime(int(tm))
    return (tm.tm_wday+1)%7+1
def get_day(tm):
    tm = time.gmtime(int(tm))
    return tm.tm_mday
