import pandas as pd
import tushare as ts
import numpy as np
from datetime import datetime
from datetime import timedelta
#获取10年hs300的日数据
#1. 获取今天的日期
end = str(datetime.today().date())
#2. 开始时间， 10年前
start = str((datetime.today()-timedelta(days=365*10)).date())
#3.获取hs300的10年期数据


ts.set_token("703aa3b4a67b9073fefa5ef596407482a7e2fec4334fd5f7c66332dc")
pro = ts.pro_api()

df = pro.index_dailybasic( ts_code='000300.SH', start_date='20130101',fields='ts_code,trade_date,turnover_rate,pe,pe_ttm')

print(df)



