from datetime import date, datetime, timedelta
from time import time
from locale import setlocale, LC_ALL
from calendar import mdays


setlocale(LC_ALL, 'pt_BR.utf-8')
"""data = datetime(2019, 4, 20, 10, 53, 20)
print(data.strftime('%d/%m/%Y %H:%M:%S'))"""

"""date = datetime.strptime('20/04/2020', "%d/%m/%Y")
print(date)"""

"""date = datetime.strptime('20/04/2020', "%d/%m/%Y")
print(date.timestamp())

print(datetime.fromtimestamp(date.timestamp()))
date = date + timedelta(5)

print(date)

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')

dif = d2 - d1
print(dif)
print(dif.seconds)
print(dif.total_seconds())
print(dif. days)
print(d1.time())
"""

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')


print('dia : '+formatacao1)
print(f"mes atual: {mes_atual}")
