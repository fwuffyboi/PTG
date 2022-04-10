def getWeatherFromLatLon(latitude: float, longitude: float):
    try:
            import time
            import json
            import requests
            from zenlog import log        
            from datetime import datetime

            with open('../../../settings.json', 'r') as settingsFile:
                # understand settings data
                data = settingsFile.read()
                obj = json.loads(data)

                APIGetLang = str(obj['preferredAPILanguage'])
                APIKey = obj['openWeatherMapAPIKey']

	        # requests for the weather.
            final_url = f'http://api.openweathermap.org/data/2.5/weather?appid={APIKey}&lat={str(latitude)}' \
                        f'&lon={str(longitude)}&lang={APIGetLang}&units=metric'

            # turning weather json data into a dict.
            weather_data = (requests.get(final_url).json())

            # if OWM returns err, log it.
            if weather_data['cod'] != 200:
                log.error(weather_data['message'])
                raise weather_data['message']

            # creating these variables ;-;
            weather_main = weather_data['weather'][0]['main']
            weather_desc = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            wind_speed = weather_data['wind']['speed']
            humidity = weather_data['main']['humidity']
            air_pressure = weather_data['main']['pressure']
            latitude = weather_data['coord']['lat']
            longitude = weather_data['coord']['lon']
            sunrise = weather_data['sys']['sunrise']
            sunset = weather_data['sys']['sunset']
            icon_id = weather_data['weather'][0]['icon']

            now = datetime.now()
            return {
                '__DISCLAIMER__': "These units are given in the METRIC system ONLY.",
                'mainWeather': weather_main,
                'weatherDescription': weather_desc,
                'weatherTemperature': temp,
                'WindSpeed': wind_speed,
                'humidity': humidity,
                'airPressure': air_pressure,
                'latitude': latitude,
                'longitude': longitude,
                'completedRequestAt': str(now.strftime("%m/%d/%Y, %H:%M:%S:%f")),
                'sunrise': str(time.strftime("%H:%M", time.gmtime(sunrise))),
                'sunset': str(time.strftime("%H:%M", time.gmtime(sunset))),
                'iconId': icon_id
            }

    except Exception as error:
        log.error("getWeather.py: " + error)
        raise error

def geocodeFromText(location: str):
    try:
        import json, string
        import time
        import requests
        from zenlog import log

        with open('../../../settings.json', 'r') as settingsFile:
            # understand settings data
            data = settingsFile.read()
            obj = json.loads(data)

            APIGetLang = str(obj['preferredAPILanguage'])
            APIKey = obj['openWeatherMapAPIKey']
            url = f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={APIKey}'
            r = requests.get(url)
            results = r.json()
            location_country_code = results[0]['country']
            location_state = results[0]['state']
            location_lat = results[0]['lat']
            location_lng = results[0]['lon']
            location_name = results[0]['local_names'][APIGetLang]
            

            # requests for the weather.
            final_url = f'http://api.openweathermap.org/data/2.5/weather?appid={APIKey}&lat={str(location_lat)}' \
                        f'&lon={str(location_lng)}&lang={APIGetLang}&units=metric'

            # turning weather json data into a dict.
            weather_data = (requests.get(final_url).json())

            if weather_data['cod'] != 200:
                log.error(weather_data['message'])
                raise weather_data['message']

        return {
            "name": location_name,
            "lat": location_lat,
            "lon": location_lng,
            "state": location_state,
            "country": location_country_code
        }

    except Exception as error:
        log.error("getWeather.py: " + str(error))
        raise error

def getWeatherFromString(locationAsString):
    latLonOfLoc = geocodeFromText(locationAsString)
    latLonOfLoc = getWeatherFromLatLon(latitude=latLonOfLoc['lat'], longitude=latLonOfLoc['lon'])
    print(latLonOfLoc)

getWeatherFromString("Twickenham")
