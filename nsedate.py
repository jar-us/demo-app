import datetime


def todayDate():
    return datetime.datetime.now()


def futureDate():
    return (datetime.datetime.now() +
            datetime.timedelta(days=600))

def convertToDateTime(nseDate):
    return datetime.datetime.strptime(nseDate, '%d-%b-%Y')
