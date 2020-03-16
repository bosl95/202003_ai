def printDayOfTheWeek(y, m, d):
    day_string = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    import datetime
    return day_string[datetime.date(y,m,d).weekday()]

year = int(input('연도를 입력하시오 : '))
month = int(input('월을 입력하시오 : '))
day = int(input('일을 입력하시오 : '))
print("{}년 {}월 {}일은 {}입니다.".format(year, month, day, printDayOfTheWeek(year, month, day)))