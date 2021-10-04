# 크리스마스까지 D-day구현해보기
import datetime

#오늘날짜
today = datetime.date.today()
#2021년 크리스마스 날짜
christmas = datetime.date(2021,12,25)

#d-day 
d_day = christmas - today
print(f"{christmas}까지 {d_day.days}일 남았습니다")
