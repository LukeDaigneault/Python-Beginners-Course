from datetime import datetime
import time

dt1 = datetime(2019, 1, 1)

dt2 = datetime.now()

dt = datetime.strptime("2019/01/01", "%Y/%m/%d")

dt = datetime.fromtimestamp(time.time())

print(dt)

print(f"{dt.year}/{dt.month}")

print(dt.strftime("%Y/%m"))

print(dt2 > dt1)
