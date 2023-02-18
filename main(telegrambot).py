import requests
#below key is accessed after signing up openweather website
key ="b66e184590bd9692daf2b2b9de43d478"

will_rain = False

# As currently there is thunderstorm in São Paulo, therefore this location is used in order to test
parameters = {
    "lat": -23.550520,
    "lon": -46.633308,
    "exclude": "current,minutely,daily",
    "appid": key,
}
# commands of api docs in openweather are used here
response = requests.get("https://api.openweathermap.org/data/2.8/onecall",params=parameters)
response.raise_for_status()
weather_data = response.json()
id = weather_data["hourly"][:12]

# Telegram bot
def telegram_bot_sendtext(bot_message):
    bot_token = '5896718665:AAGpVSCt4LAxTAerWIQd5NAETULBM5Zg7AY'
    bot_chatID = '1394025223'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()

# here, x is weather id. Basically, there are different weather codes which determines the weather conditiond like rain, drizzle, sunny, etc.
# Refer "https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2" to know about these codes
for x in id:
    condition = x["weather"][0]["id"]
    # print(condition)
    if condition<700:
        will_rain = True

# bot sends message via telegram to alert about rain
if will_rain:
    test = telegram_bot_sendtext("Today,it will rain. Do carry your umbrella!!")
    print(test)
