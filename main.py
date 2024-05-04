
# import requests
# TOKEN = "6372310639:AAHuusUtsi-Txsa2QjLkl4Ic2uL3jwSQlX4"
# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# print(requests.get(url).json())



# import requests
# TOKEN = "6372310639:AAHuusUtsi-Txsa2QjLkl4Ic2uL3jwSQlX4"
# # chat_id = "5355760547"
# chat_id = "-1002073130979"
# message = "hello from your telegram bot"
# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
# print(requests.get(url).json()) # this sends the message










# import asyncio
# import requests
# import re
# from telegram import Bot
# from tenacity import retry, wait_fixed, stop_after_attempt

# TOKEN = "6372310639:AAHuusUtsi-Txsa2QjLkl4Ic2uL3jwSQlX4"
# # chat_id = "-1002073130979"
# chat_id = "5355760547"
# # Function to get date and time
# def get_date_and_time():
#     url = "https://appointment.bmeia.gv.at/?fromSpecificInfo=True&Request Method=POST&Remote Address=45.86.164.70:443&Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7&Accept-Encoding=gzip, deflate, br, zstd&CalendarId=13713939"
     
#     payload = {}
#     headers = {'Cookie': 'ASP.NET_SessionId=12asek451chk0lj3b5t1ngtd'}
#     response = requests.post(url, headers=headers, data=payload, timeout=10)

#     timestamps = re.findall(r'\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{2}:\d{2} [AP]M', response.text)
#     return timestamps

# @retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
# async def send_message():
#     bot = Bot(token=TOKEN)
#     timestamps = get_date_and_time()
#     for timestamp in timestamps:
#         await bot.send_message(chat_id=chat_id, text=timestamp)
#         await asyncio.sleep(3)  # Add a delay of 1 second between sending messages

# asyncio.run(send_message())



import requests

url = "https://appointment.bmeia.gv.at/?fromSpecificInfo=True&Cache-Control=public, no-store, max-age=0&Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7&Accept-Encoding=gzip, deflate, br, zstd&Referer=https://appointment.bmeia.gv.at/&fromSpecificInfo=True&Remote Address=45.86.164.70:443&Accept-Encoding=gzip, deflate, br, zstd&CalendarId=23134510&PersonCount=1&Command=Next&Office=teheran"

payload = {}
headers = {
  'Cookie': 'ASP.NET_SessionId=1qlt40jx4djjngprb3nrzfkh'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)





