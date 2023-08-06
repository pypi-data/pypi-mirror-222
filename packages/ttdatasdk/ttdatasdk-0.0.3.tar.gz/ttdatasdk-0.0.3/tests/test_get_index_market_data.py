import ttdatasdk
import datetime

"""账号认证"""
username = 'admin'
password = 'admin'
ttdatasdk.auth(username, password)

# 沪深300分钟行情数据
factor_list = ['open', 'high', 'low', 'close', 'volume']
# df = ttdatasdk.get_factor(sec_code_list=['000300.SH'], unit='1m', trade_date='2022-12-19', factor_list=factor_list)
df = ttdatasdk.get_factor(sec_code='000300.SH', unit='1d', trade_date='2022-12-19', factor_list=factor_list)
print(df)
