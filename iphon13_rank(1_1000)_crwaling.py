#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import openpyxl

client_id = 'Rgfzr7RrxsnZHURwobRS'
client_secret = 'Qr8DT56ZRU'

start, num = 1, 0

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width = 100
excel_sheet.column_dimensions['C'].width = 100
excel_sheet.append(['랭킹', '제목', '링크'])

for index in range(10):
    start_number = start + (index * 100)
    naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=아이폰13&display=100&start=' + str(start_number)
    header_params = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
    res = requests.get(naver_open_api, headers=header_params)

    if res.status_code == 200:
        data = res.json()
        
        for item in data['items']:
            num += 1
            excel_sheet.append([num, item['title'], item['link']])
    else :
        print("error",res.status_code)
        
excel_file.save('iphon13.xlsx')
excel_file.close()

