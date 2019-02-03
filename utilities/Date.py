import datetime
# now = datetime.datetime.now()
# print now.year, now.month, now.day, now.hour, now.minute, now.second

class Date:

    def getIntValueFromMonth(month):
        if month == "Jan":
            return 1
        elif month == "Feb":
            return 2
        elif month == "Mar":
            return 3
        elif month == "Apr":
            return 4
        elif month == "May":
            return 5
        elif month == "Jun":
            return 6
        elif month == "Jul":
            return 7
        elif month == "Aug":
            return 8
        elif month == "Sep":
            return 9
        elif month == "Oct":
            return 10
        elif month == "Nov":
            return 11
        elif month == "Dec":
            return 12
        else:
            print("Could not determine month: " + month)
            raise

    def determineYear(month, day):
        now = datetime.datetime.now()
        todayMonth = now.month
        todayDay = now.day
        todayYear = now.year
        
        if ((Date.getIntValueFromMonth(month) > todayMonth) or
            (Date.getIntValueFromMonth(month) == todayMonth and int(day) > todayDay)):
            return str(todayYear - 1)
        else:
            return str(todayYear)

    