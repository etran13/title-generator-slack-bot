import datetime

def makeTitle(name, tutor, key): 
    "Takes input from user and returns the formatted title"
    #name = input("Enter LastNameFirstName: ")
    #key = input("Enter a for LOOP or b for LPC: ")
    if key == "a":
        location = "LOOP"
    elif key == "b":
        location == "LPC"
    else:
        location = "REMOTE"
    return format(name, tutor, getTime(), location)
    
def format(lastNameFirstName, tutor, time, location):
    "Formats the title"
    return (f'{lastNameFirstName}_{tutor}_{getDate()}_{time}_{location}')

def getDate():
    "Returns today's date"
    today = datetime.date.today()
    if today.month > 9 and today.day > 9:
        return (f'{today.year}{today.month}{today.day}')
    elif today.month > 9 and today.day <= 9:
        return (f'{today.year}{today.month}0{today.day}')
    elif today.month <= 9 and today.day > 9:
        return (f'{today.year}0{today.month}{today.day}')
    else:
        return (f'{today.year}0{today.month}0{today.day}')
    
def getTime():
    "Returns the start time of the WF appointment"
    currentHour = datetime.datetime.now().time().hour
    currentMinute = datetime.datetime.now().time().minute
    meridian = "PM"
    if currentHour > 12: 
        printHour = str(currentHour - 12)
    elif currentHour == 12:
        printHour = "12"
    else:
        printHour = currentHour
        meridian = "AM"
    if currentMinute >= 30:
        printMinute = "30"
    else:
        printMinute = "00"
    return (f'{printHour}{printMinute}{meridian}')

