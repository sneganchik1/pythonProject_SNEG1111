# try:
#     file_n = open('lesson12.py')
# except Exception as e:
#     print(f' Error: {e}')
# else:
#     for line in file_n:
#     print(line)
import json

# try:
#     file_n = open('test.txt', 'w')
#     file_n.write('fghvtgcfd')
#     file_n.close()
#
# except Exception as e:
#     print(f' Error: {e}')


# try:
#     file_n = open('test.txt', 'r')
#     data = file_n.read()
#     print(f'Data {data}')
#     file_n.close()
#
# except Exception as e:
#     print(f' Error: {e}')

#
# try:
#     file_n = open('test.txt', 'r')
#     data = file_n.readlines()
#     print(f'Data {data}')
#     file_n.close()
#
# except Exception as e:
#     print(f' Error: {e}')


# with open('test.txt', 'r') as frtry:   #автоматическое закрытие файла. контекст менеджер
#     data = frtry.read()
#     print(data)


#________________________________________
#serializacia

#JSON
# data = [
#     {'1' : 'data1',
#      '2': 'data2'},
#     {'3' : 'data3',
#      '4': 'data4'}
#     ]
#
# json_data = json.dumps(data)
# print(data)
# print(json_data)
#
# data1 = json.loads(json_data)
# print(data1)
#

#________________________________________

#TCP\IP
#
# import requests
#
# try:
#     resp = requests.request('GET', 'http://google.com')
# except Exeption as e:
#     print(f' Error {e}')
#
#
# print(f' Responce {resp}')
# # print(resp.content)
# # print(resp.headers)
# # print(resp.cookies)
# # print(resp.url)
# print(resp.status_code)

#
# import requests
# go_logo = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png'
# try:
#     resp = requests.request('GET', go_logo)
#     print(resp.status_code)
#
# except Exeption as e:
#     print(f' Error {e}')
#
# else:
#     print(f' Response {resp}')
#     data = resp.content
#     with open('google.png', 'wb') as f:
#         f.write(data)



import requests
go_logo = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png'
go = 'https://www.google.com'
try:
    resp = requests.request('GET', go)
    print(resp.status_code)

except Exeption as e:
    print(f' Error {e}')

else:
    print(f' Response {resp.headers}')
    data = resp.content
    con_t = resp.headers['Content-Type']
    print(con_t)
    if 200 <= resp.status_code < 300 and resp.headers['Content-Type'] == 'image/png':
        with open('google.png', 'wb') as f:
            f.write(data)
    else:
        print('unecspected result')
        with open('google.html', 'wb') as f:
            f.write(data)







