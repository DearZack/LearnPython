#使用datetime模块
import datetime

print(datetime.date.today().strftime('%d/%m/%Y'))
birthday = datetime.date(1949, 10, 1)
print(birthday.strftime('%d/%m/%Y'))
print(birthday + datetime.timedelta(days=2))
print(birthday.replace(year=birthday.year + 1))