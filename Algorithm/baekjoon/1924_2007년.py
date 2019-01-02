import calendar

N = input()

x = int(N.split()[0])
y = int(N.split()[1])

day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

k = calendar.weekday(2007,x,y)

print(day[k])
