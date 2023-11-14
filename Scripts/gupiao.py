# XingJieXingjie
# coding=utf-8

from pandas_datareader import data as pdr
import yfinance as yf
import os
yf.pdr_override()
code='002261.sz'
stock = pdr.get_data_yahoo(code,'2023-10-1','2023-11-10')
print(stock)    # 输出内容
   # 保存为excel和csv文件
# 定义文件夹路径
folder_path = r'C:\Users\12392\Desktop\stock data'

# 保存为Excel和CSV文件
stock.to_excel(os.path.join(folder_path, code + '.xlsx'))
stock.to_csv(os.path.join(folder_path, code + '.csv'))