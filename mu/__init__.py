import datetime

a = datetime.date.today() + datetime.timedelta(days=1)


print(a.isoformat())
