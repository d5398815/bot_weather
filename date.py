import datetime


def time_now():
    today = datetime.datetime.today()
    time_now = today.strftime("%A.%H.%M.%S")

    return time_now

    #if float(time_now[-5:]) > 19.00:
        #print("1")
    #else:
        #print("2")


#print(time_now()[-8:-3])

#print(time_now()[-8:])

#time_now()

