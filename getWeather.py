def get_weather_location(givenLocation: str):
    try:
        import json, string
        import sys, time
        import requests, flask

        with open('settings.json', 'r') as settingsFile:
            # understand settings data
            data = settingsFile.read()
            obj = json.loads(data)

            geocoderAPIKey = obj['geocoderAPIKey']
            url = f'https://app.geocodeapi.io/api/v1/search?&apikey={geocoderAPIKey}'
            params = {'text': givenLocation}
            r = requests.get(url, params=params)
            results = r.json()
            location = results['features'][0]['geometry']['coordinates']
            location_lat = location[1]
            location_lng = location[0]

            with open('settings.json', 'r') as settingsFile:
                # understand data (bruh)
                data = settingsFile.read()
                # parse file
                obj = json.loads(data)
                # get values
                # getting api key
                # print("Api Key://  " + "*" * len(str(obj['OWMAPIKey'])))
                api_key = str(obj['OWMAPIKey'])
                # getting language (english obvs but yknow. we need it for api requests ;-;)

                lang = str(obj['language'])
                # getting request refresh time.

            # requests for the weather.
            final_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&lat={str(location_lat)}' \
                        f'&lon={str(location_lng)}&lang={lang}&units=metric'

            # turning weather json data into a dict.
            weather_data = (requests.get(final_url).json())
            # print(weather_data)

            if weather_data['cod'] == 401:
                with open("applicationErrorLog.txt", "a") as logFile:
                    toWrite = (f"\nipAddr: {str(flask.request.remote_addr)}, time: {str(time.gmtime(time.time()))}, "
                               f"method: {str(flask.request.method)}, url: {str(flask.request.url)}, user-agent: "
                               f"{str(flask.request.user_agent)}, response: {str(flask.Response)}, error: {weather_data['message']}")
                    logFile.write(toWrite)
                print(f"CRITICAL_ALERT://   {weather_data['message']}")
                print(f"The tested API key is '{api_key}'.")
                return 500

            elif weather_data['cod'] == 400:
                print(f"CRITICAL_ERROR://   {weather_data['message']}.")
                with open("applicationErrorLog.txt", "a") as logFile:
                    toWrite = (f"\nipAddr: {str(flask.request.remote_addr)}, time: {str(time.gmtime(time.time()))}, "
                               f"method: {str(flask.request.method)}, url: {str(flask.request.url)}, user-agent: "
                               f"{str(flask.request.user_agent)}, response: {str(flask.Response)}, error: {weather_data['message']}")
                    logFile.write(toWrite)
                # print("The given coordinates were wrong. \n")

            elif weather_data['cod'] == 500:
                print(f"CRITICAL_ALERT://   {weather_data['message']}.")
                with open("applicationErrorLog.txt", "a") as logFile:
                    toWrite = (f"\nipAddr: {str(flask.request.remote_addr)}, time: {str(time.gmtime(time.time()))}, "
                               f"method: {str(flask.request.method)}, url: {str(flask.request.url)}, user-agent: "
                               f"{str(flask.request.user_agent)}, response: {str(flask.Response)}, error: {weather_data['message']}")
                    logFile.write(toWrite)
            # print("It appears that the service is down due to an internal server error. \nPlease try again later.")

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

            # displays whole json api output.
            # print(weather_data)

            weathrprinted = (f"""
    
      (Weather:  {weather_main})
        (Description: {string.capwords(weather_desc)})
        (Temperature:  {temp} °C)
        (Wind Speed:  {wind_speed} mph)
        (Humidity:  {humidity} %)
        (Air Pressure:  {air_pressure} inHg)
      (Location:   
        (Estimated Latitude:  {latitude})
        (Estimated Longitude:  {longitude})
      (Solar:  
        (Current Time: {str(time.strftime("%H:%M:%S", time.gmtime(time.time())))})
          (Sunrise:  {str(time.strftime("%H:%M", time.gmtime(sunrise)))})
          (Sunset:  {str(time.strftime("%H:%M", time.gmtime(sunset)))})
        """)

        return {
            '__DISCLAIMER__': "These units are given in the METRIC system ONLY.",
            'mainWeather': weather_main,
            'weatherDescription': string.capwords(weather_desc),
            'weatherTemperature': temp,
            'WindSpeed': wind_speed,
            'humidity': humidity,
            'airPressure': air_pressure,

            'latitude': latitude,
            'longitude': longitude,

            'completedRequestAt': str(time.strftime("%H:%M:%S", time.gmtime(time.time()))),

            'sunrise': sunrise,
            'sunset': sunset,

            'iconId': icon_id
        }

    except Exception as error:
        import flask, time
        with open("applicationErrorLog.txt", "a") as logFile:
            toWrite = (f"\nipAddr: {str(flask.request.remote_addr)}, time: {str(time.gmtime(time.time()))}, "
                       f"method: {str(flask.request.method)}, url: {str(flask.request.url)}, user-agent: "
                       f"{str(flask.request.user_agent)}, response: {str(flask.Response)}, error: {error}")
            logFile.write(toWrite)
        # print(f"ERROR:// {error}")
        if error == "list index out of range":
            return "The API received faulty or incorrect coordinates."