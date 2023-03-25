
# cf. book 7.7 exercises 11-13

def yearLength(year):
    if year % 400 == 0:
        return 366
    elif year % 100 == 0:
        return 365
    elif year % 4 == 0:
        return 366
    else:
        return 365

def monthLength(year,month):
    if month == 2 and yearLength(year) == 366:
        return 29
    elif month == 2:
        return 28
    elif month in [4,6,9,11]:
        return 30
    else:
        return 31

def dateDays(year,month,day):
    days = 0
    for y in range(year):
        days = days + yearLength(y)
    for m in range(1,month):
        days = days + monthLength(year,m)
    return days + day

def dateDiff(year1,month1,day1,year2,month2,day2):
    diff = dateDays(year2,month2,day2) - dateDays(year1,month1,day1)
    return diff

def inputDate(date):
    year,month,day = eval(input("Enter " + date + " in format year,month,day: "))
    return year,month,day
    
def main():
	year1,month1,day1 = inputDate("start date")
	year2,month2,day2 = inputDate("end date")
	print("The difference is", dateDiff(year1,month1,day1,year2,month2,day2))

if __name__ == '__main__':
    main()



