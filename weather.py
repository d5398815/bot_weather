import requests
import scr
import complements
import date


city_id = scr.city_id
appid = scr.appid


def request_current_weather(flag):
    if flag == 1:

        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()

            return data
        except Exception as e:
            pass
#что то с прогнозом, я не помню
    #elif flag == 2:
        #try:
            #res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            #data = res.json()
            #for i in data['list']:
                #print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])

        #except:
            ## print("Exception (forecast):", e)
            #pass


# print(request_current_weather(1))


def make_message_weather(data_w):
    description = "Условия: " + str(data_w['weather'][0]['description'])
    humidity = "Влажность: " + str(data_w['main']['humidity']) + " %"
    visibility = "Видимость: " + str(data_w['visibility']) + " метров"
    temp = "Температура: " + str(round(data_w['main']['temp'])) + "°C"
    temp_min = "Минимальная температура: " + str(round(data_w['main']['temp_min'])) + "°C"
    temp_max = "Максимальная температура: " + str(round(data_w['main']['temp_max'])) + "°C"
    speed = "Ветер: " + str(data_w['wind']['speed']) + "м/с"

    if data_w['main']['temp'] <= 2 and (data_w['wind']['speed']) >= 10:
        message_lena = "Надень шапку"

    elif data_w['main']['temp_min'] <= -1:
        message_lena = "Надень шапку"

    elif data_w['weather'][0]['description'] == "дождь":
        message_lena = "Возьми зонт, на улице дождь"

    elif data_w['weather'][0]['description'] == "ясно" and float(date.time_now()[-8:-3]) < 17.00:
        print(date.time_now()[-8:-3])
        message_lena = "Надень солнцезащитные очки"

    else:
        message_lena = "Можно и прогуляться"

        # print("Лена, надень шапку")
        # print("data:", data)

    string = description + '\n' + temp + '\n' + temp_max + '\n' + temp_min + '\n' + visibility + \
             '\n' + speed + '\n' + humidity + '\n \n' + message_lena + '\n \n' + complements.read_data()
    return string
