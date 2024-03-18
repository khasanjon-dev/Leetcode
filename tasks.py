from datetime import datetime

date_str = '2024-04-02'
date = datetime.strptime(date_str, '%Y-%m-%d')

if date < datetime.today():
    print('Sana xato kiritilgan!')
