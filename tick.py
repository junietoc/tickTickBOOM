import datetime

class Tick:
    def __init__(self, title, date):
        self.title = title
        self.date = date

class Deadline:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

print(str(datetime.datetime.today()).split(" ")[0])

