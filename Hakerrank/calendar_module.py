import calendar
date=input().split()
date=list(map(int,date))
day_number=calendar.weekday(date[2],date[0],date[1])
days_wek=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print(days_wek[day_number])